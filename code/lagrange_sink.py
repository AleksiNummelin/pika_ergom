# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 11:04:42 2022
Substantial modifications Tue 12 November 2022

@author: agt_9
"""

# script to illustrate interplay between photo-adaptation and mixing timescales
# based on model of Kida & Ito (2017) and first published using MATLAB

# started 16/08/2022

import random
from random import choices
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import datetime
from datetime import date, timedelta

exec(open('configure_lagrange_sink.py').read(),globals())

# -------------- #

configure_lagrange_sink()

# Run model

def lagrange_sink(model_name,input_date,Kz,sink_fac,mld,bathy,model_dz,model_depths,input_temperature,input_distribution,sinking_speed):
    print('Mixed layer depth: {}'.format(mld))
    input_distribution = np.squeeze(input_distribution[0:np.size(model_depths)])/np.nansum(input_distribution[0:np.size(model_depths)])
    initial_index = np.random.choice(np.size(model_depths), npart, p=input_distribution)
    for i in range (0,npart):
        # initialise depth, using input distribution
        level  = initial_index[i]
        z[i,0] = model_depths[level]
        # loop over number of timesteps
        remin = 'false'
        for t in range (1,niter):
            if remin == 'false':
                # extract diffusivity at this depth
                index = np.argmin(abs(z[i,t-1]-model_depths))
                if (z[i,t-1] < mld):
                    mld_index = np.size(np.nonzero(Kz))
                    Kz_local  = np.nanmedian(Kz[0:mld_index])
                else:
                    Kz_local = 0
                # diffuse to new depth, using normally distributed random number
                delta_z = np.random.normal(0,np.sqrt(2*Kz_local*dt),1)[0]
                delta_z = np.nanmax([-mld/2,delta_z])
                delta_z = np.nanmin([ mld/2,delta_z])
                z[i,t] = z[i,t-1] + delta_z 
                # reflective boundary condition at sea surface
                if z[i,t] < 0:
                    z[i,t] = - z[i,t]
                # reflective boundary to prevent diffusion out of the mixed layer
                elif (z[i,t-1] < mld and z[i,t] > mld):
                    z[i,t] = 2*mld - z[i,t]
                else:
                    z[i,t] = z[i,t]
                # apply sinking rate 
                z[i,t] = z[i,t] - sinking_speed*sink_fac[index]*(dt/(3600*24))
                # sedimentation
                if z[i,t] > bathy:
                    z[i,t] = bathy
                # remineralize
                remin_rand = random.uniform(0,1)
                if (remin_rand<(remin_rate/niter)):
                    remin_depth[i] = z[i,t]
                    remin_time[i]  = t/60
                    remin = 'true'        
    
   # plt.figure()
   # plt.scatter(remin_time,-remin_depth)
   # plt.show()

   # plt.figure()
   # plt.hist(remin_depth,bins=np.concatenate((0,np.cumsum(model_dz)),axis=None),density='true')
   # plt.show()

    da = xr.DataArray(data=z,dims=["particle","time"],coords=dict(particle=np.linspace(1,npart,npart),time=np.linspace(1,niter,niter)))
    print('particle_traj.nc')
    da.to_netcdf('particle_traj_{}_{}.nc'.format(model_name,date(1899,12,30)+timedelta(days=int(input_date))))

    fig, ax1 = plt.subplots()
    ax1.plot(model_depths,np.divide(input_distribution,model_dz),color='g',label='Initial distribution')
    #plt.plot(model_depths,input_temperature[0:np.size(model_depths)],label='Temperature')
    ax1.hist(z[:,0] ,color='g',alpha=0.5,bins=np.concatenate((0,np.cumsum(model_dz)),axis=None),density='true')
    ax1.hist(z[:,-1],color='c',alpha=0.5,bins=np.concatenate((0,np.cumsum(model_dz)),axis=None),density='true')
    ax1.set_xlabel('Depth (m)')
    ax1.set_ylabel('Number of particles',color='g')
    ax1.legend(loc='upper right')
    #plt.plot([mld,mld],[0,np.nanmax(input_distribution)],linestyle='--')
    ax2 = ax1.twinx() 
    ax2.plot(model_depths,input_temperature[0:np.size(model_depths)],color='r',label='Temperature')
    ax2.set_ylabel('deg. C',color='r')
    ax2.legend(loc='center right')
    plt.title('{} Released {}'.format(model_name,date(1899,12,30)+timedelta(days=int(input_date))))
    plt.savefig('{}_{}.png'.format(model_name,date(1899,12,30)+timedelta(days=int(input_date))))

    return z 

