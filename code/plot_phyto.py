import xarray as xr
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

year = 2020

colors = ['k','r','b','g']
#run_id =                                                                                   ['ctrl','aranda']#, names of pika-ergom iterations     
run_id = ['ctrl','IU7']
dpt    =                                                                                       4.5  # depth
units  =                                                                                'microgram / L' # units

plt.figure()

# flow cytometry data
infile = ''
ds = xr.open_dataset('{}/IFCB_flow_{}.nc'.format(infile,year))
print(ds)
flow_chl = ds['Filamentous.cyanobacteria'].values
flow_times = ds.time.values
plt.bar(flow_times,flow_chl,width=0.1,label='IFCB',color='grey',alpha=0.5)

i = -1
for name in run_id:
    i = i +1
    # read in an iteration of pika-ERGOM, and find the closest depth to that requested
    
    # Large phytoplankton (diatoms)
    ds         = xr.open_dataarray('{}_lpp.nc'.format(name)).sel(depth=dpt,method='nearest')
    pika       = np.squeeze(ds.values)
    # note actual depth from file
    real_depth = ds.depth.values
    # read time axis
    pika_time  = ds.time.values
    # plot iteration as time series
    plt.plot(pika_time,12*6.625e6*pika,label='pika-ergom_{}'.format(name),color=colors[i])

    # Small phytoplankton (dinoflagellates)
    ds         = xr.open_dataarray('{}_spp.nc'.format(name)).sel(depth=dpt,method='nearest')
    pika       = np.squeeze(ds.values)
    # note actual depth from file
    real_depth = ds.depth.values
    # read time axis
    pika_time  = ds.time.values
    # plot iteration as time series
    plt.plot(pika_time,12*6.625e6*pika,color=colors[i],linestyle='--')

    # Small phytoplankton (dinoflagellates)
    ds         = xr.open_dataarray('{}_cya.nc'.format(name)).sel(depth=dpt,method='nearest')
    pika       = np.squeeze(ds.values)
    # note actual depth from file
    real_depth = ds.depth.values
    # read time axis
    pika_time  = ds.time.values
    # plot iteration as time series
    plt.plot(pika_time,12*6.625e6*pika,color=colors[i],linestyle=':')

plt.ylabel('{}'.format(units))
plt.title('Depth = {0:.1f}m'.format(real_depth))
plt.grid()
plt.legend()
plt.savefig('phyto_{}.png'.format(dpt))
