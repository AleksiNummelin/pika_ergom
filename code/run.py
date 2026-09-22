#----------------------------------------------
# Python 1-d model for testing ecosystem models
# hagen.radtke@io-warnemuende.de
#----------------------------------------------

#~~~~~~~~~pika-ERGOM~~~~~~~~~~
# pika-ERGOM developed further at the Finnish Meteorological Institute
# andrew.twelves@fmi.fi
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import xarray as xr
import pandas as pd
import load_profiles
import load_weather
import load_mld
import physics_methods
import datetime as dt
import numpy as np
import math
import load_forcing
from sunposition import sunpos
from vmove_explicit import vmove_explicit
from vdiff_explicit import vdiff_explicit
# now import some functions that need to read and write global variables 
# and therefore cannot live in a module
exec(open('cgt_bio_timestep.py').read(),globals())
exec(open('cgt_calc_opacity_bio.py').read(),globals())
exec(open('cgt_init_constants.py').read(),globals())
exec(open('cgt_init_output.py').read(),globals())
exec(open('cgt_init_tracers.py').read(),globals())
exec(open('cgt_mixing_timestep.py').read(),globals())
exec(open('configure.py').read(),globals())
exec(open('myplot.py').read(),globals())

print('~~~~~~~~~~pika-ERGOM~~~~~~~~~')

print('initialization')

with open('configure.py', 'r') as f:
    print(f.read())

#load timestep, initial date etc.
configure()

#initialize the date
current_date        =start_date
current_output_date =start_date
current_output_index=0   # time index in output matrix
max_output_index    =math.floor(repeated_runs*(end_date-start_date)/output_interval)
time_axis           =np.array([0.0 for l in range(max_output_index)])
for i in range(max_output_index):
    time_axis[i]=i*output_interval+start_date

print('  loading physical forcing')

# Specify number of vertical levels
kmax = 18

# open file for ocean physics
ds             = xr.open_dataset(oce_phys_file)
depths         = ds.depth.values
# calculate cell heights from depths
cellheights    = np.zeros((kmax))
cellheights[0] = 2*depths[0]
ch             = np.copy(cellheights[0])
for k in range(1,kmax):
    cellheights[k] = 2*(depths[k] - ch)
    ch = depths[k] + 0.5*cellheights[k]
forcing_days = ds.time.values 
forcing_days = forcing_days - np.datetime64('1899-12-30')
forcing_days = forcing_days.astype('timedelta64[D]').astype(int)
depths = np.squeeze(depths[:kmax])
cellheights = np.squeeze(cellheights[:kmax])

#load physics
def load_matrix(filename):
    input_matrix = np.loadtxt(filename,usecols=range(kmax+4),comments='%')
    # convert 1-d to 2-d array if needed
    if not(isinstance(input_matrix[0],np.ndarray)):
        input_matrix = np.array([input_matrix])
    return(input_matrix)
def load_vector(filename):
    return(np.loadtxt(filename,usecols=range(5),comments='%'))

# Temperature profile [deg. C]
forcing_matrix_temperature   = ds.thetao.values 
# Salinity profile [psu]
forcing_matrix_salinity   = ds.so.values
# Mixed layer depth [m]
forcing_matrix_mld        = ds.mlotst.values

# Downward flux of shortwave light at sea surface [W/m2]
forcing_matrix_light_at_top  = pd.read_csv(solar_file,header=0,usecols=[5])
# Wind speed [m/s]
forcing_matrix_wind  = pd.read_csv(wind_file,header=0,usecols=[5])

# Bottom stress [N/m2]
forcing_matrix_bottom_stress = load_vector('physics/bottom_stress.txt')
# Clear-water opacity [1/m]
forcing_matrix_opacity_water = load_matrix('physics/opacity_water.txt')

forcing_day_temperature = current_date
forcing_index_temperature = np.argwhere(forcing_days==current_date)
forcing_day_salinity    = current_date
forcing_index_salinity = np.argwhere(forcing_days==current_date)
forcing_day_mld    = current_date
forcing_index_mld = np.argwhere(forcing_days==current_date)

forcing_index_light_at_top = 0
forcing_index_bottom_stress = 0
forcing_index_opacity_water = 0
forcing_index_diffusivity = 0

print('  loading biological initialization values')

#load constants
cgt_init_constants()

