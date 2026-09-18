import xarray as xr
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

colorbrewer = [(166/255, 97/255, 26/255),
               (223/255,194/255,125/255),
               (128/255,205/255,193/255),
               (  1/255,133/255,113/255)]

run_id =                                                                                   ['ctrl']#, names of pika-ergom iterations     
dpt    =                                                                                        0  # depth
units  =                                                                                'microgram / L' # units
var    =                                                                                     'chl' # variable
                                                                                             #^^   !!! Check that variable names match !!!
year   = 2020

ds    = xr.open_dataset('init/cmems_station_Utö_bgc_{}.nc'.format(year)).sel(depth=dpt,method='nearest').chl  # variable
cmems = np.squeeze(ds.values)
times = ds.time.values

plt.figure(figsize=(20,10))
i=-1
for name in run_id:
    i=i+1
    # read in an iteration of pika-ERGOM, and find the closest depth to that requested
    ds         = xr.open_dataarray('{}_{}.nc'.format(name,var)).sel(depth=dpt,method='nearest')
    pika       = np.squeeze(ds.values)
    # note actual depth from file
    real_depth = ds.depth.values
    # read time axis
    pika_time  = ds.time.values
    # plot iteration as time series
    plt.plot(pika_time,pika,label='pika-ergom_{}'.format(name),linewidth=5,color=colorbrewer[i])

# flow cytometry data
#infile = ''
#ds = xr.open_dataset('{}/IFCB_flow_{}.nc'.format(infile,year))
print(ds)
#flow_chl = ds.Chla_new_calc.values
#flow_times = ds.time.values
#plt.plot(flow_times,flow_chl,label='flow cytometry')

# plot reanalysis as reference
plt.plot(times,cmems,label='BALMFC reanalysis',linewidth=5,linestyle='--',color='k')
plt.yticks(fontsize=20)
plt.ylabel('{}, {}'.format(var,units),fontsize=30)
plt.title('Depth = {0:.1f}m'.format(real_depth),fontsize=30)
plt.xlim(times[0],times[-1])
times = np.unique(times.astype('datetime64[M]'))
print(times)
plt.xticks(times,times.astype('datetime64[M]'),fontsize=15)
plt.grid()
plt.legend(fontsize=20)
plt.savefig('comp_{}_{}.png'.format(var,dpt))
