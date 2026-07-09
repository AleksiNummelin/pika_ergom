import xarray as xr
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

run_id =                                                                                   ['ctrl']#, names of pika-ergom iterations     
                                                                                           # 'slow-sink']
dpt    =                                                                                    20  # depth
units  =                                                                                  'mmol m⁻³' # units
var    =                                                                                     'nh4' # variable
                                                                                             #^^
ds    = xr.open_dataset('init/cmems_station_Utö_bgc_2020.nc').sel(depth=dpt,method='nearest').nh4 # variable
cmems = np.squeeze(ds.values)

plt.figure()

for name in run_id:
    ds         = xr.open_dataarray('{}_{}.nc'.format(name,var)).sel(depth=dpt,method='nearest')
    pika       = np.squeeze(ds.values)
    real_depth = ds.depth.values
    plt.plot(pika,label='pika-ergom_{}'.format(name))

plt.plot(cmems,label='cmems-reanalysis')
plt.ylabel('{}, {}'.format(var,units))
plt.title('Depth = {0:.1f}m'.format(real_depth))
plt.legend()
plt.show()