#load initial tracer concentrations
cgt_init_tracers()

# fill the output with zeros or NaNs
cgt_init_output()

output_vector_temperature   = np.zeros(kmax)
output_vector_salinity      = np.zeros(kmax)
output_vector_opacity       = np.zeros(kmax)
output_vector_light         = np.zeros(kmax)
output_vector_diffusivity   = np.zeros(kmax)
output_scalar_light_at_top  = 0.0;
output_scalar_zenith_angle  = 0.0;
output_scalar_bottom_stress = 0.0;
output_temperature   = np.full((max_output_index,kmax), np.nan)
output_salinity      = np.full((max_output_index,kmax), np.nan)
output_opacity       = np.full((max_output_index,kmax), np.nan)
output_light         = np.full((max_output_index,kmax), np.nan)
output_diffusivity   = np.full((max_output_index,kmax), np.nan)
output_light_at_top  = np.full(max_output_index, np.nan)
output_zenith_angle  = np.full(max_output_index, np.nan)
output_bottom_stress = np.full(max_output_index, np.nan)
output_count  = 0;

print('starting the run');

forcing_scalar_light_at_top = 0
forcing_scalar_wind         = 0
counter = -1 # assumes hourly weather input and time step
# do the timestep
while current_date < repeated_runs*(end_date-start_date)+start_date:
    
    # Load temperature, salinity and mixed layer depth from hydrodynamic model output
    # Temperature profile
    forcing_vector_temperature, forcing_day_temperature , forcing_index_temperature = load_profiles.load_profiles(forcing_matrix_temperature,current_date,forcing_day_temperature,forcing_index_temperature,kmax)
    # Salinity profile
    forcing_vector_salinity   , forcing_day_salinity    , forcing_index_salinity    = load_profiles.load_profiles(forcing_matrix_salinity   ,current_date,forcing_day_salinity   ,forcing_index_salinity   ,kmax)
    
    # Load mixed layer depth from hydrodynamic model output
    forcing_scalar_mld, forcing_day_mld , forcing_index_mld                         = load_mld.load_mld(forcing_matrix_mld,current_date,forcing_day_mld,forcing_index_mld)

    # Load shortwave radiation and wind speed from hourly weather station data, assuming time step is also 1hr
    counter = counter + 1 # assumes hourly weather input and time step
    # Shortwave radiation
    forcing_scalar_light_at_top                               = load_weather.load_weather(forcing_scalar_light_at_top,forcing_matrix_light_at_top,counter)
    # Remove negative values
    forcing_scalar_light_at_top                               = np.nanmax(forcing_scalar_light_at_top,0)
    # Wind speed
    forcing_scalar_wind                                       = load_weather.load_weather(forcing_scalar_wind,forcing_matrix_wind,counter)
    
    # Calculate diffusivity from wind and mixed layer depth, using OpenDrift diffusivity calculation                            #background diffusivity=0
    forcing_vector_diffusivity = physics_methods.verticaldiffusivity_Large1994(forcing_scalar_wind, depths, forcing_scalar_mld,                         0)

    # Bottom stress
    forcing_scalar_bottom_stress, forcing_index_bottom_stress = load_forcing.load_forcing(forcing_matrix_bottom_stress,current_date,start_date,end_date, kmax, forcing_index_bottom_stress)
    
    # Load attenuation coefficient from satellite data?
    forcing_vector_opacity_water, forcing_index_opacity_water = load_forcing.load_forcing(forcing_matrix_opacity_water,current_date,start_date,end_date, kmax, forcing_index_opacity_water) 
    #forcing_vector_opacity_water = 0.18
    #forcing_scalar_opacity, forcing_scalar_opacity , forcing_index_opacity         = load_profiles.load_profiles(forcing_matrix_opacity,current_date,forcing_day_opacity,forcing_index_opacity,kmax)

    # light calculation
    zenith = sunpos(dt.datetime(1899, 12, 30) + dt.timedelta(days=current_date),location_latitude,location_longitude,0)[1]
    # Convert a possible one-element array to a scalar
    zenith = np.asarray(zenith).item()
    forcing_scalar_zenith_angle = zenith*np.pi/180

    cgt_calc_opacity_bio()
    
    forcing_vector_opacity      = forcing_vector_opacity_bio 
    for k in range(kmax):
        forcing_vector_opacity[k] = forcing_vector_opacity[k] + forcing_vector_opacity_water[k]
    forcing_vector_light        = np.zeros(kmax)
    if forcing_scalar_zenith_angle*180/np.pi < 90: # daytime
      zenith_angle_under_water = np.arcsin(np.sin(forcing_scalar_zenith_angle)/1.33)# consider refraction at sea surface       
      forcing_vector_light[0]     = forcing_scalar_light_at_top
      for k in range(kmax):
        light_path_length = cellheights[k]/np.cos(zenith_angle_under_water)
        if k<kmax-1:
          forcing_vector_light[k+1] = forcing_vector_light[k]*np.exp(-forcing_vector_opacity[k]*light_path_length)
        forcing_vector_light[k]   = forcing_vector_light[k]*np.exp(-forcing_vector_opacity[k]*light_path_length*0.5)
    
    # output of physics during this time step
    output_vector_temperature   = output_vector_temperature   + forcing_vector_temperature
    output_vector_salinity      = output_vector_salinity      + forcing_vector_salinity
    output_vector_opacity       = output_vector_opacity       + forcing_vector_opacity
    output_vector_light         = output_vector_light         + forcing_vector_light
    output_vector_diffusivity   = output_vector_diffusivity   + forcing_vector_diffusivity
    output_scalar_light_at_top  = output_scalar_light_at_top  + forcing_scalar_light_at_top
    output_scalar_zenith_angle  = output_scalar_zenith_angle  + forcing_scalar_zenith_angle
    output_scalar_bottom_stress = output_scalar_bottom_stress + forcing_scalar_bottom_stress
    output_count=output_count+1
    
    # Calculate the thermocline strength dT/dZ for use in sinking speed calculation
    dTdZ     = np.abs(np.divide(np.diff(forcing_vector_temperature),np.diff(depths)))
    sink_fac = np.square(1 - np.divide(dTdZ,(dTdZ+K_sink)))
    sink_fac = np.append(sink_fac,sink_fac[-1])
    
    # do the biology including vertical migration / particle sinking
    cgt_bio_timestep()
    
    # do the vertical mixing
    cgt_mixing_timestep()
    
    # check if output needs to be saved in final array
    if current_date*(1.0+1.0e-10) >= current_output_date + output_interval:
        # do the output of physics
        output_temperature[current_output_index,:] = output_vector_temperature /output_count
        output_salinity[current_output_index,:]    = output_vector_salinity    /output_count
        output_opacity[current_output_index,:]     = output_vector_opacity     /output_count
        output_light[current_output_index,:]       = output_vector_light       /output_count            
        output_diffusivity[current_output_index,:] = output_vector_diffusivity /output_count            
        output_light_at_top[current_output_index]  = output_scalar_light_at_top   /output_count
        output_bottom_stress[current_output_index] = output_scalar_bottom_stress  /output_count
        output_zenith_angle[current_output_index]  = output_scalar_zenith_angle   /output_count
        # reset temporary physics output values
        output_vector_temperature   = np.zeros(kmax)
        output_vector_salinity      = np.zeros(kmax)
        output_vector_opacity       = np.zeros(kmax)
        output_vector_light         = np.zeros(kmax)
        output_vector_diffusivity   = np.zeros(kmax)
        output_scalar_light_at_top  = 0.0
        output_scalar_zenith_angle  = 0.0
        output_scalar_bottom_stress = 0.0
        #do the output of biology
        exec(open('cgt_output_final.py').read(),globals())
        #reset output indexes
        output_count  = 0
        current_output_index = current_output_index + 1
        current_output_date=current_output_date+output_interval
    
    # update the current date/time
    current_date = current_date + timestep

