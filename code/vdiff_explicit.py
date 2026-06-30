def vdiff_explicit( diff, old_field, numerator, denominator, dzt, dt ):
    import numpy as np
#VDIFF_EXPLICIT apply vertical diffusivity to particulate tracers
# diff        = vector(0:kmax) of diffusivity [m2/s]
# old_field   = vector(0:kmax) of initial concentration [mol/kg]
# numerator   = vector(0:kmax): if only a part of the tracer shall move, the numerator of the moving fraction
# denominator = vector(0:kmax): if only a part of the tracer shall move, the denominator of the moving fraction
# dzt         = vector(0:kmax) of cell heights [m]
# dt          = timestep [s]
# field       = output vector(0:kmax) of final concentration [kg/m3]

    kmt   = len(old_field)
    field = np.fmax(old_field,0.0)
    diffusivity = np.multiply(np.add(diff[0:(kmt-1)],diff[1:kmt]),0.5)
    distance = np.multiply(np.add(dzt[0:(kmt-1)],dzt[1:kmt]),0.5)
    speed=np.divide(diffusivity,distance) # speed of exchange [m/s]
    mixed_height=np.multiply(speed,dt)      # height of mixed water column which would be mixed if the gradient would remain the same
    actual_mixed_height=distance*0.25*(1-np.exp(-4*(0.25*mixed_height/distance)))
    actual_speed=actual_mixed_height/dt
    
    if (np.sum(np.abs(numerator-denominator))==0):
      # calculate upward transport through lower boundary
      difference = field[0:(kmt-1)]-field[1:kmt]
    else:
      difference = (field[0:(kmt-1)]*np.fmax(numerator[0:(kmt-1)],0.0)/np.fmax(denominator[0:(kmt-1)],1e-20)-
                    field[1:kmt]    *np.fmax(numerator[1:kmt],0.0)    /np.fmax(denominator[1:kmt],1e-20))
    transport = -difference*actual_speed  # upward transport through lower boundary of the cell [mol*m/kg/s]
    transport_longer = np.zeros(kmt+1)
    transport_longer[1:kmt] = transport
    #transport = np.append(np.zeros(1),np.append(transport,np.zeros(1)))
    #transport = np.array([0]+transport.tolist()+[0])          # now it's through upper boundary
    transport_diff = transport_longer[1:(kmt+1)]-transport_longer[0:kmt]
    field = old_field + transport_diff*dt/dzt
    return(field)