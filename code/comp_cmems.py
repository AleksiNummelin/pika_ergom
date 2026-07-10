import xarray as xr
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

run_id =                                                                                   ['ctrl']#, names of pika-ergom iterations     
dpt    =                                                                                       20  # depth
units  =                                                                                'mmol m⁻³' # units
var    =                                                                                     'nh4' # variable
                                                                                             #^^   !!! Check that variable names match !!!
ds    = xr.open_dataset('init/cmems_station_Utö_bgc_2020.nc').sel(depth=dpt,method='nearest').nh4  # variable
cmems = np.squeeze(ds.values)

plt.figure()

for name in run_id:
    # read in an iteration of pika-ERGOM, and find the closest depth to that requested
    ds         = xr.open_dataarray('{}_{}.nc'.format(name,var)).sel(depth=dpt,method='nearest')
    pika       = np.squeeze(ds.values)
    # note actual depth from file
    real_depth = ds.depth.values
    # plot iteration as time series
    plt.plot(pika,label='pika-ergom_{}'.format(name))

# plot reanalysis as reference
plt.plot(cmems,label='cmems-reanalysis')
plt.ylabel('{}, {}'.format(var,units))
plt.title('Depth = {0:.1f}m'.format(real_depth))
plt.legend()
plt.show()
