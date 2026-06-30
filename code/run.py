#----------------------------------------------
# Python 1-d model for testing ecosystem models
# hagen.radtke@io-warnemuende.de
#----------------------------------------------

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

print('initialization')

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

#load cell heights
cellheights = np.loadtxt('physics/cellheights.txt') # cell heights [m]
depths      = np.cumsum(cellheights) # bottom depths of cells [m]
kmax        = len(cellheights)             # number of vertical layers

#load physics
def load_matrix(filename):
    input_matrix = np.loadtxt(filename,usecols=range(kmax+4),comments='%')
    # convert 1-d to 2-d array if needed
    if not(isinstance(input_matrix[0],np.ndarray)):
        input_matrix = np.array([input_matrix])
    return(input_matrix)
def load_vector(filename):
    return(np.loadtxt(filename,usecols=range(5),comments='%'))

### --- AGT

import xarray as xr

#da                           = xr.open_dataarray
#forcing_matrix_temperature   = da.sel...  # select a point from the NEMO output

forcing_matrix_temperature   = load_matrix('physics/temperature.txt')  # temperature [deg_C]

### -------

forcing_matrix_salinity      = load_matrix('physics/salinity.txt')     # salinity [g/kg]
forcing_matrix_light_at_top  = load_vector('physics/light_at_top.txt') # downward flux of 
                                                                       # shortwave light at sea surface [W/m2]
forcing_matrix_bottom_stress = load_vector('physics/bottom_stress.txt')# bottom stress [N/m2]                                                              
forcing_matrix_opacity_water = load_matrix('physics/opacity_water.txt')# clear-water opacity [1/m]
forcing_matrix_diffusivity   = load_matrix('physics/diffusivity.txt')  # turbulent vertical diffusivity [m2/s]

forcing_index_temperature = 0
forcing_index_salinity = 0
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

# do the timestep
while current_date < repeated_runs*(end_date-start_date)+start_date:
    # load the physics
    forcing_vector_temperature  , forcing_index_temperature   = load_forcing.load_forcing(forcing_matrix_temperature,current_date,start_date,end_date, kmax, forcing_index_temperature)
    forcing_vector_salinity     , forcing_index_salinity      = load_forcing.load_forcing(forcing_matrix_salinity,current_date,start_date,end_date, kmax, forcing_index_salinity)
    forcing_vector_opacity_water, forcing_index_opacity_water = load_forcing.load_forcing(forcing_matrix_opacity_water,current_date,start_date,end_date, kmax, forcing_index_opacity_water)
    forcing_vector_diffusivity  , forcing_index_diffusivity   = load_forcing.load_forcing(forcing_matrix_diffusivity,current_date,start_date,end_date, kmax, forcing_index_diffusivity)
    forcing_scalar_light_at_top , forcing_index_light_at_top  = load_forcing.load_forcing(forcing_matrix_light_at_top,current_date,start_date,end_date, kmax, forcing_index_light_at_top)
    forcing_scalar_bottom_stress, forcing_index_bottom_stress = load_forcing.load_forcing(forcing_matrix_bottom_stress,current_date,start_date,end_date, kmax, forcing_index_bottom_stress)
    
    # light calculation
    zenith = sunpos(dt.datetime(1899, 12, 30) + dt.timedelta(days=current_date),location_latitude,location_longitude,0)[1]
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
    
    # do the biology including vertical migration / particle sinking
    cgt_bio_timestep()
    
    # do the vertical mixing
    cgt_mixing_timestep()
    
    # check if output needs to be saved in final array
    if current_date*(1.0+1.0e-10) >= current_output_date + output_interval:
        # display current date/time
        print(dt.date(1899,12,30)+dt.timedelta(days=current_date))
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

### --- AGT --- ###

import xarray as xr
import pandas as pd

# write a limited number of variables to netcdf

# coordinates

time  = pd.date_range("1964-01-01", periods=366)
depth = np.flip(np.linspace(0,115,116))

# variables

output_t_o2 = np.transpose(output_t_o2)
da = xr.DataArray(data=output_t_o2,dims=["depth","time"],coords=dict(depth=depth,time=time),attrs=dict(units="mol kg⁻¹",),)
da.to_netcdf('t_o2.nc')

output_t_lpp = np.transpose(output_t_lpp)
da = xr.DataArray(data=output_t_lpp,dims=["depth","time"],coords=dict(depth=depth,time=time),attrs=dict(units="mol kg⁻¹",),)
da.to_netcdf('t_lpp.nc')

output_t_spp = np.transpose(output_t_spp)
da = xr.DataArray(data=output_t_spp,dims=["depth","time"],coords=dict(depth=depth,time=time),attrs=dict(units="mol kg⁻¹",),)
da.to_netcdf('t_spp.nc')

output_t_cya = np.transpose(output_t_cya)
da = xr.DataArray(data=output_t_cya,dims=["depth","time"],coords=dict(depth=depth,time=time),attrs=dict(units="mol kg⁻¹",),)
da.to_netcdf('t_cya.nc')

