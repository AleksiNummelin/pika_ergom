def cgt_init_tracers():
    #--------------------------------
    # load initial values for tracers
    #--------------------------------

    ###---AGT

    # read in some initial conditions from reanalysis:

    import xarray as xr
    ds = xr.open_dataset(bgc_input_file)
    print(ds)

    global tracer_vector_t_o2
    tracer_vector_t_o2            = ds.o2.isel(time=0).values
    tracer_vector_t_o2            = np.squeeze(tracer_vector_t_o2)*1e-6

    global tracer_vector_t_no3
    tracer_vector_t_no3            = ds.no3.isel(time=0).values
    tracer_vector_t_no3            = np.squeeze(tracer_vector_t_no3)*1e-6

    global tracer_vector_t_po4
    tracer_vector_t_po4            = ds.po4.isel(time=0).values
    tracer_vector_t_po4            = np.squeeze(tracer_vector_t_po4)*1e-6

    global tracer_vector_t_nh4
    tracer_vector_t_nh4            = ds.nh4.isel(time=0).values
    tracer_vector_t_nh4            = np.squeeze(tracer_vector_t_nh4)*1e-6

    # some need to be loaded from files
    global tracer_vector_t_n2           
    tracer_vector_t_n2            = np.loadtxt('init/t_n2.txt')

    global tracer_vector_t_dic          
    tracer_vector_t_dic           = np.loadtxt('init/t_dic.txt')

    global tracer_vector_t_h2s          
    tracer_vector_t_h2s           = np.loadtxt('init/t_h2s.txt')

    global tracer_vector_t_alk          
    tracer_vector_t_alk           = np.loadtxt('init/t_alk.txt')

    global tracer_vector_t_det          
    tracer_vector_t_det           = np.loadtxt('init/t_det.txt')

    global tracer_vector_t_ipw          
    tracer_vector_t_ipw           = np.loadtxt('init/t_ipw.txt')

    global tracer_scalar_t_sed          
    tracer_scalar_t_sed           = float(np.loadtxt('init/t_sed.txt'))

    global tracer_scalar_t_ips          
    tracer_scalar_t_ips           = float(np.loadtxt('init/t_ips.txt'))

    global tracer_scalar_t_sed_poc      
    tracer_scalar_t_sed_poc       = float(np.loadtxt('init/t_sed_poc.txt'))

    global tracer_scalar_t_sed_pocn     
    tracer_scalar_t_sed_pocn      = float(np.loadtxt('init/t_sed_pocn.txt'))

    global tracer_scalar_t_sed_pocp     
    tracer_scalar_t_sed_pocp      = float(np.loadtxt('init/t_sed_pocp.txt'))


    # others are initialized as constant
    global tracer_vector_t_lpp 
    tracer_vector_t_lpp             = np.full(kmax,lpp0)
    global tracer_vector_t_spp
    tracer_vector_t_spp             = np.full(kmax,spp0)
    global tracer_vector_t_cya
    tracer_vector_t_cya             = np.full(kmax,cya0)
    global tracer_vector_t_lip
    tracer_vector_t_lip             = np.full(kmax,lip0)
    global tracer_vector_t_zoo
    tracer_vector_t_zoo             = np.full(kmax,zoo0)

    global tracer_vector_t_sul          
    tracer_vector_t_sul           = np.full(kmax,0.0)
    global tracer_vector_t_doc          
    tracer_vector_t_doc           = np.full(kmax,0.0)
    global tracer_vector_t_dop          
    tracer_vector_t_dop           = np.full(kmax,0.0)
    global tracer_vector_t_don          
    tracer_vector_t_don           = np.full(kmax,0.0)
    global tracer_vector_t_cdom         
    tracer_vector_t_cdom          = np.full(kmax,0.0)
    global tracer_vector_t_poc          
    tracer_vector_t_poc           = np.full(kmax,0.0)
    global tracer_vector_t_pocp         
    tracer_vector_t_pocp          = np.full(kmax,0.0)
    global tracer_vector_t_pocn         
    tracer_vector_t_pocn          = np.full(kmax,0.0)

    # some tracers have vertical movement
    global vertical_speed_of_t_cya          
    vertical_speed_of_t_cya           = np.zeros(kmax)
    global vertical_diffusivity_of_t_cya          
    vertical_diffusivity_of_t_cya           = np.zeros(kmax)
    global vertical_speed_of_t_det          
    vertical_speed_of_t_det           = np.zeros(kmax)
    global vertical_diffusivity_of_t_det          
    vertical_diffusivity_of_t_det           = np.zeros(kmax)
    global vertical_speed_of_t_poc          
    vertical_speed_of_t_poc           = np.zeros(kmax)
    global vertical_diffusivity_of_t_poc          
    vertical_diffusivity_of_t_poc           = np.zeros(kmax)
    global vertical_speed_of_t_pocp         
    vertical_speed_of_t_pocp          = np.zeros(kmax)
    global vertical_diffusivity_of_t_pocp         
    vertical_diffusivity_of_t_pocp          = np.zeros(kmax)
    global vertical_speed_of_t_pocn         
    vertical_speed_of_t_pocn          = np.zeros(kmax)
    global vertical_diffusivity_of_t_pocn         
    vertical_diffusivity_of_t_pocn          = np.zeros(kmax)
    global vertical_speed_of_t_lpp          
    vertical_speed_of_t_lpp           = np.zeros(kmax)
    global vertical_diffusivity_of_t_lpp          
    vertical_diffusivity_of_t_lpp           = np.zeros(kmax)
    global vertical_speed_of_t_ipw          
    vertical_speed_of_t_ipw           = np.zeros(kmax)
    global vertical_diffusivity_of_t_ipw          
    vertical_diffusivity_of_t_ipw           = np.zeros(kmax)

    # auxiliaries which communicate data from the last time step are set to 0
    global auxiliary_scalar_h3o            
    auxiliary_scalar_h3o             = 0.0;