# Write a limited number of variables to netcdf

# Time axis
time  = pd.date_range("2020-01-01", periods=365)
# Depth axis
depth = depths

print('Output files:')

# Dissolved oxygen (mmol m⁻³)
output_t_o2 = output_t_o2*1e6
da = xr.DataArray(data=output_t_o2,dims=["time","depth"],coords=dict(time=time,depth=depth),attrs=dict(units="mmol m⁻³",),)
da.to_netcdf('{}_o2.nc'.format(run_id))
print('{}_o2.nc'.format(run_id))

# Phosphate (mmol m⁻³)
output_t_po4 = output_t_po4*1e6
da = xr.DataArray(data=output_t_po4,dims=["time","depth"],coords=dict(time=time,depth=depth),attrs=dict(units="mmol m⁻³",),)
da.to_netcdf('{}_po4.nc'.format(run_id))
print('{}_po4.nc'.format(run_id))

# DOP (mmol m⁻³)
output_t_po4 = output_t_po4*1e6
da = xr.DataArray(data=output_t_dop,dims=["time","depth"],coords=dict(time=time,depth=depth),attrs=dict(units="mmol m⁻³",),)
da.to_netcdf('{}_dop.nc'.format(run_id))
print('{}_dop.nc'.format(run_id))

# Nitrate (mmol m⁻³)
output_t_no3 = output_t_no3*1e6
da = xr.DataArray(data=output_t_no3,dims=["time","depth"],coords=dict(time=time,depth=depth),attrs=dict(units="mmol m⁻³",),)
da.to_netcdf('{}_no3.nc'.format(run_id))
print('{}_no3.nc'.format(run_id))

