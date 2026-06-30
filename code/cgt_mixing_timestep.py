def cgt_mixing_timestep():
    global tracer_vector_t_n2           
    global tracer_vector_t_o2           
    global tracer_vector_t_dic          
    global tracer_vector_t_nh4          
    global tracer_vector_t_no3          
    global tracer_vector_t_po4          
    global tracer_vector_t_spp          
    global tracer_vector_t_zoo          
    global tracer_vector_t_h2s          
    global tracer_vector_t_sul          
    global tracer_vector_t_alk          
    global tracer_vector_t_lip          
    global tracer_vector_t_doc          
    global tracer_vector_t_dop          
    global tracer_vector_t_don          
    global tracer_vector_t_cdom         
    global tracer_vector_t_cya          
    global tracer_vector_t_det          
    global tracer_vector_t_poc          
    global tracer_vector_t_pocp         
    global tracer_vector_t_pocn         
    global tracer_vector_t_lpp          
    global tracer_vector_t_ipw          
    global forcing_vector_diffusivity
    # vertical diffusion of all tracers
    forcing_vector_diffusivity = np.fmax(forcing_vector_diffusivity, min_diffusivity)
    forcing_vector_diffusivity = np.fmin(forcing_vector_diffusivity, max_diffusivity)
    for m in range(num_vdiff_steps):
      # second, diffuse the tracers (including marked tracers) themselves
        tracer_vector_t_n2            = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_n2           , 
                               tracer_vector_t_n2           , tracer_vector_t_n2           , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_o2            = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_o2           , 
                               tracer_vector_t_o2           , tracer_vector_t_o2           , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_dic           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_dic          , 
                               tracer_vector_t_dic          , tracer_vector_t_dic          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_nh4           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_nh4          , 
                               tracer_vector_t_nh4          , tracer_vector_t_nh4          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_no3           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_no3          , 
                               tracer_vector_t_no3          , tracer_vector_t_no3          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_po4           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_po4          , 
                               tracer_vector_t_po4          , tracer_vector_t_po4          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_spp           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_spp          , 
                               tracer_vector_t_spp          , tracer_vector_t_spp          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_zoo           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_zoo          , 
                               tracer_vector_t_zoo          , tracer_vector_t_zoo          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_h2s           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_h2s          , 
                               tracer_vector_t_h2s          , tracer_vector_t_h2s          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_sul           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_sul          , 
                               tracer_vector_t_sul          , tracer_vector_t_sul          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_alk           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_alk          , 
                               tracer_vector_t_alk          , tracer_vector_t_alk          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_lip           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_lip          , 
                               tracer_vector_t_lip          , tracer_vector_t_lip          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_doc           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_doc          , 
                               tracer_vector_t_doc          , tracer_vector_t_doc          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_dop           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_dop          , 
                               tracer_vector_t_dop          , tracer_vector_t_dop          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_don           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_don          , 
                               tracer_vector_t_don          , tracer_vector_t_don          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_cdom          = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_cdom         , 
                               tracer_vector_t_cdom         , tracer_vector_t_cdom         , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_cya           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_cya          , 
                               tracer_vector_t_cya          , tracer_vector_t_cya          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_det           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_det          , 
                               tracer_vector_t_det          , tracer_vector_t_det          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_poc           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_poc          , 
                               tracer_vector_t_poc          , tracer_vector_t_poc          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_pocp          = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_pocp         , 
                               tracer_vector_t_pocp         , tracer_vector_t_pocp         , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_pocn          = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_pocn         , 
                               tracer_vector_t_pocn         , tracer_vector_t_pocn         , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_lpp           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_lpp          , 
                               tracer_vector_t_lpp          , tracer_vector_t_lpp          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
        tracer_vector_t_ipw           = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_t_ipw          , 
                               tracer_vector_t_ipw          , tracer_vector_t_ipw          , 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
