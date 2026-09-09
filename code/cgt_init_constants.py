def cgt_init_constants():
    #-----------------
    # define constants
    #-----------------
    global critical_stress # critical shear stress for sediment erosion [N/m2]
    critical_stress = 0.016    
    global cya0            # seed concentration for diazotroph cyanobacteria [mol/kg]
    cya0            = 9.0E-8   
    global din_min_lpp     # DIN half saturation constant for large-cell phytoplankton growth [mol/kg]
    din_min_lpp     = 1.0E-6   
    global din_min_spp     # DIN half saturation constant for small-cell phytoplankton growth [mol/kg]
    din_min_spp     = 1.6E-7   
    global dip_min_cya     # DIP half saturation constant for diazotroph cyanobacteria growth [mol/kg]
    dip_min_cya     = 1.0E-8   
    global din_min_lip     # DIN half saturation constant for limnic phytoplankton growth [mol/kg]
    din_min_lip     = 1.0E-6   
    global epsilon         # no division by 0
    epsilon         = 4.5E-17  
    global food_min_zoo    # Ivlev phytoplankton concentration for zooplankton grazing [mol/kg]
    food_min_zoo    = 4.108E-6 
    global gamma0          # light attentuation parameter (opacity of clear water) [1/m], DO NOT CHANGE NAME gamma0 SINCE THIS NAME WILL BE USED IN THE TEMPLATE
    gamma0          = 0.027    
    global gamma1          # light attentuation parameter (opacity of POM containing chlorophyll) [m**2/mol]
    gamma1          = 58.0     
    global gamma2          # light attentuation parameter (opacity of POM detritus) [m**2/mol]
    gamma2          = 53.2     
    global gamma3          # light attentuation parameter (opacity of DON) [m**2/mol]
    gamma3          = 12.6     
    global h2s_min_po4_liber # minimum h2s concentration for liberation of iron phosphate from the sediment [mol/kg]
    h2s_min_po4_liber = 1.0E-6   
    global ips_threshold   # threshold for increased PO4 burial [mol/m**2]
    ips_threshold   = 0.1      
    global ips_cl          # iron phosphate in sediment closure parameter [mol/m2]
    ips_cl          = 0.02025  
    global k_h2s_no3       # reaction constant h2s oxidation with no3 [kg/mol/day]
    k_h2s_no3       = 800000.0 
    global k_h2s_o2        # reaction constant h2s oxidation with o2 [kg/mol/day]
    k_h2s_o2        = 800000.0 
    global k_sul_no3       # reaction constant sul oxidation with no3 [kg/mol/day]
    k_sul_no3       = 20000.0  
    global k_sul_o2        # reaction constant sul oxidation with o2 [kg/mol/day]
    k_sul_o2        = 20000.0  
    global light_opt_cya   # optimal light for diazotroph cyanobacteria growth [W/m**2]
                           ### ~~~ pika-ERGOM ~~~ Range of values tested, impacts small.
                           ### ~~~ pika-ERGOM ~~~ Could be used as basis for ensemble.
    light_opt_cya   = 50.0     
    global light_opt_lpp   # optimal light for large-cell phytoplankton growth [W/m**2]
                           ### ~~~ pika-ERGOM ~~~ Range of values tested, impacts small.
                           ### ~~~ pika-ERGOM ~~~ Could be used as basis for ensemble.
    light_opt_lpp   = 35.0     
    global light_opt_spp   # optimal light for small-cell phytoplankton growth [W/m**2]
                           ### ~~~ pika-ERGOM ~~~ Range of values tested, impacts small.
                           ### ~~~ pika-ERGOM ~~~ Could be used as basis for ensemble.
    light_opt_spp   = 50.0     
    global light_opt_lip   # optimal light for limnic phytoplankton growth [W/m**2]
    light_opt_lip   = 30.0     
    global lip0            # seed concentration for limnic phytoplankton [mol/kg]
    lip0            = 4.5E-9   
    global lpp0            # seed concentration for large-cell phytoplankton [mol/kg]
    lpp0            = 4.5E-9   
    global no3_min_sed_denit # nitrate half-saturation concentration for denitrification in the water column [mol/kg]
    no3_min_sed_denit = 1.423E-7 
    global no3_min_det_denit # minimum no3 concentration for recycling of detritus using nitrate (denitrification)
    no3_min_det_denit = 1.0E-9   
    global o2_min_det_resp # oxygen half-saturation constant for detritus recycling [mol/kg]
    o2_min_det_resp = 1.0E-6   
    global o2_min_nit      # oxygen half-saturation constant for nitrification [mol/kg]
    o2_min_nit      = 3.75E-6  
    global o2_min_po4_retent # oxygen half-saturation concentration for retension of phosphate during sediment denitrification [mol/kg]
    o2_min_po4_retent = 0.0000375 
    global o2_min_sed_resp # oxygen half-saturation constant for recycling of sediment detritus using oxygen [mol/kg]
    o2_min_sed_resp = 0.000064952 
    global patm_co2        # atmospheric partial pressure of CO2 [Pa]
    patm_co2        = 38.0     
    global q10_det_rec     # q10 rule factor for recycling [1/K]
    q10_det_rec     = 0.15     
    global q10_doc_rec     # q10 rule factor for DOC recycling [1/K]
    q10_doc_rec     = 0.069    
    global q10_h2s         # q10 rule factor for oxidation of h2s and sul [1/K]
    q10_h2s         = 0.0693   
    global q10_nit         # q10 rule factor for nitrification [1/K]
    q10_nit         = 0.11     
    global q10_sed_rec     # q10 rule factor for detritus recycling in the sediment [1/K]
    q10_sed_rec     = 0.175    
    global r_biores        # bio-resuspension rate [1/day]
    r_biores        = 0.015    
    global r_cya_assim     # maximum rate for nutrient uptake of diazotroph cyanobacteria [1/day]
                           ### ~~~ pika-ERGOM ~~~ Increased from 0.75 d⁻¹ to 3.0 d⁻¹, to better match rapid cyanobacteria growth seen in flow cytometry from Utö
                           ### ~~~ pika-ERGOM ~~~ Kraft et al. (2025): https://doi.org/10.1016/j.hal.2025.102865
    r_cya_assim     = 3.0     
    global r_cya_resp      # respiration rate of cyanobacteria to ammonium [1/day]
    r_cya_resp      = 0.01     
    global r_det_rec       # recycling rate (detritus to ammonium) at 0°C [1/day]
    r_det_rec       = 0.003    
    global r_ips_burial    # final burial rate for PO4 [1/day]
    r_ips_burial    = 0.0018   
    global r_ips_ero       # erosion rate for iron PO4 [1/day]
    r_ips_ero       = 6.0      
    global r_ips_liber     # PO4 liberation rate under anoxic conditions [1/day]
    r_ips_liber     = 0.1      
    global r_lpp_assim     # maximum rate for nutrient uptake of large-cell phytoplankton [1/day]
                           ### ~~~ pika-ERGOM ~~~ Decreased from 1.38 d⁻¹ to 1.0 d⁻¹, to delay diatom bloom from March to April, as seen in Ferrybox data.
                           ### ~~~ pika-ERGOM ~~~ Tvärminne lab experiments suggest a plausible range of 0.6 d⁻¹ to 1.2 d⁻¹, depending on species.
                           ### ~~~ pika-ERGOM ~~~ Spilling (2007): http://urn.fi/URN:ISBN:978-952-10-3626-2 
    r_lpp_assim     = 1.0     
    global r_lpp_resp      # respiration rate of large phytoplankton to ammonium [1/day]
    r_lpp_resp      = 0.075    
    global r_lip_assim     # maximum rate for nutrient uptake of limnic phytoplankton [1/day]
    r_lip_assim     = 1.38     
    global r_lip_resp      # respiration rate of limnic phytoplankton to ammonium [1/day]
    r_lip_resp      = 0.075    
    global r_nh4_nitrif    # nitrification rate at 0°C [1/day]
    r_nh4_nitrif    = 0.05     
    global r_pp_mort       # mortality rate of phytoplankton [1/day]
    r_pp_mort       = 0.03     
    global r_cya_mort_diff # enhanced cya mortality due to strong turbulence
                           ### ~~~ pika-ERGOM ~~~ Increase mortality of cyanobacteria to 0.3 d⁻¹ based on flow cytometry from Utö
                           ### ~~~ pika-ERGOM ~~~ Kraft et al. (2025): https://doi.org/10.1016/j.hal.2025.102865

    r_cya_mort_diff = 0.27     
    global r_cya_mort_thresh # diffusivity threshold for enhanced cyano mortality
                           ### ~~~ pika-ERGOM ~~~ Apply increased mortality irrespective of diffusivity.
                           ### ~~~ pika-ERGOM ~~~ Threshold based on diffusivity makes results highly setup-dependent.
    r_cya_mort_thresh = 0.0     
    global r_sed_ero       # maximum sediment detritus erosion rate [1/day]
    r_sed_ero       = 6.0      
    global r_sed_rec       # maximum recycling rate for sedimentary detritus [1/d]
    r_sed_rec       = 0.003    
    global r_sed_poc_rec   # maximum recycling rate for sedimentary POC [1/d]
    r_sed_poc_rec   = 0.0005   
    global r_spp_assim     # maximum rate for nutrient uptake of small-cell phytoplankton [1/day]
                           ### ~~~ pika-ERGOM ~~~ Decreased from 0.4 d⁻¹ to 0.2 d⁻¹, following removal of minimum temperature threshold.
                           ### ~~~ pika-ERGOM ~~~ Tvärminne lab experiments suggest a plausible range of 0.2 d⁻¹ to 0.3 d⁻¹, depending on species.
                           ### ~~~ pika-ERGOM ~~~ Spilling (2007): http://urn.fi/URN:ISBN:978-952-10-3626-2 
    r_spp_assim     = 0.2      
    global r_spp_resp      # respiration rate of small phytoplankton to ammonium [1/day]
    r_spp_resp      = 0.0175   
    global r_zoo_graz      # maximum zooplankton grazing rate [1/day]
    r_zoo_graz      = 0.5      
    global r_zoo_mort      # mortality rate of zooplankton [1/day]
    r_zoo_mort      = 0.03     
    global r_zoo_resp      # respiration rate of zooplankton [1/day]
    r_zoo_resp      = 0.01     
    global rfr_c           # redfield ratio C/N
    rfr_c           = 6.625    
    global rfr_h           # redfield ratio H/N
    rfr_h           = 16.4375  
    global rfr_o           # redfield ratio O/N
    rfr_o           = 6.875    
    global rfr_p           # redfield ratio P/N
    rfr_p           = 0.0625   
    global rfr_cp          # redfield ratio C/P
    rfr_cp          = 106.0    
    global sali_max_cya    # upper salinity limit - diazotroph cyanobacteria [psu]
    sali_max_cya    = 8.0      
    global sali_min_cya    # lower salinity limit - diazotroph cyanobacteria [psu]
    sali_min_cya    = 4.0      
    global nit_max_cya     # limits cyano growth in DIN reach environment
    nit_max_cya     = 5.0E-7   
    global nit_switch_cya  # strengs of DIN control for cyano growth
    nit_switch_cya  = 8.0      
    global sali_max_lip    # lower salinity limit - limnic phytoplankton [psu]
    sali_max_lip    = 2.0      
    global sed_max         # maximum sediment detritus concentration that feels erosion [mol/m**2]
    sed_max         = 1.0      
    global sed_burial      # maximum sediment load before burial
    sed_burial      = 1.0      
    global spp0            # seed concentration for small-cell phytoplankton [mol/kg]
                           ### ~~~ pika-ERGOM ~~~ Simulations show that an increase by around one order of magnitude leads to a spring bloom
                           ### ~~~ pika-ERGOM ~~~ where diatoms and dinoflagellates co-exist almost equally. 
                           ### ~~~ pika-ERGOM ~~~ Potential to conduct ensemble of runs with different initial conditions.
                           ### ~~~ pika-ERGOM ~~~ Lab experiments from Tvärminne also suggest high sensitivity to initial conditions.
                           ### ~~~ pika-ERGOM ~~~ Kremp et al. (2008): 
    spp0            = 4.5E-9   
    global temp_min_cya    # lower temperature limit - diazotroph cyanobacteria [°C]
                           ### ~~~ pika-ERGOM ~~~ Increasd from 13.5 deg. C to 15.0 deg. C in order to match FICOS model
                           ### ~~~ pika-ERGOM ~~~ Lignell et al. (2025): 
    temp_min_cya    = 15.0     
    global temp_switch_cya # strengs of temperature control for cyano growth
    temp_switch_cya = 4.0      
    global temp_min_spp    # lower temperature limit - small-cell phytoplankton [°C]
                           ### ~~~ pika-ERGOM ~~~ Lower temperature limit (10 deg. C) removed to allow for growth of cold-water dinoflagellates.
                           ### ~~~ pika-ERGOM ~~~ Spilling (2007): http://urn.fi/URN:ISBN:978-952-10-3626-2
    temp_min_spp    = 0.0     
    global temp_opt_zoo    # optimal temperature for zooplankton grazing [°C]
    temp_opt_zoo    = 20.0     
    global w_co2_stf       # piston velocity for co2 surface flux [m/d]
    w_co2_stf       = 4.0      
    global w_cya           # vertical speed of diazotroph cyanobacteria [m/day]
                           ### ~~~ pika-ERGOM ~~~ Buoyancy (vertical speed +1 m/d) removed to prevent excessive cyanobacteria persistence in autumn.
                           ### ~~~ pika-ERGOM ~~~ ### ~~~ pika-ERGOM ~~~ Kraft et al. (2025): https://doi.org/10.1016/j.hal.2025.102865
    w_cya           = 0.0      
    global w_det           # vertical speed of detritus [m/day]
    w_det           = -4.5  
    global w_ipw           # vertical speed of suspended iron PO4 [m/day]
    w_ipw           = -1.0     
    global w_det_sedi      # sedimentation velocity (negative for downward) [m/day]
    w_det_sedi      = -2.25    
    global w_ipw_sedi      # sedimentation velocity for iron PO4 [m/day]
    w_ipw_sedi      = -0.5     
    global w_lpp           # vertical speed of large-cell phytoplankton [m/day]
                           ### ~~~ pika-ERGOM ~~~ Sinking speed increased from 0.5 m/d to 1.0 m/d.
    w_lpp           = -1.0     
    global w_n2_stf        # piston velocity for n2 surface flux [m/d]
    w_n2_stf        = 5.0      
    global w_o2_stf        # piston velocity for oxygen surface flux [m/d]
    w_o2_stf        = 5.0      
    global zoo0            # seed concentration for zooplankton [mol/kg]
    zoo0            = 4.5E-9   
    global zoo_cl          # zooplankton closure parameter [mol/kg]
    zoo_cl          = 9.0E-8   
    global don_fraction    # fraction of DON in respiration products
    don_fraction    = 0.0      
    global r_poc_rec       # recycling rate (poc to dic) at 0°C [1/day]
    r_poc_rec       = 0.003    
    global r_pocp_rec      # recycling rate (pocp to dic and po4) at 0°C [1/day]
    r_pocp_rec      = 0.002    
    global r_pocn_rec      # recycling rate (pocn to dic and nh4) at 0°C [1/day]
    r_pocn_rec      = 0.002    
    global w_poc           # vertical speed of poc [m/day]
    w_poc           = -0.2     
    global w_poc_sedi      # sedimentation velocity (negative for downward) [m/day]
    w_poc_sedi      = -0.1     
    global w_pocp          # vertical speed of pocp [m/day]
    w_pocp          = -0.1     
    global w_pocp_sedi     # sedimentation velocity (negative for downward) [m/day]
    w_pocp_sedi     = -0.05    
    global w_pocn          # vertical speed of pocn [m/day]
    w_pocn          = -0.1     
    global w_pocn_sedi     # sedimentation velocity (negative for downward) [m/day]
    w_pocn_sedi     = -0.05    
    global fac_doc_assim_lpp # factor modifying DOC assimilation rate of large phytoplankton LPP
    fac_doc_assim_lpp = 1.0      
    global fac_doc_assim_cya # factor modifying DOC assimilation rate of cyanobacteria
    fac_doc_assim_cya = 1.0      
    global fac_doc_assim_spp # factor modifying DOC assimilation rate of small phytoplankton SPP
    fac_doc_assim_spp = 1.0      
    global fac_doc_assim_lip # factor modifying DOC assimilation rate of limnic phytoplankton LIP
    fac_doc_assim_lip = 1.0      
    global fac_dop_assim   # factor modifying assimilation rate for POCP production
    fac_dop_assim   = 0.5      
    global fac_don_assim   # factor modifying assimilation rate for POCN production
    fac_don_assim   = 1.0      
    global fac_enh_rec     # enhance recyclig of DON,POCN/DOP,POCP in case of limiting DIN/DIP
    fac_enh_rec     = 10.0     
    global ret_po4_1       # PO4 retension in oxic sediments
    ret_po4_1       = 0.1      
    global ret_po4_2       # additional PO4 retension in oxic sediments of the Bothnian Sea
    ret_po4_2       = 0.5      
    global ret_po4_3       # additional PO4 retension in oxic sediments of the Bothnian Sea
    ret_po4_3       = 0.13     
    global frac_denit_scal # scaling frac_denit_sed
    frac_denit_scal = 1.0      
    global reduced_rec     # decrease recycling in sed under anoxia by reduce_rec
    reduced_rec     = 0.8      
    global martin_fac_poc  # [1/d], depth dependence of POC sinking speed
    martin_fac_poc  = 0.01     
    global r_doc2poc       # POC formation rate
    r_doc2poc       = 0.01     
    global r_don2pocn      # POCN formation rate
    r_don2pocn      = 0.01     
    global r_dop2pocp      # POCP formation rate
    r_dop2pocp      = 0.01     
    global r_doc_rec       # recycling rate (doc to dic) at 0°C [1/day]
    r_doc_rec       = 0.001 
    global r_don_rec       # recycling rate (don to dic and NH4) at 0°C [1/day]
    r_don_rec       = 0.001 
    global r_dop_rec       # recycling rate (dop to dic and PO4) at 0°C [1/day]
    r_dop_rec       = 0.001 
    global fac_ips_burial  # reduced burial of t_ips, mimicing resolving iron-P complexes in deeper sediment and subsequent upward PO4 flux
    fac_ips_burial  = 0.5      
    global r_cdom_decay    # decay rate of cdom
    r_cdom_decay    = 0.0035   
    global r_cdom_light    # PAR intensity controling CDOM decay
    r_cdom_light    = 40.0     
    global alk_btf_0       # artifical alkalinity bottom flux constant mol/m**2/day
    alk_btf_0       = 0.002    
    global alk_btf_0_BBfac # fraction of BS BFT Alk flux in BB
    alk_btf_0_BBfac = 0.25     
    global alk_btf_DBBfac  # Factor for alkalinity BTF below depth D2 in Bothnian Bay
    alk_btf_DBBfac  = 0.0      
    global alk_btf_Dfac    # Factor for alkalinity BTF below depth D2
    alk_btf_Dfac    = 0.3      
    global alk_btf_D1      # upper depth for alkalinity dissolution from sea bed
    alk_btf_D1      = 10.0     
    global alk_btf_D2      # below depth D2 alkalinity dissolution from sea bed is reduced by alk_btf_Dfac
    alk_btf_D2      = 75.0
