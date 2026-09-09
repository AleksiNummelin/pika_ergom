import xarray as xr
import numpy as np

def configure_lagrange_sink():

    global npart                      # Total number of particles per release
    npart             = 10000
    global dt                         # Timestep for Lagrangian model (s)
    dt                = 600
    global niter                      # Number of iterations in Lagrangian model
    niter             = 144
    global remin_rate                 # Remineralization/decay rate (d⁻¹)
    remin_rate        = 0.0
    global z                          # Initialise array for Lagrangian trajectories
    z                 = np.zeros((npart,niter))
    global remin_depth                # Initialise array for remineralization depths
    remin_depth = np.zeros((npart)) + np.nan
    global remin_time                 # Initialise array for remineralisation times
    remin_time  = np.zeros((npart)) + np.nan