# Ammonium (mmol m⁻³)
output_t_nh4 = output_t_nh4*1e6
da = xr.DataArray(data=output_t_nh4,dims=["time","depth"],coords=dict(time=time,depth=depth),attrs=dict(units="mmol m⁻³",),)
da.to_netcdf('{}_nh4.nc'.format(run_id))
print('{}_nh4.nc'.format(run_id))

# Large phytoplankton (mol kg⁻¹)
output_t_lpp = output_t_lpp
da = xr.DataArray(data=output_t_lpp,dims=["time","depth"],coords=dict(time=time,depth=depth),attrs=dict(units="mol kg⁻¹",),)
da.to_netcdf('{}_lpp.nc'.format(run_id))
print('{}_lpp.nc'.format(run_id))

# Small phytoplankton (mol kg⁻¹)
output_t_spp = output_t_spp
da = xr.DataArray(data=output_t_spp,dims=["time","depth"],coords=dict(time=time,depth=depth),attrs=dict(units="mol kg⁻¹",),)
da.to_netcdf('{}_spp.nc'.format(run_id))
print('{}_spp.nc'.format(run_id))

# Cyanobacteria (mol kg⁻¹)
output_t_cya = output_t_cya
da = xr.DataArray(data=output_t_cya,dims=["time","depth"],coords=dict(time=time,depth=depth),attrs=dict(units="mol kg⁻¹",),)
da.to_netcdf('{}_cya.nc'.format(run_id))
print('{}_cya.nc'.format(run_id))

# Zooplankton (mol kg⁻¹)
output_t_zoo = output_t_zoo
da = xr.DataArray(data=output_t_zoo,dims=["time","depth"],coords=dict(time=time,depth=depth),attrs=dict(units="mol kg⁻¹",),)
da.to_netcdf('{}_zoo.nc'.format(run_id))
print('{}_zoo.nc'.format(run_id))

# Chlorophyll-a (mg m⁻³)
output_t_chl = 2e6*(output_t_spp + output_t_lpp + output_t_cya)
da = xr.DataArray(data=output_t_chl,dims=["time","depth"],coords=dict(time=time,depth=depth),attrs=dict(units="mg m⁻³",),)
print('{}_chl.nc'.format(run_id))
da.to_netcdf('{}_chl.nc'.format(run_id))

# pCO2
da = xr.DataArray(data=output_pco2,dims=["time"],coords=dict(time=time),attrs=dict(units="",),)
print('{}_pco2.nc'.format(run_id))
da.to_netcdf('{}_pco2.nc'.format(run_id))

# detritus
output_t_det = output_t_det*1e6
da = xr.DataArray(data=output_t_det,dims=["time","depth"],coords=dict(time=time,depth=depth),attrs=dict(units="mmol m⁻³",),)
da.to_netcdf('{}_det.nc'.format(run_id))
print('{}_det.nc'.format(run_id))

# DIC
output_t_dic = output_t_dic*1e6
da = xr.DataArray(data=output_t_dic,dims=["time","depth"],coords=dict(time=time,depth=depth),attrs=dict(units="mmol m⁻³",),)
da.to_netcdf('{}_dic.nc'.format(run_id))
print('{}_dic.nc'.format(run_id))

