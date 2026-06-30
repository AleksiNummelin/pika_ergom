def cgt_calc_opacity_bio():
    global forcing_vector_opacity_bio
    #-----------------------------------------------------------------
    # fill the vector opacity_bio with the opacity caused by POM [1/m]
    #-----------------------------------------------------------------
    forcing_vector_opacity_bio = np.zeros(kmax)
    
    # water column tracers
    # calculate opacity contribution [1/m] as product of
    # opacity [m2/mol] * concentration [mol/kg] * water density [kg/m3]
    for k in range(kmax):
        forcing_vector_opacity_bio[k] = forcing_vector_opacity_bio[k] + \
        gamma1 * tracer_vector_t_spp          [k] * density_water + \
        gamma1 * tracer_vector_t_lip          [k] * density_water + \
        gamma3 * tracer_vector_t_don          [k] * density_water + \
        gamma1 * tracer_vector_t_cya          [k] * density_water + \
        gamma2 * tracer_vector_t_det          [k] * density_water + \
        gamma1 * tracer_vector_t_lpp          [k] * density_water + \
        0.0
    
    # surface tracers (only in uppermost cell)
    # calculate opacity contribution [1/m] as product of
    # opacity [m2/mol] * concentration [mol/m2] / cell height [m]
    forcing_vector_opacity_bio[0] = forcing_vector_opacity_bio[0] + \
    0.0
