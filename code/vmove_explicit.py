def vmove_explicit( move, old_field, numerator, denominator, dzt, dt ):
#VMOVE_EXPLICIT apply vertical movement to particulate tracers
# move        = vector(0:kmax) of velocity [m/s]
# old_field   = vector(0:kmax) of initial concentration [mol/kg]
# numerator   = vector(0:kmax): if only a part of the tracer shall move, the numerator of the moving fraction
# denominator = vector(0:kmax): if only a part of the tracer shall move, the denominator of the moving fraction
# dzt         = vector(0:kmax) of cell heights [m]
# dt          = timestep [s]
# field       = output vector(1:kmax) of final concentration [kg/m3]

    kmt   = len(dzt)              # number of vertical levels
    field = old_field                   # output vector
    
    ft1  = 0.0                          # upward tracer flux through the upper boundary of the cell [mol*m/kg/s]
    for k in range(kmt-1):
        kp1 = k+1
        velocity = 0.5*move[k]
        wpos     = velocity + abs(velocity)                   # velocity if upward, else 0.0   [m/s]
        wneg     = velocity - abs(velocity)                   # velocity if downward, else 0.0 [m/s]
        if numerator[k] == denominator[k]:
           ft2 = (wneg*max(field[k],0.0)+wpos*max(field[kp1],0.0) )   
                                                               # upward transport through lower boundary of the t cell [mol*m/kg/s]
        else:
           ft2 = (wneg*max(field[k],0.0)*max(numerator[k],0.0)/max(denominator[k],1e-20) 
                 +wpos*max(field[kp1],0.0)*max(numerator[kp1],0.0)/max(denominator[kp1],1e-20) )  
                                                               # upward transport through lower boundary of the t cell [mol*m/kg/s]
        field[k] = field[k] - dt*(ft1-ft2)/dzt[k]              # change in the t-cell due to transports through lower and upper boundary [mol/kg/s]
        ft1 = ft2
    k = kmt-1
    field[k] = field[k] - dt*ft1/dzt[k]
    return(field)

