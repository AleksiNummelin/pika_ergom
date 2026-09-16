import xarray as xr
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

run_id =                                                                                   ['ctrl','IU7']#, names of pika-ergom iterations     
dpt    =                                                                                        0  # depth
units  =                                                                                'mmol m⁻³' # units
var    =                                                                                     'chl' # variable
                                                                                             #^^   !!! Check that variable names match !!!
year   = 2020

ds    = xr.open_dataset('init/cmems_station_Utö_bgc_{}.nc'.format(year)).sel(depth=dpt,method='nearest').chl  # variable
cmems = np.squeeze(ds.values)
times = ds.time.values

plt.figure()

for name in run_id:
    # read in an iteration of pika-ERGOM, and find the closest depth to that requested
    ds         = xr.open_dataarray('{}_{}.nc'.format(name,var)).sel(depth=dpt,method='nearest')
    pika       = np.squeeze(ds.values)
    # note actual depth from file
    real_depth = ds.depth.values
    # read time axis
    pika_time  = ds.time.values
    # plot iteration as time series
    plt.plot(pika_time,pika,label='pika-ergom_{}'.format(name))

# flow cytometry data
infile = ''
ds = xr.open_dataset('{}/IFCB_flow_{}.nc'.format(infile,year))
print(ds)
flow_chl = ds.Chla_new_calc.values
flow_times = ds.time.values
plt.plot(flow_times,flow_chl,label='flow cytometry')

# plot reanalysis as reference
plt.plot(times,cmems,label='cmems-reanalysis')
plt.ylabel('{}, {}'.format(var,units))
plt.title('Depth = {0:.1f}m'.format(real_depth))
plt.grid()
plt.legend()
plt.savefig('comp_{}_{}.png'.format(var,dpt))
