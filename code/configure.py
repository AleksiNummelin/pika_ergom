def configure():
    global start_date    
    start_date         = (dt.date(1964,1,1) - dt.date(1899,12,30)).days  # start date
    global end_date
    end_date           = (dt.date(1965,1,1) - dt.date(1899,12,30)).days  # final date  
    global repeated_runs
    repeated_runs      = 1                    # how often the same forcing period is repeated
    global timestep
    timestep           = 1.0/24               # timestep [days]
    global output_interval
    output_interval    = 24.0/24              # output interval [days]
    global location_longitude
    location_longitude = 20.0                 # longitude [deg], for zenith angle calculation
    global location_latitude
    location_latitude  = 57.33                # latitude  [deg], for zenith angle calculation
    global location_altitude
    location_altitude  = 0.0                  # altitude [m], for zenith angle calculation
    global density_water
    density_water      = 1035.0               # Density of water [kg/m3] to convert between mol/kg and mol/m3
    global num_vmove_steps
    num_vmove_steps    = 1                    # if >1, this splits the vertical movement timestep (keep CFL criterion valid if tracers move very fast)
    global num_vdiff_steps
    num_vdiff_steps    = 10                   # if >1, this splits the vertical mixing (keep CFL criterion valid if tracers move very fast)
    global min_diffusivity
    min_diffusivity    = 1e-4                 # minimum vertical turbulent diffusivity [m2/s]
    global max_diffusivity
    max_diffusivity    = 1                    # maximum vertical turbulent diffusivity [m2/s]