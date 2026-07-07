def theta(x):
    if x>0:
        return(1.0)
    else:
        return(0.0)

def exp(x):
    import math
    return math.exp(x)

def log(x):
    import math
    return math.log(x)

def sqrt(x):
    import math
    return math.sqrt(x)

def power(base, exponent):
    return base ** exponent

def cgt_bio_timestep(): 
    import numpy as np
    # declare which global variables we want to modify
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
    global tracer_scalar_t_sed          
    global tracer_scalar_t_ips          
    global tracer_scalar_t_sed_poc      
    global tracer_scalar_t_sed_pocn     
    global tracer_scalar_t_sed_pocp     
    global output_vector_t_n2           
    global output_vector_t_o2           
    global output_vector_t_dic          
    global output_vector_t_nh4          
    global output_vector_t_no3          
    global output_vector_t_po4          
    global output_vector_t_spp          
    global output_vector_t_zoo          
    global output_vector_t_h2s          
    global output_vector_t_sul          
    global output_vector_t_alk          
    global output_vector_t_lip          
    global output_vector_t_doc          
    global output_vector_t_dop          
    global output_vector_t_don          
    global output_vector_t_cdom         
    global output_vector_t_cya          
    global output_vector_t_det          
    global output_vector_t_poc          
    global output_vector_t_pocp         
    global output_vector_t_pocn         
    global output_vector_t_lpp          
    global output_vector_t_ipw          
    global output_scalar_t_sed          
    global output_scalar_t_ips          
    global output_scalar_t_sed_poc      
    global output_scalar_t_sed_pocn     
    global output_scalar_t_sed_pocp     
    global vertical_speed_of_t_cya          
    global vertical_diffusivity_of_t_cya          
    global vertical_speed_of_t_det          
    global vertical_diffusivity_of_t_det          
    global vertical_speed_of_t_poc          
    global vertical_diffusivity_of_t_poc          
    global vertical_speed_of_t_pocp         
    global vertical_diffusivity_of_t_pocp         
    global vertical_speed_of_t_pocn         
    global vertical_diffusivity_of_t_pocn         
    global vertical_speed_of_t_lpp          
    global vertical_diffusivity_of_t_lpp          
    global vertical_speed_of_t_ipw          
    global vertical_diffusivity_of_t_ipw          
    global output_vector_lr_assim_lpp   
    global output_vector_lr_assim_spp   
    global output_vector_lr_assim_cya   
    global output_vector_lr_assim_lpp_doc
    global output_vector_lr_assim_spp_doc
    global output_vector_lr_assim_cya_doc
    global output_vector_lr_assim_lpp_dop
    global output_vector_lr_assim_spp_dop
    global output_vector_lr_assim_lpp_don
    global output_vector_lr_assim_spp_don
    global output_vector_ref_p_sw       
    global output_vector_ref_n_sw       
    global output_vector_lr_pocp        
    global output_vector_lr_dop         
    global output_vector_lr_pocn        
    global output_vector_lr_don         
    global output_vector_w_poc_var      
    global output_vector_w_pocn_var     
    global output_vector_w_pocp_var     
    global output_scalar_k0_co2         
    global output_scalar_k1_co2         
    global output_scalar_k2_co2         
    global output_scalar_alk_boron      
    global output_scalar_alk_h2s        
    global output_scalar_alk_water      
    global output_scalar_alk_po4        
    global output_scalar_alk_co2        
    global output_scalar_alk_residual   
    global output_scalar_dalkc_dh3o     
    global output_scalar_dalkresidual_dpH
    global output_scalar_ph             
    global output_scalar_h3o            
    global output_scalar_pco2           
    global output_scalar_schmidtnumber_co2
    global output_scalar_schmidtnumber_o2
    global output_scalar_schmidtnumber_n2
    global auxiliary_scalar_h3o            
    global output_vector_p_no3_assim_lpp
    global output_vector_p_nh4_assim_lpp
    global output_vector_p_no3_assim_spp
    global output_vector_p_nh4_assim_spp
    global output_vector_p_n2_assim_cya 
    global output_vector_p_assim_lpp_doc
    global output_vector_p_assim_spp_doc
    global output_vector_p_assim_cya_doc
    global output_vector_p_assim_lpp_dop
    global output_vector_p_assim_spp_dop
    global output_vector_p_nh4_assim_lpp_don
    global output_vector_p_no3_assim_lpp_don
    global output_vector_p_nh4_assim_spp_don
    global output_vector_p_no3_assim_spp_don
    global output_vector_p_pocp_resp    
    global output_vector_p_pocn_resp    
    global output_vector_p_cya_mort_det_diff
    global output_vector_p_det_resp_nh4 
    global output_vector_p_det_denit_nh4
    global output_vector_p_det_sulf_nh4 
    global output_vector_p_h2s_oxno3_sul
    global output_vector_p_doc2pco      
    global output_vector_p_dop2pocp     
    global output_vector_p_don2pocn     
    global output_vector_p_doc_resp     
    global output_vector_p_dop_resp     
    global output_vector_p_don_resp     
    global output_scalar_p_sed_resp_nh4 
    global output_scalar_p_sed_biores_poc
    global output_scalar_p_sed_burial   
    global output_scalar_p_ips_burial   
    global output_scalar_p_poc_burial   
    global output_scalar_p_pocn_burial  
    global output_scalar_p_pocp_burial  
    global output_scalar_p_alk_btf      
  
    # calculate total element concentrations in the water column
    for k in range(kmax):
        cgt_dummyvar = 0.0
     

    # calculate total colored element concentrations at bottom

    # Water column processes

    cgt_bottomdepth = 0.0 
    for k in range(kmax):
            cgt_bottomdepth = cgt_bottomdepth + cellheights[k]
          
            #------------------------------------
            # STEP 1: prepare abiotic parameters
            #------------------------------------
            cgt_temp       = forcing_vector_temperature[k]             # potential temperature     [Celsius]
            cgt_sali       = forcing_vector_salinity[k]                # salinity                  [g/kg]
            cgt_diffusivity= forcing_vector_diffusivity[k]             # diffusivity               [m2/s]
            cgt_light      = forcing_vector_light[k]                   # light intensity           [W/m2]
            cgt_cellheight = cellheights[k]                            # cell height               [m]
            cgt_density    = density_water                             # density                   [kg/m3]
            cgt_timestep   = timestep                                  # timestep                  [days]
            cgt_longitude  = location_longitude                        # geographic longitude      [deg]
            cgt_latitude   = location_latitude                         # geographic latitude       [deg]
            if (k == kmax-1):
                cgt_current_wave_stress=forcing_scalar_bottom_stress    # bottom stress             [N/m2]
                                   
             
            #------------------------------------
            # STEP 2: load tracer values
            #------------------------------------
            t_n2            = float(tracer_vector_t_n2           [k])   # dissolved molecular nitrogen
            if (k == 0):
                above_t_n2            = float(tracer_vector_t_n2           [k]) 
            else:
               above_t_n2            = float(tracer_vector_t_n2           [k-1])
             
            t_o2            = float(tracer_vector_t_o2           [k])   # dissolved oxygen
            if (k == 0):
                above_t_o2            = float(tracer_vector_t_o2           [k]) 
            else:
               above_t_o2            = float(tracer_vector_t_o2           [k-1])
             
            t_dic           = float(tracer_vector_t_dic          [k])   # dissolved inorganic carbon, treated as carbon dioxide
            if (k == 0):
                above_t_dic           = float(tracer_vector_t_dic          [k]) 
            else:
               above_t_dic           = float(tracer_vector_t_dic          [k-1])
             
            t_nh4           = float(tracer_vector_t_nh4          [k])   # ammonium
            if (k == 0):
                above_t_nh4           = float(tracer_vector_t_nh4          [k]) 
            else:
               above_t_nh4           = float(tracer_vector_t_nh4          [k-1])
             
            t_no3           = float(tracer_vector_t_no3          [k])   # nitrate
            if (k == 0):
                above_t_no3           = float(tracer_vector_t_no3          [k]) 
            else:
               above_t_no3           = float(tracer_vector_t_no3          [k-1])
             
            t_po4           = float(tracer_vector_t_po4          [k])   # phosphate
            if (k == 0):
                above_t_po4           = float(tracer_vector_t_po4          [k]) 
            else:
               above_t_po4           = float(tracer_vector_t_po4          [k-1])
             
            t_spp           = float(tracer_vector_t_spp          [k])   # small-cell phytoplankton
            if (k == 0):
                above_t_spp           = float(tracer_vector_t_spp          [k]) 
            else:
               above_t_spp           = float(tracer_vector_t_spp          [k-1])
             
            t_zoo           = float(tracer_vector_t_zoo          [k])   # zooplankton
            if (k == 0):
                above_t_zoo           = float(tracer_vector_t_zoo          [k]) 
            else:
               above_t_zoo           = float(tracer_vector_t_zoo          [k-1])
             
            t_h2s           = float(tracer_vector_t_h2s          [k])   # hydrogen sulfide
            if (k == 0):
                above_t_h2s           = float(tracer_vector_t_h2s          [k]) 
            else:
               above_t_h2s           = float(tracer_vector_t_h2s          [k-1])
             
            t_sul           = float(tracer_vector_t_sul          [k])   # sulfur
            if (k == 0):
                above_t_sul           = float(tracer_vector_t_sul          [k]) 
            else:
               above_t_sul           = float(tracer_vector_t_sul          [k-1])
             
            t_alk           = float(tracer_vector_t_alk          [k])   # total alkalinity
            if (k == 0):
                above_t_alk           = float(tracer_vector_t_alk          [k]) 
            else:
               above_t_alk           = float(tracer_vector_t_alk          [k-1])
             
            t_lip           = float(tracer_vector_t_lip          [k])   # limnic phytoplankton
            if (k == 0):
                above_t_lip           = float(tracer_vector_t_lip          [k]) 
            else:
               above_t_lip           = float(tracer_vector_t_lip          [k-1])
             
            t_doc           = float(tracer_vector_t_doc          [k])   # dissolved organic carbon
            if (k == 0):
                above_t_doc           = float(tracer_vector_t_doc          [k]) 
            else:
               above_t_doc           = float(tracer_vector_t_doc          [k-1])
             
            t_dop           = float(tracer_vector_t_dop          [k])   # phosphorus in dissolved organic carbon in Redfield ratio
            if (k == 0):
                above_t_dop           = float(tracer_vector_t_dop          [k]) 
            else:
               above_t_dop           = float(tracer_vector_t_dop          [k-1])
             
            t_don           = float(tracer_vector_t_don          [k])   # nitrogen in dissolved organic carbon in Redfield ratio
            if (k == 0):
                above_t_don           = float(tracer_vector_t_don          [k]) 
            else:
               above_t_don           = float(tracer_vector_t_don          [k-1])
             
            t_cdom          = float(tracer_vector_t_cdom         [k])   # colored dissolved organic carbon
            if (k == 0):
                above_t_cdom          = float(tracer_vector_t_cdom         [k]) 
            else:
               above_t_cdom          = float(tracer_vector_t_cdom         [k-1])
             
            t_cya           = float(tracer_vector_t_cya          [k])   # diazotroph cyanobacteria
            if (k == 0):
                above_t_cya           = float(tracer_vector_t_cya          [k]) 
            else:
               above_t_cya           = float(tracer_vector_t_cya          [k-1])
             
            t_det           = float(tracer_vector_t_det          [k])   # detritus
            if (k == 0):
                above_t_det           = float(tracer_vector_t_det          [k]) 
            else:
               above_t_det           = float(tracer_vector_t_det          [k-1])
             
            t_poc           = float(tracer_vector_t_poc          [k])   # particulate organic carbon
            if (k == 0):
                above_t_poc           = float(tracer_vector_t_poc          [k]) 
            else:
               above_t_poc           = float(tracer_vector_t_poc          [k-1])
             
            t_pocp          = float(tracer_vector_t_pocp         [k])   # phosphorus in particulate organic carbon in Redfield ratio
            if (k == 0):
                above_t_pocp          = float(tracer_vector_t_pocp         [k]) 
            else:
               above_t_pocp          = float(tracer_vector_t_pocp         [k-1])
             
            t_pocn          = float(tracer_vector_t_pocn         [k])   # nitrogen in particulate organic carbon in Redfield ratio
            if (k == 0):
                above_t_pocn          = float(tracer_vector_t_pocn         [k]) 
            else:
               above_t_pocn          = float(tracer_vector_t_pocn         [k-1])
             
            t_lpp           = float(tracer_vector_t_lpp          [k])   # large-cell phytoplankton
            if (k == 0):
                above_t_lpp           = float(tracer_vector_t_lpp          [k]) 
            else:
               above_t_lpp           = float(tracer_vector_t_lpp          [k-1])
             
            t_ipw           = float(tracer_vector_t_ipw          [k])   # suspended iron phosphate
            if (k == 0):
                above_t_ipw           = float(tracer_vector_t_ipw          [k]) 
            else:
               above_t_ipw           = float(tracer_vector_t_ipw          [k-1])
             

            t_n2                  = max(t_n2           ,0.0) 
            above_t_n2            = max(above_t_n2           ,0.0) 
            t_o2                  = max(t_o2           ,0.0) 
            above_t_o2            = max(above_t_o2           ,0.0) 
            t_dic                 = max(t_dic          ,0.0) 
            above_t_dic           = max(above_t_dic          ,0.0) 
            t_nh4                 = max(t_nh4          ,0.0) 
            above_t_nh4           = max(above_t_nh4          ,0.0) 
            t_no3                 = max(t_no3          ,0.0) 
            above_t_no3           = max(above_t_no3          ,0.0) 
            t_po4                 = max(t_po4          ,0.0) 
            above_t_po4           = max(above_t_po4          ,0.0) 
            t_spp                 = max(t_spp          ,0.0) 
            above_t_spp           = max(above_t_spp          ,0.0) 
            t_zoo                 = max(t_zoo          ,0.0) 
            above_t_zoo           = max(above_t_zoo          ,0.0) 
            t_h2s                 = max(t_h2s          ,0.0) 
            above_t_h2s           = max(above_t_h2s          ,0.0) 
            t_sul                 = max(t_sul          ,0.0) 
            above_t_sul           = max(above_t_sul          ,0.0) 
            t_lip                 = max(t_lip          ,0.0) 
            above_t_lip           = max(above_t_lip          ,0.0) 
            t_doc                 = max(t_doc          ,0.0) 
            above_t_doc           = max(above_t_doc          ,0.0) 
            t_dop                 = max(t_dop          ,0.0) 
            above_t_dop           = max(above_t_dop          ,0.0) 
            t_don                 = max(t_don          ,0.0) 
            above_t_don           = max(above_t_don          ,0.0) 
            t_cdom                = max(t_cdom         ,0.0) 
            above_t_cdom          = max(above_t_cdom         ,0.0) 
            t_cya                 = max(t_cya          ,0.0) 
            above_t_cya           = max(above_t_cya          ,0.0) 
            t_det                 = max(t_det          ,0.0) 
            above_t_det           = max(above_t_det          ,0.0) 
            t_poc                 = max(t_poc          ,0.0) 
            above_t_poc           = max(above_t_poc          ,0.0) 
            t_pocp                = max(t_pocp         ,0.0) 
            above_t_pocp          = max(above_t_pocp         ,0.0) 
            t_pocn                = max(t_pocn         ,0.0) 
            above_t_pocn          = max(above_t_pocn         ,0.0) 
            t_lpp                 = max(t_lpp          ,0.0) 
            above_t_lpp           = max(above_t_lpp          ,0.0) 
            t_ipw                 = max(t_ipw          ,0.0) 
            above_t_ipw           = max(above_t_ipw          ,0.0) 

            if (k == kmax-1):
                cgt_dummyvar = 0.0
                t_sed           = tracer_scalar_t_sed             # sediment detritus
                t_ips           = tracer_scalar_t_ips             # iron phosphate in sediment
                t_sed_poc       = tracer_scalar_t_sed_poc         # sediment particular carbon
                t_sed_pocn      = tracer_scalar_t_sed_pocn        # sediment particular organic N+C
                t_sed_pocp      = tracer_scalar_t_sed_pocp        # sediment particular organic P+C

                t_sed           = max(t_sed          ,0.0) 
                t_ips           = max(t_ips          ,0.0) 
                t_sed_poc       = max(t_sed_poc      ,0.0) 
                t_sed_pocn      = max(t_sed_pocn     ,0.0) 
                t_sed_pocp      = max(t_sed_pocp     ,0.0) 
              

            #------------------------------------
            # STEP 4.1: calculate auxiliaries
            #------------------------------------
            # Iterative loops
            #----------------
            # initialize iterative auxiliary variables
            temp_k          = 0.0
            ph_temp         = 0.0
            k_water         = 0.0
            k0_co2          = 0.0
            k1_co2          = 0.0
            k2_co2          = 0.0
            k_boron         = 0.0
            k1_po4          = 0.0
            k2_po4          = 0.0
            k3_po4          = 0.0
            k1_h2s          = 0.0
            boron_total     = 0.0
            alk_boron       = 0.0
            alk_h2s         = 0.0
            alk_water       = 0.0
            alk_po4_denominator = 0.0
            alk_po4         = 0.0
            alk_co2_denominator = 0.0
            alk_co2         = 0.0
            alk_residual    = 0.0
            dalkp_dh3o      = 0.0
            dalkc_dh3o      = 0.0
            dalkresidual_dpH = 0.0
            ph              = 0.0
            h3o             = 1.0e-8
            
            # iterative loop vertLoc=WAT
            for cgt_iteration in range(1,10+1):
                cgt_dummyvar = 0.0
                if cgt_iteration <= 1:
                    # absolute temperature [K] :
                    temp_k          = cgt_temp + 273.15                     

            # iterative loop vertLoc=SED
            if (k == kmax-1):
                for cgt_iteration in range(1,10+1):
                    cgt_dummyvar = 0.0

            # iterative loop vertLoc=SUR
            if (k == 0):
                for cgt_iteration in range(1,10+1):
                    cgt_dummyvar = 0.0
                    if cgt_iteration <= 10:
                        # temporary value assumed for pH [1] :
                        ph_temp         = 0.0-log(h3o)/log(10.0)                
                    if cgt_iteration <= 1:
                        # self-ionization constant of Water [mol2/kg2] :
                        k_water         = exp( -13847.26 / temp_k + 148.96502 - 23.6521 * log(temp_k) + (118.67/temp_k - 5.977 + 1.0495 * log(temp_k)) * sqrt(cgt_sali) - 0.01615 * cgt_sali)        
                    if cgt_iteration <= 1:
                        # Solubility of CO2 [mol/kg/Pa] :
                        k0_co2          = exp(9345.17 / temp_k - 60.2409 + 23.3585 * (log(temp_k) - 4.605170186) + cgt_sali*(0.023517 - 0.00023656 * temp_k + 0.00000047036 *temp_k*temp_k))/101325.0        
                    if cgt_iteration <= 1:
                        # Acid dissociation constant CO2 + 2 H2O <-> HCO3- + H3O+ [mol/kg] :
                        k1_co2          = power(10.0,( -3633.86 / temp_k + 61.2172 - 9.6777 * log(temp_k) + 0.011555 * cgt_sali - 0.0001152 * cgt_sali * cgt_sali))        
                    if cgt_iteration <= 1:
                        # Acid dissociation constant HCO3- + H2O <-> [CO3 2-] + H3O+ [mol/kg] :
                        k2_co2          = power(10.0,( -471.78 / temp_k - 25.929 + 3.16967 * log(temp_k) + 0.01781 * cgt_sali - 0.0001122 * cgt_sali * cgt_sali))        
                    if cgt_iteration <= 1:
                        # Acid dissociation constant of boric acid [mol/kg] :
                        k_boron         = exp(( -8966.9 - 2890.53*sqrt(cgt_sali) - 77.942*cgt_sali + 1.728*cgt_sali*sqrt(cgt_sali) - 0.0996*cgt_sali*cgt_sali) / temp_k + 148.0248 + 137.1942*sqrt(cgt_sali) + 1.62142*cgt_sali + (-24.4344 - 25.085*sqrt(cgt_sali) - 0.2474*cgt_sali)*log(temp_k) + 0.053105*sqrt(cgt_sali)*temp_k )        
                    if cgt_iteration <= 1:
                        # Acid dissociation constant H3PO4 + H2O <-> [H2PO4 -] + H3O+ [mol/kg] :
                        k1_po4          = exp( -4576.752/temp_k + 115.525 - 18.453*log(temp_k) + (0.69171 - 106.736/temp_k)*sqrt(cgt_sali) - (0.01844 + 0.65643/temp_k)*cgt_sali )        
                    if cgt_iteration <= 1:
                        # Acid dissociation constant [H2PO4 -] + H2O <-> [HPO4 2-] + H3O+ [mol/kg] :
                        k2_po4          = exp( -8814.715/temp_k + 172.0883 - 27.927*log(temp_k) + (1.35660 - 160.340/temp_k)*sqrt(cgt_sali) - (0.05778 - 0.37335/temp_k)*cgt_sali )        
                    if cgt_iteration <= 1:
                        # Acid dissociation constant [HPO4 2-] + H2O <-> [PO4 3-] + H3O+ [mol/kg] :
                        k3_po4          = exp( -3070.75/temp_k - 18.141 + (2.81197 + 17.27039/temp_k)*sqrt(cgt_sali) - (0.09984 + 44.99486/temp_k)*cgt_sali )        
                    if cgt_iteration <= 1:
                        # Acid dissociation constant H2S + H2O <-> HS- + H3O+ [mol/kg] :
                        k1_h2s          = exp( -3131.42/temp_k + 5.818 + 0.368*(power(max(0.0,cgt_sali),(1.0/3.0))))        
                    if cgt_iteration <= 1:
                        # total concentration of boron [mol/kg] :
                        boron_total     = 0.000416 * cgt_sali/35.0              
                    if cgt_iteration <= 10:
                        # boron alkalinity [mol/kg] :
                        alk_boron       = boron_total * k_boron / (k_boron + h3o)        
                    if cgt_iteration <= 10:
                        # hydrogen sulfide alkalinity [mol/kg] :
                        alk_h2s         = t_h2s * k1_h2s / (k1_h2s + h3o)        
                    if cgt_iteration <= 10:
                        # water alkalinity [mol/kg] :
                        alk_water       = k_water / h3o - h3o                   
                    if cgt_iteration <= 10:
                        # denominator in phosphate alkalinity formula [mol3/kg3] :
                        alk_po4_denominator = (h3o*h3o*h3o + k1_po4*h3o*h3o + k1_po4*k2_po4*h3o + k1_po4*k2_po4*k3_po4)        
                    if cgt_iteration <= 10:
                        # phosphate alkalinity [mol/kg] :
                        alk_po4         = t_po4*(k1_po4*k2_po4*h3o + 2.0*k1_po4*k2_po4*k3_po4 - h3o*h3o*h3o) / alk_po4_denominator        
                    if cgt_iteration <= 10:
                        # denominator in carbonate alkalinity formula [mol2/kg2] :
                        alk_co2_denominator = (h3o*h3o + k1_co2*h3o + k1_co2*k2_co2)        
                    if cgt_iteration <= 10:
                        # carbonate alkalinity [mol/kg] :
                        alk_co2         = t_dic*k1_co2*(h3o+2*k2_co2)/alk_co2_denominator        
                    if cgt_iteration <= 10:
                        # error in total alkalinity calculation at the assumed pH [mol/kg] :
                        alk_residual    = t_alk - alk_co2 - alk_po4 - alk_boron - alk_h2s - alk_water        
                    if cgt_iteration <= 10:
                        # derivative of phosphate alkalinity with respect to h3o [1] :
                        dalkp_dh3o      = t_po4*(0.0-k1_po4*h3o*h3o*h3o*h3o-4*k1_po4*k2_po4*h3o*h3o*h3o-(k1_po4*k1_po4*k2_po4+9*k1_po4*k2_po4*k3_po4)*h3o*h3o-4*k1_po4*k1_po4*k2_po4*k3_po4*h3o-k1_po4*k1_po4*k2_po4*k2_po4*k3_po4)/(alk_po4_denominator*alk_po4_denominator)        
                    if cgt_iteration <= 10:
                        # derivative of carbonate alkalinity with respect to h3o [1] :
                        dalkc_dh3o      = t_dic*(0.0-k1_co2*h3o*h3o-k1_co2*k1_co2*k2_co2-4*k1_co2*k2_co2*h3o)/(alk_co2_denominator*alk_co2_denominator)        
                    if cgt_iteration <= 10:
                        # derivative of residual_alk with respect to pH [mol/kg] :
                        dalkresidual_dpH = 0.0-log(10.0)*h3o*(alk_boron/(k_boron+h3o)+alk_h2s/(k1_h2s+h3o)+k_water/(h3o*h3o)+1-dalkp_dh3o-dalkc_dh3o)        
                    if cgt_iteration <= 10:
                        # newly determined pH value [1] :
                        temp1  = alk_residual/dalkresidual_dpH  
                        ph              = ph_temp - temp1 + theta(abs(temp1) - 1)*0.5*temp1        
                    if cgt_iteration <= 10:
                        # h3o ion concentration [mol/kg] :
                        h3o             = power(10.0,0.0-max(1.0,min(13.0,ph)))        


            # Normal, non-iterative auxiliary variables
            #------------------------------------------
            # oxygen saturation concentration [mol/kg] :
            o2_sat          = (10.18e0+((5.306e-3-4.8725e-5*cgt_temp)*cgt_temp-0.2785e0)*cgt_temp+cgt_sali*((2.2258e-3+(4.39e-7*cgt_temp-4.645e-5)*cgt_temp)*cgt_temp-6.33e-2))*44.66e0*1e-6 
             
            # dissolved molecular nitrogen saturation concentration [mol/kg] :
            temp1  = log((298.15-cgt_temp)/(273.15+cgt_temp)) 
            temp2  = temp1*temp1                    
            temp3  = temp2*temp1                    
            n2_sat          = 1e-6*exp(6.42931 + 2.92704*temp1 + 4.32531*temp2 + 4.69149*temp3 + cgt_sali*(0.0 -7.44129e-3 - 8.02566e-3*temp1 - 1.46775e-2*temp2)) 
             
            # solubility of molecular nitrogen [mol/kg/Pa] :
            solubility_n2   = n2_sat * 1.263925e-5           
             
            # square of positive temperature [degC * degC] :
            temp_sq         = max(0.0,cgt_temp)*max(0.0,cgt_temp) 
             
            # effectice zooplankton concentration assumed for mortality and respiration process [mol/kg] :
            zoo_eff         = t_zoo*t_zoo/zoo_cl             
             
            # dissolved inorganic nitrogen [mol/kg] :
            din             = t_no3+t_nh4                    
             
            # squared DIN [mol2/kg2] :
            din_sq          = din*din                        
             
            # squared phosphate [mol**2/kg**2] :
            po4_sq          = t_po4*t_po4                    
             
            # total phytoplankton [mol/kg] :
            pp              = t_lpp+t_spp+t_cya              
             
            # large-cell phytoplankton plus seed concentration [mol/kg] :
            lpp_plus_lpp0   = t_lpp+lpp0                     
             
            # small-cell phytoplankton plus seed concentration [mol/kg] :
            spp_plus_spp0   = t_spp+spp0                     
             
            # limnic phytoplankton plus seed concentration [mol/kg] :
            lip_plus_lip0   = t_lip+lip0                     
             
            # diazotroph cyanobacteria plus seed concentration [mol/kg] :
            cya_plus_cya0   = t_cya+cya0                     
             
            # suitable food for zooplankton (weighted with food preferences) [mol/kg] :
            food_zoo        = t_lpp+t_spp+t_lip+0.5*t_cya    
             
            # light limitation factor for large-cell phytoplankton growth [1] :
            temp1  = max(cgt_light/2.0,light_opt_lpp) 
            lim_light_lpp   = cgt_light/temp1*exp(1-cgt_light/temp1) 
             
            # light limitation factor for small-cell phytoplankton growth [1] :
            temp1  = max(cgt_light/2.0,light_opt_spp) 
            lim_light_spp   = cgt_light/temp1*exp(1-cgt_light/temp1) 
             
            # light limitation factor for limnic phytoplankton growth [1] :
            temp1  = max(cgt_light/2.0,light_opt_lip) 
            lim_light_lip   = cgt_light/temp1*exp(1-cgt_light/temp1) 
             
            # light limitation factor for diazotroph cyanobacteria growth [1] :
            temp1  = max(cgt_light/2.0,light_opt_cya) 
            lim_light_cya   = cgt_light/temp1*exp(1-cgt_light/temp1) 
             
            # growth rate of large-cell phytoplankton, limited by DIN, DIP, light and oxygen [1/day] :
            lr_assim_lpp    = r_lpp_assim*theta(t_o2-2*t_h2s)*min(din_sq/(din_sq+din_min_lpp*din_min_lpp),min(po4_sq/(po4_sq+din_min_lpp*din_min_lpp*rfr_p*rfr_p),lim_light_lpp)) 
             
            # growth rate of small-cell phytoplankton, limited by DIN, DIP, light, oxygen and temperature [1/day] :
            lr_assim_spp    = r_spp_assim*theta(t_o2-2*t_h2s)*min(din_sq/(din_sq+din_min_spp*din_min_spp),min(po4_sq/(po4_sq+din_min_spp*din_min_spp*rfr_p*rfr_p),lim_light_spp))*(1+temp_sq/(temp_sq+temp_min_spp*temp_min_spp)) 
             
            # growth rate of limnic phytoplankton, limited by DIN, DIP, light, salt and oxygen [1/day] :
            lr_assim_lip    = r_lip_assim*theta(t_o2-2*t_h2s)*min(din_sq/(din_sq+din_min_lip*din_min_lip),min(po4_sq/(po4_sq+din_min_lip*din_min_lip*rfr_p*rfr_p),lim_light_lip))*(1/(1+exp(cgt_sali*cgt_sali-sali_max_lip*sali_max_lip))) 
             
            # growth rate of diazotroph cyanobacteria, limited by DIP, light, oxygen, temperature and salinity [1/day] :
            lr_assim_cya    = r_cya_assim*theta(t_o2-2*t_h2s)*min(po4_sq/(po4_sq+dip_min_cya*dip_min_cya),lim_light_cya)*(1/(1+exp(temp_switch_cya*(temp_min_cya-cgt_temp))))*(1/(1+exp(cgt_sali-sali_max_cya)))*(1/(1+exp(sali_min_cya-cgt_sali)))*(1/(1+exp(nit_switch_cya*(din-nit_max_cya)))) 
             
            # production rate of DOC by LPP :
            lr_assim_lpp_doc = fac_doc_assim_lpp * r_lpp_assim * theta(t_o2-2*t_h2s) * min(min(1 - din_sq/(din_sq+din_min_lpp*din_min_lpp),1 - po4_sq/(din_min_lpp*din_min_lpp*rfr_p*rfr_p + po4_sq)), lim_light_lpp) 
             
            # production rate of DOC by SPP :
            lr_assim_spp_doc = fac_doc_assim_spp * r_spp_assim * theta(t_o2-2*t_h2s) * min(min(1 - din_sq/(din_sq+din_min_spp*din_min_spp),1 - po4_sq/(din_min_spp*din_min_spp*rfr_p*rfr_p + po4_sq)), lim_light_spp)*(1+temp_sq/(temp_sq+temp_min_spp*temp_min_spp)) 
             
            # production rate of DOC by CYA :
            lr_assim_cya_doc = fac_doc_assim_cya * r_cya_assim*theta(t_o2-2*t_h2s)*min(1 - po4_sq/(po4_sq+dip_min_cya*dip_min_cya),lim_light_cya)*(1/(1+exp(temp_switch_cya*(temp_min_cya-cgt_temp))))*(1/(1+exp(cgt_sali-sali_max_cya)))*(1/(1+exp(sali_min_cya-cgt_sali))) 
             
            # production rate of DOC by LPP :
            lr_assim_lip_doc = fac_doc_assim_lip * r_lip_assim * theta(t_o2-2*t_h2s) * min(min(1 - din_sq/(din_sq+din_min_lip*din_min_lip),1 - po4_sq/(din_min_lip*din_min_lip*rfr_p*rfr_p + po4_sq)), lim_light_lip)*(1/(1+exp(cgt_sali-sali_max_lip))) 
             
            # production rate of DOP by LPP :
            lr_assim_lpp_dop = fac_dop_assim * r_lpp_assim * theta(t_o2-2*t_h2s) * min(min(1 - din_sq/(din_sq+din_min_lpp*din_min_lpp),po4_sq/(din_min_lpp*din_min_lpp*rfr_p*rfr_p + po4_sq)), lim_light_lpp) 
             
            # production rate of DOP by SPP :
            lr_assim_spp_dop = fac_dop_assim * r_spp_assim * theta(t_o2-2*t_h2s) * min(min(1 - din_sq/(din_sq+din_min_spp*din_min_spp),po4_sq/(din_min_spp*din_min_spp*rfr_p*rfr_p + po4_sq)), lim_light_spp)*(1+temp_sq/(temp_sq+temp_min_spp*temp_min_spp)) 
             
            # production rate of DOP by LPP :
            lr_assim_lip_dop = fac_dop_assim * r_lip_assim * theta(t_o2-2*t_h2s) * min(min(1 - din_sq/(din_sq+din_min_lip*din_min_lip),po4_sq/(din_min_lip*din_min_lip*rfr_p*rfr_p + po4_sq)), lim_light_lip)*(1/(1+exp(cgt_sali-sali_max_lip))) 
             
            # production rate of DON by LPP :
            lr_assim_lpp_don = fac_don_assim * r_lpp_assim * theta(t_o2-2*t_h2s) * min(min(din_sq/(din_sq+din_min_lpp*din_min_lpp),1 - po4_sq/(din_min_lpp*din_min_lpp*rfr_p*rfr_p + po4_sq)), lim_light_lpp) 
             
            # production rate of DON by SPP :
            lr_assim_spp_don = fac_don_assim * r_spp_assim * theta(t_o2-2*t_h2s) * min(min(din_sq/(din_sq+din_min_spp*din_min_spp),1 - po4_sq/(din_min_spp*din_min_spp*rfr_p*rfr_p + po4_sq)), lim_light_spp)*(1+temp_sq/(temp_sq+temp_min_spp*temp_min_spp)) 
             
            # production rate of DON by limnic phytoplankton :
            lr_assim_lip_don = fac_don_assim * r_lip_assim * theta(t_o2-2*t_h2s) * min(min(din_sq/(din_sq+din_min_lip*din_min_lip),1 - po4_sq/(din_min_lip*din_min_lip*rfr_p*rfr_p + po4_sq)), lim_light_lip)*(1/(1+exp(cgt_sali-sali_max_lip))) 
             
            # growth rate of zooplankton, limited by food, oxygen and temperature [1/day] :
            lr_graz_zoo     = r_zoo_graz*(1-exp(-food_zoo*food_zoo/(food_min_zoo*food_min_zoo)))*theta(t_o2-2*t_h2s)*(1.0+temp_sq/(temp_opt_zoo*temp_opt_zoo)*exp(2.0-cgt_temp*2.0/temp_opt_zoo)) 
             
            # fraction of phosphate which is retained as iron-bound phosphate instead of being released after mineralization in the sediment [1] :
            frac_po4retent  = ret_po4_1 + ret_po4_2*theta(cgt_latitude-60.75) + ret_po4_3*theta(cgt_latitude-63.75) 
             
            # modifies pocp recycling towards Redfield ratio if PO4 is depleted :
            ref_p_sw        = (1 - (po4_sq/(rfr_p*din_min_lpp*rfr_p*din_min_lpp+po4_sq)))/(1+exp(6.0*(1-din/(t_po4/rfr_p+epsilon)))) 
             
            # modifies pocn recycling towards Redfield ratio if DIN is depleted :
            ref_n_sw        = (1 - (din_sq/(din_min_lpp*din_min_lpp+din_sq)))/(1+exp(6.0*(1-t_po4/rfr_p/(din+epsilon)))) 
             
            # add an additional POCP recycling if PO4 below Redfield but sufficient DIN :
            lr_pocp         = r_pocp_rec*(1 + fac_enh_rec*ref_p_sw) 
             
            # add an additional DOP recycling if PO4 is below Redfield but sufficient DIN :
            lr_dop          = r_dop_rec*(1 + fac_enh_rec*ref_p_sw) 
             
            # add an additional POCN recycling if DIN below Redfield but sufficient PO4 :
            lr_pocn         = r_pocn_rec*(1 + fac_enh_rec*ref_n_sw) 
             
            # add an additional DON recycling if DIN below Redfield but sufficient PO4 :
            lr_don          = r_don_rec*(1 + fac_enh_rec*ref_n_sw) 
             
            # depth dependent POC sinking speed :
            w_poc_var       = martin_fac_poc * cgt_bottomdepth * (-1.0) 
             
            # depth dependent POCN sinking speed :
            w_pocn_var      = -0.15                          
             
            # depth dependent POCP sinking speed :
            w_pocp_var      = -0.15                          
             

            if (k == kmax-1):
                cgt_dummyvar = 0.0
                # fraction of ammonium that is immediately nitrified and denitrified after remineralization in oxic sediments :
                frac_denit_sed  = frac_denit_scal*(0.5+0.5*exp(-0.01*cgt_bottomdepth))  
                
                # total carbon in sediment layer [mol/m**2] :
                sed_tot         = t_sed*rfr_c + t_sed_poc + t_sed_pocn*rfr_c + t_sed_pocp*rfr_cp  
                
                # total carbon in active sediment layer [mol/m**2] :
                sed_tot_active  = max(0.0,min(sed_tot,sed_max*rfr_c))  
                
                # total carbon in sediment layer before burial [mol/m**2] :
                sed_tot_burial  = max(0.0,min(sed_tot,sed_burial*rfr_c))  
                
                # detritus in active sediment layer [mol/m**2] :
                sed_active      = sed_tot_active * t_sed/sed_tot  
                
                # recycling rate of sediment detritus, limited by oxygen [1/d] :
                lr_sed_rec      = r_sed_rec*exp(q10_sed_rec*cgt_temp)*(1.0-reduced_rec*theta(2*t_h2s-t_o2))  
                
                # recycling rate of sediment POC, limited by oxygen [1/d] :
                lr_sed_poc_rec  = r_sed_poc_rec*exp(q10_sed_rec*cgt_temp)*(1.0-reduced_rec*theta(2*t_h2s-t_o2))  
                
                # effective concentration of iron phosphate in the sediment assumed for burial (enhanced burial above a threshold) [mol/m**2] :
                ips_eff         = max(t_ips,t_ips+t_ips*(t_ips-ips_threshold)/ips_cl)  
                
                # switch (1=erosion, 0=no erosion) which depends on the combined bottom stress of currents and waves :
                erosion_is_active = theta(cgt_current_wave_stress - critical_stress)  
                
                # poc in active sediment layer [mol/m**2] :
                poc_active      = sed_tot_active * t_sed_poc/sed_tot  
                
                # pocn in active sediment layer [mol/m**2] :
                pocn_active     = sed_tot_active * t_sed_pocn/sed_tot  
                
                # pocp in active sediment layer [mol/m**2] :
                pocp_active     = sed_tot_active * t_sed_pocp/sed_tot  
                
                # latitude dependence of alk BTF (Bothnian Sea) :
                alk_btf_l1      = 1/(1+exp(5*(60.5 - cgt_latitude)))  
                
                # latitude dependence of alk BTF (Bothnian Bay) :
                alk_btf_l2      = 1/(1+exp(5*(cgt_latitude - 63.5)))  
                
                # depth dependence of alk dissolution :
                alk_btf_db1     = theta(cgt_bottomdepth-alk_btf_D1)*theta(alk_btf_D2-cgt_bottomdepth)  
                
                # depth dependence of alk dissolution :
                alk_btf_db2     = theta(cgt_bottomdepth-alk_btf_D2)  
                
                # Alk bottom flux in Bothnian Sea :
                alk_btf_sw_BS   = alk_btf_l1 * alk_btf_l2 * (alk_btf_db1 + alk_btf_Dfac*alk_btf_db2)  
                
                # Alk bottom flux in Bothnian Bay :
                alk_btf_sw_BB   = (1 - alk_btf_l2) * (alk_btf_db1 + alk_btf_DBBfac*alk_btf_db2)  
                
              
             
            if (k == 0):
                cgt_dummyvar = 0.0
                # co2 partial pressure [Pa] :
                pco2            = t_dic / k0_co2 / (1 + k1_co2/h3o + k1_co2*k2_co2/h3o/h3o)  
                
                # CO2 concentration in the surface layer [mol/kg] :
                co2             = pco2*k0_co2                     
                
                # Schmidt number for CO2 surface flux [1] :
                schmidtnumber_co2 = max(250.0,2068.9 + cgt_temp*((-118.63) + cgt_temp*(2.9311 + cgt_temp*(-0.027))))  
                
                # solubility of oxygen [mol/kg/Pa] :
                solubility_o2   = o2_sat*4.71265e-5               
                
                # Schmidt number for oxygen surface flux [1] :
                schmidtnumber_o2 = max(250.0,1929.7 + cgt_temp*((-117.46) + cgt_temp*(3.116 + cgt_temp*(-0.0306))))  
                
                # Schmidt number for nitrogen surface flux [1] :
                schmidtnumber_n2 = max(250.0,2206.1 + cgt_temp*((-144.86) + cgt_temp*(4.5413 + cgt_temp*(-0.056988))))  
                
              
             
            #------------------------------------
            # STEP 4.2: output of auxiliaries
            #------------------------------------
            output_vector_lr_assim_lpp   [k] = output_vector_lr_assim_lpp   [k] + lr_assim_lpp    
            output_vector_lr_assim_spp   [k] = output_vector_lr_assim_spp   [k] + lr_assim_spp    
            output_vector_lr_assim_cya   [k] = output_vector_lr_assim_cya   [k] + lr_assim_cya    
            output_vector_lr_assim_lpp_doc[k] = output_vector_lr_assim_lpp_doc[k] + lr_assim_lpp_doc 
            output_vector_lr_assim_spp_doc[k] = output_vector_lr_assim_spp_doc[k] + lr_assim_spp_doc 
            output_vector_lr_assim_cya_doc[k] = output_vector_lr_assim_cya_doc[k] + lr_assim_cya_doc 
            output_vector_lr_assim_lpp_dop[k] = output_vector_lr_assim_lpp_dop[k] + lr_assim_lpp_dop 
            output_vector_lr_assim_spp_dop[k] = output_vector_lr_assim_spp_dop[k] + lr_assim_spp_dop 
            output_vector_lr_assim_lpp_don[k] = output_vector_lr_assim_lpp_don[k] + lr_assim_lpp_don 
            output_vector_lr_assim_spp_don[k] = output_vector_lr_assim_spp_don[k] + lr_assim_spp_don 
            output_vector_ref_p_sw       [k] = output_vector_ref_p_sw       [k] + ref_p_sw        
            output_vector_ref_n_sw       [k] = output_vector_ref_n_sw       [k] + ref_n_sw        
            output_vector_lr_pocp        [k] = output_vector_lr_pocp        [k] + lr_pocp         
            output_vector_lr_dop         [k] = output_vector_lr_dop         [k] + lr_dop          
            output_vector_lr_pocn        [k] = output_vector_lr_pocn        [k] + lr_pocn         
            output_vector_lr_don         [k] = output_vector_lr_don         [k] + lr_don          
            output_vector_w_poc_var      [k] = output_vector_w_poc_var      [k] + w_poc_var       
            output_vector_w_pocn_var     [k] = output_vector_w_pocn_var     [k] + w_pocn_var      
            output_vector_w_pocp_var     [k] = output_vector_w_pocp_var     [k] + w_pocp_var      

            if (k == kmax-1):
                cgt_dummyvar = 0.0
              
            if (k == 0):
                cgt_dummyvar = 0.0
                output_scalar_k0_co2          = output_scalar_k0_co2          + k0_co2          
                output_scalar_k1_co2          = output_scalar_k1_co2          + k1_co2          
                output_scalar_k2_co2          = output_scalar_k2_co2          + k2_co2          
                output_scalar_alk_boron       = output_scalar_alk_boron       + alk_boron       
                output_scalar_alk_h2s         = output_scalar_alk_h2s         + alk_h2s         
                output_scalar_alk_water       = output_scalar_alk_water       + alk_water       
                output_scalar_alk_po4         = output_scalar_alk_po4         + alk_po4         
                output_scalar_alk_co2         = output_scalar_alk_co2         + alk_co2         
                output_scalar_alk_residual    = output_scalar_alk_residual    + alk_residual    
                output_scalar_dalkc_dh3o      = output_scalar_dalkc_dh3o      + dalkc_dh3o      
                output_scalar_dalkresidual_dpH = output_scalar_dalkresidual_dpH + dalkresidual_dpH 
                output_scalar_ph              = output_scalar_ph              + ph              
                output_scalar_h3o             = output_scalar_h3o             + h3o             
                output_scalar_pco2            = output_scalar_pco2            + pco2            
                output_scalar_schmidtnumber_co2 = output_scalar_schmidtnumber_co2 + schmidtnumber_co2 
                output_scalar_schmidtnumber_o2 = output_scalar_schmidtnumber_o2 + schmidtnumber_o2 
                output_scalar_schmidtnumber_n2 = output_scalar_schmidtnumber_n2 + schmidtnumber_n2 
              

            #------------------------------------
            # STEP 5: calculate process limitations
            #------------------------------------

            lim_t_n2_7           = theta(t_n2-0.0) 
            lim_t_o2_0           = 1.0-exp(-t_o2/o2_min_det_resp) 
            lim_t_o2_2           = theta(t_o2-0.0) 
            lim_t_o2_4           = t_o2*t_o2/(t_o2*t_o2+o2_min_po4_retent*o2_min_po4_retent) 
            lim_t_o2_6           = t_o2*t_o2/(t_o2*t_o2+o2_min_sed_resp*o2_min_sed_resp) 
            lim_t_dic_8          = theta(t_dic-0.0) 
            lim_t_nh4_11         = theta(t_nh4-0.0) 
            lim_t_no3_1          = 1.0-exp(-t_no3/no3_min_det_denit) 
            lim_t_no3_3          = t_no3*t_no3/(t_no3*t_no3+no3_min_sed_denit*no3_min_sed_denit) 
            lim_t_no3_9          = theta(t_no3-0.0) 
            lim_t_po4_10         = theta(t_po4-0.0) 
            lim_t_spp_16         = theta(t_spp-0.0) 
            lim_t_zoo_19         = theta(t_zoo-0.0) 
            lim_t_h2s_5          = theta(t_h2s-h2s_min_po4_liber) 
            lim_t_h2s_24         = theta(t_h2s-0.0) 
            lim_t_sul_25         = theta(t_sul-0.0) 
            lim_t_lip_18         = theta(t_lip-0.0) 
            lim_t_doc_29         = theta(t_doc-0.0) 
            lim_t_dop_30         = theta(t_dop-0.0) 
            lim_t_don_31         = theta(t_don-0.0) 
            lim_t_cdom_32        = theta(t_cdom-0.0) 
            lim_t_cya_17         = theta(t_cya-0.0) 
            lim_t_det_20         = theta(t_det-0.0) 
            lim_t_poc_12         = theta(t_poc-0.0) 
            lim_t_pocp_13        = theta(t_pocp-0.0) 
            lim_t_pocn_14        = theta(t_pocn-0.0) 
            lim_t_lpp_15         = theta(t_lpp-0.0) 
            lim_t_ipw_26         = theta(t_ipw-0.0) 

            if (k == kmax-1):
                cgt_dummyvar = 0.0
                lim_t_sed_21         = theta(t_sed-0.0) 
                lim_t_ips_23         = theta(t_ips-0.0) 
                lim_t_sed_poc_22     = theta(t_sed_poc-0.0) 
                lim_t_sed_pocn_27    = theta(t_sed_pocn-0.0) 
                lim_t_sed_pocp_28    = theta(t_sed_pocp-0.0) 
              

            if (k == 0):
                cgt_dummyvar = 0.0
              

            #------------------------------------
            #-- POSITIVE-DEFINITE SCHEME --------
            #-- means the following steps will be repeated as often as nessecary
            #------------------------------------

            fraction_of_total_timestep = 1.0     # how much of the original timestep is remaining
            total_rate_p_n2_stf_down            = 0.0 
            total_rate_p_n2_stf_up              = 0.0 
            total_rate_p_o2_stf_down            = 0.0 
            total_rate_p_o2_stf_up              = 0.0 
            total_rate_p_co2_stf_down           = 0.0 
            total_rate_p_co2_stf_up             = 0.0 
            total_rate_p_no3_assim_lpp          = 0.0 
            total_rate_p_nh4_assim_lpp          = 0.0 
            total_rate_p_no3_assim_spp          = 0.0 
            total_rate_p_nh4_assim_spp          = 0.0 
            total_rate_p_nh4_assim_lip          = 0.0 
            total_rate_p_no3_assim_lip          = 0.0 
            total_rate_p_n2_assim_cya           = 0.0 
            total_rate_p_assim_lpp_doc          = 0.0 
            total_rate_p_assim_spp_doc          = 0.0 
            total_rate_p_assim_lip_doc          = 0.0 
            total_rate_p_assim_cya_doc          = 0.0 
            total_rate_p_assim_lpp_dop          = 0.0 
            total_rate_p_assim_spp_dop          = 0.0 
            total_rate_p_assim_lip_dop          = 0.0 
            total_rate_p_nh4_assim_lpp_don          = 0.0 
            total_rate_p_no3_assim_lpp_don          = 0.0 
            total_rate_p_nh4_assim_spp_don          = 0.0 
            total_rate_p_no3_assim_spp_don          = 0.0 
            total_rate_p_nh4_assim_lip_don          = 0.0 
            total_rate_p_no3_assim_lip_don          = 0.0 
            total_rate_p_poc_resp               = 0.0 
            total_rate_p_poc_denit              = 0.0 
            total_rate_p_poc_sulf               = 0.0 
            total_rate_p_pocp_resp              = 0.0 
            total_rate_p_pocp_denit             = 0.0 
            total_rate_p_pocp_sulf              = 0.0 
            total_rate_p_pocn_resp              = 0.0 
            total_rate_p_pocn_denit             = 0.0 
            total_rate_p_pocn_sulf              = 0.0 
            total_rate_p_lpp_graz_zoo           = 0.0 
            total_rate_p_spp_graz_zoo           = 0.0 
            total_rate_p_cya_graz_zoo           = 0.0 
            total_rate_p_lip_graz_zoo           = 0.0 
            total_rate_p_lpp_resp_nh4           = 0.0 
            total_rate_p_spp_resp_nh4           = 0.0 
            total_rate_p_lip_resp_nh4           = 0.0 
            total_rate_p_cya_resp_nh4           = 0.0 
            total_rate_p_zoo_resp_nh4           = 0.0 
            total_rate_p_lpp_mort_det           = 0.0 
            total_rate_p_spp_mort_det           = 0.0 
            total_rate_p_lip_mort_det           = 0.0 
            total_rate_p_cya_mort_det           = 0.0 
            total_rate_p_cya_mort_det_diff          = 0.0 
            total_rate_p_zoo_mort_det           = 0.0 
            total_rate_p_nh4_nit_no3            = 0.0 
            total_rate_p_det_resp_nh4           = 0.0 
            total_rate_p_det_denit_nh4          = 0.0 
            total_rate_p_det_sulf_nh4           = 0.0 
            total_rate_p_sed_resp_nh4           = 0.0 
            total_rate_p_sed_denit_nh4          = 0.0 
            total_rate_p_sed_sulf_nh4           = 0.0 
            total_rate_p_sed_poc_resp           = 0.0 
            total_rate_p_sed_poc_denit          = 0.0 
            total_rate_p_sed_poc_sulf           = 0.0 
            total_rate_p_po4_retent_ips          = 0.0 
            total_rate_p_ips_liber_po4          = 0.0 
            total_rate_p_h2s_oxo2_sul           = 0.0 
            total_rate_p_h2s_oxno3_sul          = 0.0 
            total_rate_p_sul_oxo2_so4           = 0.0 
            total_rate_p_sul_oxno3_so4          = 0.0 
            total_rate_p_det_sedi_sed           = 0.0 
            total_rate_p_ipw_sedi_ips           = 0.0 
            total_rate_p_poc_sedi_sed           = 0.0 
            total_rate_p_pocn_sedi_sed          = 0.0 
            total_rate_p_pocp_sedi_sed          = 0.0 
            total_rate_p_sed_ero_det            = 0.0 
            total_rate_p_ips_ero_ipw            = 0.0 
            total_rate_p_sed_ero_poc            = 0.0 
            total_rate_p_sed_ero_pocn           = 0.0 
            total_rate_p_sed_ero_pocp           = 0.0 
            total_rate_p_sed_biores_det          = 0.0 
            total_rate_p_ips_biores_ipw          = 0.0 
            total_rate_p_sed_biores_poc          = 0.0 
            total_rate_p_sed_biores_pocn          = 0.0 
            total_rate_p_sed_biores_pocp          = 0.0 
            total_rate_p_sed_burial             = 0.0 
            total_rate_p_ips_burial             = 0.0 
            total_rate_p_poc_burial             = 0.0 
            total_rate_p_pocn_burial            = 0.0 
            total_rate_p_pocp_burial            = 0.0 
            total_rate_p_sed_pocn_resp          = 0.0 
            total_rate_p_sed_pocp_resp          = 0.0 
            total_rate_p_sed_pocn_denit          = 0.0 
            total_rate_p_sed_pocp_denit          = 0.0 
            total_rate_p_sed_pocn_sulf          = 0.0 
            total_rate_p_sed_pocp_sulf          = 0.0 
            total_rate_p_doc2pco                = 0.0 
            total_rate_p_dop2pocp               = 0.0 
            total_rate_p_don2pocn               = 0.0 
            total_rate_p_doc_resp               = 0.0 
            total_rate_p_doc_denit              = 0.0 
            total_rate_p_doc_sulf               = 0.0 
            total_rate_p_dop_resp               = 0.0 
            total_rate_p_dop_denit              = 0.0 
            total_rate_p_dop_sulf               = 0.0 
            total_rate_p_don_resp               = 0.0 
            total_rate_p_don_denit              = 0.0 
            total_rate_p_don_sulf               = 0.0 
            total_rate_p_cdom_decay             = 0.0 
            total_rate_p_alk_btf                = 0.0 
            total_rate_p_nh4_nitdenit_n2          = 0.0 
            number_of_loop = 1 

            while (cgt_timestep > 0.0):

                #------------------------------------
                # STEP 6.1: calculate process rates
                #------------------------------------
                # assimilation of nitrate by large-cell phytoplankton :
                p_no3_assim_lpp = (lpp_plus_lpp0*lr_assim_lpp*t_no3/(din+epsilon))*lim_t_no3_9*lim_t_po4_10*lim_t_dic_8 
                p_no3_assim_lpp = max(p_no3_assim_lpp,0.0) 

                # assimilation of ammonium by large-cell phytoplankton :
                p_nh4_assim_lpp = (lpp_plus_lpp0*lr_assim_lpp*t_nh4/(din+epsilon))*lim_t_dic_8*lim_t_po4_10*lim_t_nh4_11 
                p_nh4_assim_lpp = max(p_nh4_assim_lpp,0.0) 

                # assimilation of nitrate by small-cell phytoplankton :
                p_no3_assim_spp = (spp_plus_spp0*lr_assim_spp*t_no3/(din+epsilon))*lim_t_no3_9*lim_t_po4_10*lim_t_dic_8 
                p_no3_assim_spp = max(p_no3_assim_spp,0.0) 

                # assimilation of ammonium by small-cell phytoplankton :
                p_nh4_assim_spp = (spp_plus_spp0*lr_assim_spp*t_nh4/(din+epsilon))*lim_t_dic_8*lim_t_po4_10*lim_t_nh4_11 
                p_nh4_assim_spp = max(p_nh4_assim_spp,0.0) 

                # assimilation of ammonium by limnic phytoplankton :
                p_nh4_assim_lip = (lip_plus_lip0*lr_assim_lip*t_nh4/(din+epsilon))*lim_t_nh4_11*lim_t_po4_10*lim_t_dic_8 
                p_nh4_assim_lip = max(p_nh4_assim_lip,0.0) 

                # assimilation of nitrate by limnic phytoplankton :
                p_no3_assim_lip = (lip_plus_lip0*lr_assim_lip*t_no3/(din+epsilon))*lim_t_dic_8*lim_t_po4_10*lim_t_no3_9 
                p_no3_assim_lip = max(p_no3_assim_lip,0.0) 

                # fixation of dinitrogen by diazotroph cyanobacteria :
                p_n2_assim_cya  = (cya_plus_cya0*lr_assim_cya)*lim_t_dic_8*lim_t_po4_10*lim_t_n2_7 
                p_n2_assim_cya  = max(p_n2_assim_cya ,0.0) 

                # Production of DOC by LIP :
                p_assim_lpp_doc = (rfr_c * t_lpp * lr_assim_lpp_doc)*lim_t_dic_8 
                p_assim_lpp_doc = max(p_assim_lpp_doc,0.0) 

                # Production of DOC by SPP :
                p_assim_spp_doc = (rfr_c * t_spp * lr_assim_spp_doc)*lim_t_dic_8 
                p_assim_spp_doc = max(p_assim_spp_doc,0.0) 

                # Production of DOC by LPP :
                p_assim_lip_doc = (rfr_c * t_lip * lr_assim_lip_doc)*lim_t_dic_8 
                p_assim_lip_doc = max(p_assim_lip_doc,0.0) 

                # Production of DOC by CYA :
                p_assim_cya_doc = (rfr_c * t_cya * lr_assim_cya_doc)*lim_t_dic_8 
                p_assim_cya_doc = max(p_assim_cya_doc,0.0) 

                # Production of DOP by LPP :
                p_assim_lpp_dop = (rfr_p * t_lpp * lr_assim_lpp_dop)*lim_t_po4_10*lim_t_dic_8 
                p_assim_lpp_dop = max(p_assim_lpp_dop,0.0) 

                # Production of DOP by SPP :
                p_assim_spp_dop = (rfr_p * t_spp * lr_assim_spp_dop)*lim_t_dic_8*lim_t_po4_10 
                p_assim_spp_dop = max(p_assim_spp_dop,0.0) 

                # Production of DOP by LIP :
                p_assim_lip_dop = (rfr_p * t_lip * lr_assim_lip_dop)*lim_t_po4_10*lim_t_dic_8 
                p_assim_lip_dop = max(p_assim_lip_dop,0.0) 

                # Production of DON by LPP :
                p_nh4_assim_lpp_don = (t_lpp * lr_assim_lpp_don*t_nh4/(din+epsilon))*lim_t_dic_8*lim_t_nh4_11 
                p_nh4_assim_lpp_don = max(p_nh4_assim_lpp_don,0.0) 

                # Production of DON by LPP :
                p_no3_assim_lpp_don = (t_lpp * lr_assim_lpp_don*t_no3/(din+epsilon))*lim_t_no3_9*lim_t_dic_8 
                p_no3_assim_lpp_don = max(p_no3_assim_lpp_don,0.0) 

                # Production of DON by SPP :
                p_nh4_assim_spp_don = (t_spp * lr_assim_spp_don*t_nh4/(din+epsilon))*lim_t_nh4_11*lim_t_dic_8 
                p_nh4_assim_spp_don = max(p_nh4_assim_spp_don,0.0) 

                # Production of DON by SPP :
                p_no3_assim_spp_don = (t_spp * lr_assim_spp_don*t_no3/(din+epsilon))*lim_t_dic_8*lim_t_no3_9 
                p_no3_assim_spp_don = max(p_no3_assim_spp_don,0.0) 

                # Production of DON by LIP :
                p_nh4_assim_lip_don = (t_lip * lr_assim_lip_don*t_nh4/(din+epsilon))*lim_t_nh4_11*lim_t_dic_8 
                p_nh4_assim_lip_don = max(p_nh4_assim_lip_don,0.0) 

                # Production of DON by LIP :
                p_no3_assim_lip_don = (t_lip * lr_assim_lip_don*t_no3/(din+epsilon))*lim_t_dic_8*lim_t_no3_9 
                p_no3_assim_lip_don = max(p_no3_assim_lip_don,0.0) 

                # respiration of POC :
                p_poc_resp      = (t_poc * r_poc_rec * exp(q10_det_rec * cgt_temp))*lim_t_o2_0*lim_t_poc_12 
                p_poc_resp      = max(p_poc_resp     ,0.0) 

                # recycling of POC using nitrate (denitrification) :
                p_poc_denit     = (t_poc*r_poc_rec*exp(q10_det_rec*cgt_temp))*(1.0-lim_t_o2_0)*lim_t_no3_1*lim_t_poc_12 
                p_poc_denit     = max(p_poc_denit    ,0.0) 

                # Mineralization of POC, e-acceptor sulfate (sulfate reduction) :
                p_poc_sulf      = (t_poc*r_poc_rec*exp(q10_det_rec*cgt_temp))*(1.0-lim_t_o2_0)*(1.0-lim_t_no3_1)*lim_t_poc_12 
                p_poc_sulf      = max(p_poc_sulf     ,0.0) 

                # respiration of POCP :
                p_pocp_resp     = (t_pocp * lr_pocp * exp(q10_det_rec * cgt_temp))*lim_t_o2_0*lim_t_pocp_13 
                p_pocp_resp     = max(p_pocp_resp    ,0.0) 

                # recycling of POC using nitrate (denitrification) :
                p_pocp_denit    = (t_pocp*r_pocp_rec*exp(q10_det_rec*cgt_temp))*(1.0-lim_t_o2_0)*lim_t_no3_1*lim_t_pocp_13 
                p_pocp_denit    = max(p_pocp_denit   ,0.0) 

                # Mineralization of POC, e-acceptor sulfate (sulfate reduction) :
                p_pocp_sulf     = (t_pocp*r_pocp_rec*exp(q10_det_rec*cgt_temp))*(1.0-lim_t_o2_0)*(1.0-lim_t_no3_1)*lim_t_pocp_13 
                p_pocp_sulf     = max(p_pocp_sulf    ,0.0) 

                # respiration of POCN :
                p_pocn_resp     = (t_pocn * lr_pocn * exp(q10_det_rec * cgt_temp))*lim_t_o2_0*lim_t_pocn_14 
                p_pocn_resp     = max(p_pocn_resp    ,0.0) 

                # recycling of POCN using nitrate (denitrification) :
                p_pocn_denit    = (t_pocn*r_pocn_rec*exp(q10_det_rec*cgt_temp))*(1.0-lim_t_o2_0)*lim_t_no3_1*lim_t_pocn_14 
                p_pocn_denit    = max(p_pocn_denit   ,0.0) 

                # Mineralization of POCN, e-acceptor sulfate (sulfate reduction) :
                p_pocn_sulf     = (t_pocn*r_pocn_rec*exp(q10_det_rec*cgt_temp))*(1.0-lim_t_o2_0)*(1.0-lim_t_no3_1)*lim_t_pocn_14 
                p_pocn_sulf     = max(p_pocn_sulf    ,0.0) 

                # grazing of zooplankton eating large-cell phytoplankton :
                p_lpp_graz_zoo  = ((t_zoo+zoo0)*lr_graz_zoo*t_lpp/max(food_zoo,epsilon))*lim_t_lpp_15 
                p_lpp_graz_zoo  = max(p_lpp_graz_zoo ,0.0) 

                # grazing of zooplankton eating small-cell phytoplankton :
                p_spp_graz_zoo  = ((t_zoo+zoo0)*lr_graz_zoo*t_spp/max(food_zoo,epsilon))*lim_t_spp_16 
                p_spp_graz_zoo  = max(p_spp_graz_zoo ,0.0) 

                # grazing of zooplankton eating diazotroph cyanobacteria :
                p_cya_graz_zoo  = ((t_zoo+zoo0)*lr_graz_zoo*(0.5*t_cya)/max(food_zoo,epsilon))*lim_t_cya_17 
                p_cya_graz_zoo  = max(p_cya_graz_zoo ,0.0) 

                # grazing of zooplankton eating limnic phytoplankton :
                p_lip_graz_zoo  = ((t_zoo+zoo0)*lr_graz_zoo*t_lip/max(food_zoo,epsilon))*lim_t_lip_18 
                p_lip_graz_zoo  = max(p_lip_graz_zoo ,0.0) 

                # respiration of large-cell phytoplankton :
                p_lpp_resp_nh4  = (t_lpp*r_lpp_resp)*lim_t_lpp_15*lim_t_o2_2 
                p_lpp_resp_nh4  = max(p_lpp_resp_nh4 ,0.0) 

                # respiration of small-cell phytoplankton :
                p_spp_resp_nh4  = (t_spp*r_spp_resp)*lim_t_o2_2*lim_t_spp_16 
                p_spp_resp_nh4  = max(p_spp_resp_nh4 ,0.0) 

                # respiration of limnic phytoplankton :
                p_lip_resp_nh4  = (t_lip*r_lip_resp)*lim_t_o2_2*lim_t_lip_18 
                p_lip_resp_nh4  = max(p_lip_resp_nh4 ,0.0) 

                # respiration of diazotroph cyanobacteria :
                p_cya_resp_nh4  = (t_cya*r_cya_resp)*lim_t_o2_2*lim_t_cya_17 
                p_cya_resp_nh4  = max(p_cya_resp_nh4 ,0.0) 

                # respiration of zooplankton :
                p_zoo_resp_nh4  = (zoo_eff*r_zoo_resp)*lim_t_o2_2*lim_t_zoo_19 
                p_zoo_resp_nh4  = max(p_zoo_resp_nh4 ,0.0) 

                # mortality of large-cell phytoplankton :
                p_lpp_mort_det  = (t_lpp*r_pp_mort*(1+9*theta(5.0e-6-t_o2)))*lim_t_lpp_15 
                p_lpp_mort_det  = max(p_lpp_mort_det ,0.0) 

                # mortality of small-scale phytoplankton :
                p_spp_mort_det  = (t_spp*r_pp_mort*(1+9*theta(5.0e-6-t_o2)))*lim_t_spp_16 
                p_spp_mort_det  = max(p_spp_mort_det ,0.0) 

                # mortality of limnic phytoplankton :
                p_lip_mort_det  = (t_lip*r_pp_mort*(1+9*theta(5.0e-6-t_o2)))*lim_t_lip_18 
                p_lip_mort_det  = max(p_lip_mort_det ,0.0) 

                # mortality of diazotroph cyanobacteria :
                p_cya_mort_det  = (t_cya*r_pp_mort*(1+9*theta(5.0e-6-t_o2)))*lim_t_cya_17 
                p_cya_mort_det  = max(p_cya_mort_det ,0.0) 

                # mortality of diazotroph cyanobacteria due to strong turbulence :
                p_cya_mort_det_diff = (t_cya*r_pp_mort*(r_cya_mort_diff*theta(cgt_diffusivity-r_cya_mort_thresh)))*lim_t_cya_17 
                p_cya_mort_det_diff = max(p_cya_mort_det_diff,0.0) 

                # mortality of zooplankton :
                p_zoo_mort_det  = (zoo_eff*r_zoo_mort*(1+9*theta(5.0e-6-t_o2)))*lim_t_zoo_19 
                p_zoo_mort_det  = max(p_zoo_mort_det ,0.0) 

                # nitrification :
                p_nh4_nit_no3   = (t_nh4*r_nh4_nitrif*exp(q10_nit*cgt_temp))*lim_t_nh4_11*lim_t_o2_2 
                p_nh4_nit_no3   = max(p_nh4_nit_no3  ,0.0) 

                # recycling of detritus using oxygen (respiration) :
                p_det_resp_nh4  = (t_det*r_det_rec*exp(q10_det_rec*cgt_temp))*lim_t_o2_0*lim_t_det_20 
                p_det_resp_nh4  = max(p_det_resp_nh4 ,0.0) 

                # recycling of detritus using nitrate (denitrification) :
                p_det_denit_nh4 = (t_det*r_det_rec*exp(q10_det_rec*cgt_temp))*(1.0-lim_t_o2_0)*lim_t_no3_1*lim_t_det_20 
                p_det_denit_nh4 = max(p_det_denit_nh4,0.0) 

                # recycling of detritus using sulfate (sulfate reduction) :
                p_det_sulf_nh4  = (t_det*r_det_rec*exp(q10_det_rec*cgt_temp))*(1.0-lim_t_o2_0)*(1.0-lim_t_no3_1)*lim_t_det_20 
                p_det_sulf_nh4  = max(p_det_sulf_nh4 ,0.0) 

                # oxidation of hydrogen sulfide with oxygen :
                p_h2s_oxo2_sul  = (t_h2s*t_o2*k_h2s_o2*exp(q10_h2s*cgt_temp))*lim_t_o2_2*lim_t_h2s_24 
                p_h2s_oxo2_sul  = max(p_h2s_oxo2_sul ,0.0) 

                # oxidation of hydrogen sulfide with nitrate :
                p_h2s_oxno3_sul = (t_h2s*t_no3*k_h2s_no3*exp(q10_h2s*cgt_temp))*lim_t_h2s_24*lim_t_no3_9 
                p_h2s_oxno3_sul = max(p_h2s_oxno3_sul,0.0) 

                # oxidation of elemental sulfur with oxygen :
                p_sul_oxo2_so4  = (t_sul*t_o2*k_sul_o2*exp(q10_h2s*cgt_temp))*lim_t_sul_25*lim_t_o2_2 
                p_sul_oxo2_so4  = max(p_sul_oxo2_so4 ,0.0) 

                # oxidation of elemental sulfur with nitrate :
                p_sul_oxno3_so4 = (t_sul*t_no3*k_sul_no3*exp(q10_h2s*cgt_temp))*lim_t_sul_25*lim_t_no3_9 
                p_sul_oxno3_so4 = max(p_sul_oxno3_so4,0.0) 

                # particle formation from DOC :
                p_doc2pco       = (t_doc * r_doc2poc)*lim_t_doc_29 
                p_doc2pco       = max(p_doc2pco      ,0.0) 

                # particle formation from DOP :
                p_dop2pocp      = (t_dop * r_dop2pocp)*lim_t_dop_30 
                p_dop2pocp      = max(p_dop2pocp     ,0.0) 

                # particle formation from DON :
                p_don2pocn      = (t_don * r_don2pocn)*lim_t_don_31 
                p_don2pocn      = max(p_don2pocn     ,0.0) 

                # respiration of DOC :
                p_doc_resp      = (t_doc * r_doc_rec * exp(q10_doc_rec * cgt_temp))*lim_t_o2_0*lim_t_doc_29 
                p_doc_resp      = max(p_doc_resp     ,0.0) 

                # recycling of DOC using nitrate (denitrification) :
                p_doc_denit     = (t_doc*r_doc_rec*exp(q10_det_rec*cgt_temp))*(1.0-lim_t_o2_0)*lim_t_no3_1*lim_t_doc_29 
                p_doc_denit     = max(p_doc_denit    ,0.0) 

                # Mineralization of DOC, e-acceptor sulfate (sulfate reduction) :
                p_doc_sulf      = (t_doc*r_doc_rec*exp(q10_det_rec*cgt_temp))*(1.0-lim_t_o2_0)*(1.0-lim_t_no3_1)*lim_t_doc_29 
                p_doc_sulf      = max(p_doc_sulf     ,0.0) 

                # respiration of DOP :
                p_dop_resp      = (t_dop * lr_dop * exp(q10_det_rec * cgt_temp))*lim_t_o2_0*lim_t_dop_30 
                p_dop_resp      = max(p_dop_resp     ,0.0) 

                # recycling of DOP using nitrate (denitrification) :
                p_dop_denit     = (t_dop*r_dop_rec*exp(q10_det_rec*cgt_temp))*(1.0-lim_t_o2_0)*lim_t_no3_1*lim_t_dop_30 
                p_dop_denit     = max(p_dop_denit    ,0.0) 

                # Mineralization of DOP, e-acceptor sulfate (sulfate reduction) :
                p_dop_sulf      = (t_dop*r_dop_rec*exp(q10_det_rec*cgt_temp))*(1.0-lim_t_o2_0)*(1.0-lim_t_no3_1)*lim_t_dop_30 
                p_dop_sulf      = max(p_dop_sulf     ,0.0) 

                # respiration of DON :
                p_don_resp      = (t_don * lr_don * exp(q10_det_rec * cgt_temp))*lim_t_o2_0*lim_t_don_31 
                p_don_resp      = max(p_don_resp     ,0.0) 

                # recycling of DON using nitrate (denitrification) :
                p_don_denit     = (t_don*r_don_rec*exp(q10_det_rec*cgt_temp))*(1.0-lim_t_o2_0)*lim_t_no3_1*lim_t_don_31 
                p_don_denit     = max(p_don_denit    ,0.0) 

                # Mineralization of DON, e-acceptor sulfate (sulfate reduction) :
                p_don_sulf      = (t_don*r_don_rec*exp(q10_det_rec*cgt_temp))*(1.0-lim_t_o2_0)*(1.0-lim_t_no3_1)*lim_t_don_31 
                p_don_sulf      = max(p_don_sulf     ,0.0) 

                # decay of cdom due to light :
                p_cdom_decay    = (t_cdom*r_cdom_decay*cgt_light/r_cdom_light)*lim_t_cdom_32 
                p_cdom_decay    = max(p_cdom_decay   ,0.0) 


                if (k == kmax-1):
                    cgt_dummyvar = 0.0
                    # recycling of sedimentary detritus to ammonium using oxygen (respiration) :
                    p_sed_resp_nh4  = (lr_sed_rec*sed_active)*lim_t_sed_21*lim_t_o2_2 
                    p_sed_resp_nh4  = max(p_sed_resp_nh4 ,0.0) 
                
                    # recycling of sedimentary detritus to ammonium using nitrate (denitrification) :
                    p_sed_denit_nh4 = (lr_sed_rec*sed_active)*(1.0-lim_t_o2_2)*lim_t_no3_3*lim_t_sed_21 
                    p_sed_denit_nh4 = max(p_sed_denit_nh4,0.0) 
                
                    # recycling of sedimentary detritus to ammonium using sulfate (sulfate reduction) :
                    p_sed_sulf_nh4  = (lr_sed_rec*sed_active)*(1.0-lim_t_o2_2)*(1.0-lim_t_no3_3)*lim_t_sed_21 
                    p_sed_sulf_nh4  = max(p_sed_sulf_nh4 ,0.0) 
                
                    # recycling of sedimentary poc to dic using oxygen (respiration) :
                    p_sed_poc_resp  = (lr_sed_poc_rec*poc_active)*lim_t_sed_poc_22*lim_t_o2_2 
                    p_sed_poc_resp  = max(p_sed_poc_resp ,0.0) 
                
                    # recycling of sedimentary poc to dic using nitrate (denitrification) :
                    p_sed_poc_denit = (lr_sed_poc_rec*poc_active)*(1.0-lim_t_o2_2)*lim_t_no3_3*lim_t_sed_poc_22 
                    p_sed_poc_denit = max(p_sed_poc_denit,0.0) 
                
                    # recycling of sedimentary poc to dic using sulfate (sulfate reduction) :
                    p_sed_poc_sulf  = (lr_sed_poc_rec*poc_active)*(1.0-lim_t_o2_2)*(1.0-lim_t_no3_3)*lim_t_sed_poc_22 
                    p_sed_poc_sulf  = max(p_sed_poc_sulf ,0.0) 
                
                    # retention of phosphate in the sediment under oxic conditions :
                    p_po4_retent_ips = (p_sed_resp_nh4*frac_po4retent)*lim_t_o2_4*lim_t_po4_10 
                    p_po4_retent_ips = max(p_po4_retent_ips,0.0) 
                
                    # liberation of phosphate from the sediment under anoxic conditions :
                    p_ips_liber_po4 = (t_ips*r_ips_liber)*lim_t_h2s_5*lim_t_ips_23 
                    p_ips_liber_po4 = max(p_ips_liber_po4,0.0) 
                
                    # detritus sedimentation :
                    p_det_sedi_sed  = ((1.0-erosion_is_active)*(0.0-w_det_sedi)*t_det*cgt_density)*lim_t_det_20 
                    p_det_sedi_sed  = max(p_det_sedi_sed ,0.0) 
                
                    # sedimentation of iron PO4 :
                    p_ipw_sedi_ips  = ((1.0-erosion_is_active)*(0.0-w_ipw_sedi)*t_ipw*cgt_density)*lim_t_ipw_26 
                    p_ipw_sedi_ips  = max(p_ipw_sedi_ips ,0.0) 
                
                    # poc sedimentation :
                    p_poc_sedi_sed  = ((1.0-erosion_is_active)*(0.0-w_poc_var)*t_poc*cgt_density)*lim_t_poc_12 
                    p_poc_sedi_sed  = max(p_poc_sedi_sed ,0.0) 
                
                    # pocn sedimentation :
                    p_pocn_sedi_sed = ((1.0-erosion_is_active)*(0.0-w_pocn_sedi)*t_pocn*cgt_density)*lim_t_pocn_14 
                    p_pocn_sedi_sed = max(p_pocn_sedi_sed,0.0) 
                
                    # pocp sedimentation :
                    p_pocp_sedi_sed = ((1.0-erosion_is_active)*(0.0-w_pocp_sedi)*t_pocp*cgt_density)*lim_t_pocp_13 
                    p_pocp_sedi_sed = max(p_pocp_sedi_sed,0.0) 
                
                    # sedimentary detritus erosion :
                    p_sed_ero_det   = (erosion_is_active*r_sed_ero*sed_active)*lim_t_sed_21 
                    p_sed_ero_det   = max(p_sed_ero_det  ,0.0) 
                
                    # erosion of iron PO4 :
                    p_ips_ero_ipw   = (erosion_is_active*r_ips_ero*t_ips)*lim_t_ips_23 
                    p_ips_ero_ipw   = max(p_ips_ero_ipw  ,0.0) 
                
                    # sedimentary poc erosion :
                    p_sed_ero_poc   = (erosion_is_active*r_sed_ero*poc_active)*lim_t_sed_poc_22 
                    p_sed_ero_poc   = max(p_sed_ero_poc  ,0.0) 
                
                    # sedimentary pocn erosion :
                    p_sed_ero_pocn  = (erosion_is_active*r_sed_ero*pocn_active)*lim_t_sed_pocn_27 
                    p_sed_ero_pocn  = max(p_sed_ero_pocn ,0.0) 
                
                    # sedimentary pocp erosion :
                    p_sed_ero_pocp  = (erosion_is_active*r_sed_ero*pocp_active)*lim_t_sed_pocp_28 
                    p_sed_ero_pocp  = max(p_sed_ero_pocp ,0.0) 
                
                    # bio resuspension of sedimentary detritus :
                    p_sed_biores_det = (r_biores*exp(-0.02*cgt_bottomdepth)*sed_active)*lim_t_o2_6*lim_t_sed_21 
                    p_sed_biores_det = max(p_sed_biores_det,0.0) 
                
                    # bio resuspension of iron PO4 :
                    p_ips_biores_ipw = (r_biores*exp(-0.02*cgt_bottomdepth)*t_ips)*lim_t_o2_6*lim_t_ips_23 
                    p_ips_biores_ipw = max(p_ips_biores_ipw,0.0) 
                
                    # bio resuspension of sedimentary poc :
                    p_sed_biores_poc = (r_biores*exp(-0.02*cgt_bottomdepth)*poc_active)*lim_t_o2_6*lim_t_sed_poc_22 
                    p_sed_biores_poc = max(p_sed_biores_poc,0.0) 
                
                    # bio resuspension of sedimentary pocn :
                    p_sed_biores_pocn = (r_biores*exp(-0.02*cgt_bottomdepth)*pocn_active)*lim_t_o2_6*lim_t_sed_pocn_27 
                    p_sed_biores_pocn = max(p_sed_biores_pocn,0.0) 
                
                    # bio resuspension of sedimentary pocp :
                    p_sed_biores_pocp = (r_biores*exp(-0.02*cgt_bottomdepth)*pocp_active)*lim_t_o2_6*lim_t_sed_pocp_28 
                    p_sed_biores_pocp = max(p_sed_biores_pocp,0.0) 
                
                    # burial of detritus deeper than max_sed :
                    p_sed_burial    = ((sed_tot-sed_tot_burial)/cgt_timestep*t_sed/sed_tot)*lim_t_sed_21 
                    p_sed_burial    = max(p_sed_burial   ,0.0) 
                
                    # burial of iron PO4 :
                    p_ips_burial    = (fac_ips_burial*(sed_tot-sed_tot_burial)/cgt_timestep*t_ips/sed_tot)*lim_t_ips_23 
                    p_ips_burial    = max(p_ips_burial   ,0.0) 
                
                    # burial of poc deeper than max_sed :
                    p_poc_burial    = ((sed_tot-sed_tot_burial)/cgt_timestep*t_sed_poc/sed_tot)*lim_t_sed_poc_22 
                    p_poc_burial    = max(p_poc_burial   ,0.0) 
                
                    # burial of pocn deeper than max_sed :
                    p_pocn_burial   = ((sed_tot-sed_tot_burial)/cgt_timestep*t_sed_pocn/sed_tot)*lim_t_sed_pocn_27 
                    p_pocn_burial   = max(p_pocn_burial  ,0.0) 
                
                    # burial of pocp deeper than max_sed :
                    p_pocp_burial   = ((sed_tot-sed_tot_burial)/cgt_timestep*t_sed_pocp/sed_tot)*lim_t_sed_pocp_28 
                    p_pocp_burial   = max(p_pocp_burial  ,0.0) 
                
                    # recycling of sedimentary pocn to dic and NH4 using oxygen (respiration) :
                    p_sed_pocn_resp = (lr_sed_rec*pocn_active)*lim_t_o2_2*lim_t_sed_pocn_27 
                    p_sed_pocn_resp = max(p_sed_pocn_resp,0.0) 
                
                    # recycling of sedimentary pocp to dic and PO4 using oxygen (respiration) :
                    p_sed_pocp_resp = (lr_sed_rec*pocp_active)*lim_t_sed_pocp_28*lim_t_o2_2 
                    p_sed_pocp_resp = max(p_sed_pocp_resp,0.0) 
                
                    # recycling of sedimentary pocn to dic and NH4 using nitrate (denitrification) :
                    p_sed_pocn_denit = (lr_sed_rec*pocn_active)*(1.0-lim_t_o2_2)*lim_t_no3_3*lim_t_sed_pocn_27 
                    p_sed_pocn_denit = max(p_sed_pocn_denit,0.0) 
                
                    # recycling of sedimentary pocp to dic and PO4 using nitrate (denitrification) :
                    p_sed_pocp_denit = (lr_sed_rec*pocp_active)*(1.0-lim_t_o2_2)*lim_t_no3_3*lim_t_sed_pocp_28 
                    p_sed_pocp_denit = max(p_sed_pocp_denit,0.0) 
                
                    # recycling of sedimentary pocn to dic and NH4 using sulfate (sulfate reduction) :
                    p_sed_pocn_sulf = (lr_sed_rec*pocn_active)*(1.0-lim_t_o2_2)*(1.0-lim_t_no3_3)*lim_t_pocn_14 
                    p_sed_pocn_sulf = max(p_sed_pocn_sulf,0.0) 
                
                    # recycling of sedimentary pocp to dic and PO4 using sulfate (sulfate reduction) :
                    p_sed_pocp_sulf = (lr_sed_rec*pocp_active)*(1.0-lim_t_o2_2)*(1.0-lim_t_no3_3)*lim_t_pocp_13 
                    p_sed_pocp_sulf = max(p_sed_pocp_sulf,0.0) 
                
                    # calcium carbonate dissolution from till sediments :
                    p_alk_btf       = alk_btf_0 * (alk_btf_sw_BS + alk_btf_0_BBfac*alk_btf_sw_BB) 
                    p_alk_btf       = max(p_alk_btf      ,0.0) 
                
                    # coupled nitrification and denitrification after mineralization of detritus in oxic sediments :
                    p_nh4_nitdenit_n2 = (frac_denit_sed*(p_sed_resp_nh4+p_sed_pocn_resp)*theta(t_o2-5.0e-6))*lim_t_o2_2*lim_t_nh4_11 
                    p_nh4_nitdenit_n2 = max(p_nh4_nitdenit_n2,0.0) 
                
                 
             
                if (k == 0):
                    cgt_dummyvar = 0.0
                    # downward nitrogen flux through the surface :
                    p_n2_stf_down   = w_n2_stf*(n2_sat-t_n2)*theta(n2_sat-t_n2)*cgt_density 
                    p_n2_stf_down   = max(p_n2_stf_down  ,0.0) 
                
                    # upward nitrogen flux through the surface :
                    p_n2_stf_up     = (w_n2_stf*(t_n2-n2_sat)*theta(t_n2-n2_sat)*cgt_density)*lim_t_n2_7 
                    p_n2_stf_up     = max(p_n2_stf_up    ,0.0) 
                
                    # downward oxygen flux through the surface :
                    p_o2_stf_down   = w_o2_stf*(o2_sat-t_o2)*theta(o2_sat-t_o2)*cgt_density 
                    p_o2_stf_down   = max(p_o2_stf_down  ,0.0) 
                
                    # upward oxygen flux through the surface :
                    p_o2_stf_up     = (w_o2_stf*(t_o2-o2_sat)*theta(t_o2-o2_sat)*cgt_density)*lim_t_o2_2 
                    p_o2_stf_up     = max(p_o2_stf_up    ,0.0) 
                
                    # downward co2 flux through the surface :
                    p_co2_stf_down  = w_co2_stf*(patm_co2-pco2)*k0_co2*theta(patm_co2-pco2)*cgt_density 
                    p_co2_stf_down  = max(p_co2_stf_down ,0.0) 
                
                    # upward co2 flux through the surface :
                    p_co2_stf_up    = (w_co2_stf*(pco2-patm_co2)*k0_co2*theta(pco2-patm_co2)*cgt_density)*lim_t_dic_8 
                    p_co2_stf_up    = max(p_co2_stf_up   ,0.0) 
                
                 

                #------------------------------------
                # STEP 6.2: calculate possible euler-forward change (in a full timestep)
                #------------------------------------

                change_of_t_n2            = 0.0 
                change_of_t_o2            = 0.0 
                change_of_t_dic           = 0.0 
                change_of_t_nh4           = 0.0 
                change_of_t_no3           = 0.0 
                change_of_t_po4           = 0.0 
                change_of_t_spp           = 0.0 
                change_of_t_zoo           = 0.0 
                change_of_t_h2s           = 0.0 
                change_of_t_sul           = 0.0 
                change_of_t_alk           = 0.0 
                change_of_t_sed           = 0.0 
                change_of_t_ips           = 0.0 
                change_of_t_lip           = 0.0 
                change_of_t_doc           = 0.0 
                change_of_t_dop           = 0.0 
                change_of_t_don           = 0.0 
                change_of_t_sed_poc       = 0.0 
                change_of_t_sed_pocn      = 0.0 
                change_of_t_sed_pocp      = 0.0 
                change_of_t_cdom          = 0.0 
                change_of_t_cya           = 0.0 
                change_of_t_det           = 0.0 
                change_of_t_poc           = 0.0 
                change_of_t_pocp          = 0.0 
                change_of_t_pocn          = 0.0 
                change_of_t_lpp           = 0.0 
                change_of_t_ipw           = 0.0 

             
                change_of_t_n2            = change_of_t_n2            + cgt_timestep*(0.0 
                    + (p_poc_denit)*(0.4)            # recycling of POC using nitrate (denitrification)
                    + (p_pocp_denit)*(42.4)          # recycling of POC using nitrate (denitrification)
                    + (p_pocn_denit)*(2.65)          # recycling of POCN using nitrate (denitrification)
                    + (p_det_denit_nh4)*(2.65)       # recycling of detritus using nitrate (denitrification)
                    + (p_h2s_oxno3_sul)*(0.2)        # oxidation of hydrogen sulfide with nitrate
                    + (p_sul_oxno3_so4)*(0.6)        # oxidation of elemental sulfur with nitrate
                    + (p_doc_denit)*(0.4)            # recycling of DOC using nitrate (denitrification)
                    + (p_dop_denit)*(42.4)           # recycling of DOP using nitrate (denitrification)
                    + (p_don_denit)*(2.65)           # recycling of DON using nitrate (denitrification)
                    - (p_n2_assim_cya)*(0.5)         # fixation of dinitrogen by diazotroph cyanobacteria
                ) 
             
                change_of_t_o2            = change_of_t_o2            + cgt_timestep*(0.0 
                    + (p_no3_assim_lpp)*(8.625)      # assimilation of nitrate by large-cell phytoplankton
                    + (p_nh4_assim_lpp)*(6.625)      # assimilation of ammonium by large-cell phytoplankton
                    + (p_no3_assim_spp)*(8.625)      # assimilation of nitrate by small-cell phytoplankton
                    + (p_nh4_assim_spp)*(6.625)      # assimilation of ammonium by small-cell phytoplankton
                    + (p_nh4_assim_lip)*(6.625)      # assimilation of ammonium by limnic phytoplankton
                    + (p_no3_assim_lip)*(8.625)      # assimilation of nitrate by limnic phytoplankton
                    + (p_n2_assim_cya)*(7.375)       # fixation of dinitrogen by diazotroph cyanobacteria
                    + p_assim_lpp_doc                # Production of DOC by LIP
                    + p_assim_spp_doc                # Production of DOC by SPP
                    + p_assim_lip_doc                # Production of DOC by LPP
                    + p_assim_cya_doc                # Production of DOC by CYA
                    + (p_assim_lpp_dop)*(106)        # Production of DOP by LPP
                    + (p_assim_spp_dop)*(106)        # Production of DOP by SPP
                    + (p_assim_lip_dop)*(106)        # Production of DOP by LIP
                    + (p_nh4_assim_lpp_don)*(6.625)   # Production of DON by LPP
                    + (p_no3_assim_lpp_don)*(8.625)   # Production of DON by LPP
                    + (p_nh4_assim_spp_don)*(6.625)   # Production of DON by SPP
                    + (p_no3_assim_spp_don)*(8.625)   # Production of DON by SPP
                    + (p_nh4_assim_lip_don)*(6.625)   # Production of DON by LIP
                    + (p_no3_assim_lip_don)*(8.625)   # Production of DON by LIP
                    - p_poc_resp                     # respiration of POC
                    - (p_pocp_resp)*(106)            # respiration of POCP
                    - (p_pocn_resp)*(6.625)          # respiration of POCN
                    - (p_lpp_resp_nh4)*(6.625)       # respiration of large-cell phytoplankton
                    - (p_spp_resp_nh4)*(6.625)       # respiration of small-cell phytoplankton
                    - (p_lip_resp_nh4)*(6.625)       # respiration of limnic phytoplankton
                    - (p_cya_resp_nh4)*(6.625)       # respiration of diazotroph cyanobacteria
                    - (p_zoo_resp_nh4)*(6.625)       # respiration of zooplankton
                    - (p_nh4_nit_no3)*(2)            # nitrification
                    - (p_det_resp_nh4)*(6.625)       # recycling of detritus using oxygen (respiration)
                    - (p_h2s_oxo2_sul)*(0.5)         # oxidation of hydrogen sulfide with oxygen
                    - (p_sul_oxo2_so4)*(1.5)         # oxidation of elemental sulfur with oxygen
                    - p_doc_resp                     # respiration of DOC
                    - (p_dop_resp)*(106)             # respiration of DOP
                    - (p_don_resp)*(6.625)           # respiration of DON
                ) 
             
                change_of_t_dic           = change_of_t_dic           + cgt_timestep*(0.0 
                    + p_poc_resp                     # respiration of POC
                    + p_poc_denit                    # recycling of POC using nitrate (denitrification)
                    + p_poc_sulf                     # Mineralization of POC, e-acceptor sulfate (sulfate reduction)
                    + (p_pocp_resp)*(106)            # respiration of POCP
                    + (p_pocp_denit)*(106)           # recycling of POC using nitrate (denitrification)
                    + (p_pocp_sulf)*(106)            # Mineralization of POC, e-acceptor sulfate (sulfate reduction)
                    + (p_pocn_resp)*(6.625)          # respiration of POCN
                    + (p_pocn_denit)*(6.625)         # recycling of POCN using nitrate (denitrification)
                    + (p_pocn_sulf)*(6.625)          # Mineralization of POCN, e-acceptor sulfate (sulfate reduction)
                    + (p_lpp_resp_nh4)*(rfr_c)       # respiration of large-cell phytoplankton
                    + (p_spp_resp_nh4)*(rfr_c)       # respiration of small-cell phytoplankton
                    + (p_lip_resp_nh4)*(rfr_c)       # respiration of limnic phytoplankton
                    + (p_cya_resp_nh4)*(rfr_c)       # respiration of diazotroph cyanobacteria
                    + (p_zoo_resp_nh4)*(rfr_c)       # respiration of zooplankton
                    + (p_det_resp_nh4)*(rfr_c)       # recycling of detritus using oxygen (respiration)
                    + (p_det_denit_nh4)*(rfr_c)      # recycling of detritus using nitrate (denitrification)
                    + (p_det_sulf_nh4)*(rfr_c)       # recycling of detritus using sulfate (sulfate reduction)
                    + p_doc_resp                     # respiration of DOC
                    + p_doc_denit                    # recycling of DOC using nitrate (denitrification)
                    + p_doc_sulf                     # Mineralization of DOC, e-acceptor sulfate (sulfate reduction)
                    + (p_dop_resp)*(106)             # respiration of DOP
                    + (p_dop_denit)*(106)            # recycling of DOP using nitrate (denitrification)
                    + (p_dop_sulf)*(106)             # Mineralization of DOP, e-acceptor sulfate (sulfate reduction)
                    + (p_don_resp)*(6.625)           # respiration of DON
                    + (p_don_denit)*(6.625)          # recycling of DON using nitrate (denitrification)
                    + (p_don_sulf)*(6.625)           # Mineralization of DON, e-acceptor sulfate (sulfate reduction)
                    - (p_no3_assim_lpp)*(rfr_c)      # assimilation of nitrate by large-cell phytoplankton
                    - (p_nh4_assim_lpp)*(rfr_c)      # assimilation of ammonium by large-cell phytoplankton
                    - (p_no3_assim_spp)*(rfr_c)      # assimilation of nitrate by small-cell phytoplankton
                    - (p_nh4_assim_spp)*(rfr_c)      # assimilation of ammonium by small-cell phytoplankton
                    - (p_nh4_assim_lip)*(rfr_c)      # assimilation of ammonium by limnic phytoplankton
                    - (p_no3_assim_lip)*(rfr_c)      # assimilation of nitrate by limnic phytoplankton
                    - (p_n2_assim_cya)*(rfr_c)       # fixation of dinitrogen by diazotroph cyanobacteria
                    - p_assim_lpp_doc                # Production of DOC by LIP
                    - p_assim_spp_doc                # Production of DOC by SPP
                    - p_assim_lip_doc                # Production of DOC by LPP
                    - p_assim_cya_doc                # Production of DOC by CYA
                    - (p_assim_lpp_dop)*(106)        # Production of DOP by LPP
                    - (p_assim_spp_dop)*(106)        # Production of DOP by SPP
                    - (p_assim_lip_dop)*(106)        # Production of DOP by LIP
                    - (p_nh4_assim_lpp_don)*(rfr_c)   # Production of DON by LPP
                    - (p_no3_assim_lpp_don)*(rfr_c)   # Production of DON by LPP
                    - (p_nh4_assim_spp_don)*(rfr_c)   # Production of DON by SPP
                    - (p_no3_assim_spp_don)*(rfr_c)   # Production of DON by SPP
                    - (p_nh4_assim_lip_don)*(rfr_c)   # Production of DON by LIP
                    - (p_no3_assim_lip_don)*(rfr_c)   # Production of DON by LIP
                ) 
             
                change_of_t_nh4           = change_of_t_nh4           + cgt_timestep*(0.0 
                    + p_pocn_resp                    # respiration of POCN
                    + p_pocn_denit                   # recycling of POCN using nitrate (denitrification)
                    + p_pocn_sulf                    # Mineralization of POCN, e-acceptor sulfate (sulfate reduction)
                    + (p_lpp_resp_nh4)*((1-don_fraction))   # respiration of large-cell phytoplankton
                    + (p_spp_resp_nh4)*((1-don_fraction))   # respiration of small-cell phytoplankton
                    + (p_lip_resp_nh4)*((1-don_fraction))   # respiration of limnic phytoplankton
                    + (p_cya_resp_nh4)*((1-don_fraction))   # respiration of diazotroph cyanobacteria
                    + (p_zoo_resp_nh4)*((1-don_fraction))   # respiration of zooplankton
                    + p_det_resp_nh4                 # recycling of detritus using oxygen (respiration)
                    + p_det_denit_nh4                # recycling of detritus using nitrate (denitrification)
                    + p_det_sulf_nh4                 # recycling of detritus using sulfate (sulfate reduction)
                    + p_don_resp                     # respiration of DON
                    + p_don_denit                    # recycling of DON using nitrate (denitrification)
                    + p_don_sulf                     # Mineralization of DON, e-acceptor sulfate (sulfate reduction)
                    - p_nh4_assim_lpp                # assimilation of ammonium by large-cell phytoplankton
                    - p_nh4_assim_spp                # assimilation of ammonium by small-cell phytoplankton
                    - p_nh4_assim_lip                # assimilation of ammonium by limnic phytoplankton
                    - p_nh4_assim_lpp_don            # Production of DON by LPP
                    - p_nh4_assim_spp_don            # Production of DON by SPP
                    - p_nh4_assim_lip_don            # Production of DON by LIP
                    - p_nh4_nit_no3                  # nitrification
                ) 
             
                change_of_t_no3           = change_of_t_no3           + cgt_timestep*(0.0 
                    + p_nh4_nit_no3                  # nitrification
                    - p_no3_assim_lpp                # assimilation of nitrate by large-cell phytoplankton
                    - p_no3_assim_spp                # assimilation of nitrate by small-cell phytoplankton
                    - p_no3_assim_lip                # assimilation of nitrate by limnic phytoplankton
                    - p_no3_assim_lpp_don            # Production of DON by LPP
                    - p_no3_assim_spp_don            # Production of DON by SPP
                    - p_no3_assim_lip_don            # Production of DON by LIP
                    - (p_poc_denit)*(0.8)            # recycling of POC using nitrate (denitrification)
                    - (p_pocp_denit)*(84.8)          # recycling of POC using nitrate (denitrification)
                    - (p_pocn_denit)*(5.3)           # recycling of POCN using nitrate (denitrification)
                    - (p_det_denit_nh4)*(5.3)        # recycling of detritus using nitrate (denitrification)
                    - (p_h2s_oxno3_sul)*(0.4)        # oxidation of hydrogen sulfide with nitrate
                    - (p_sul_oxno3_so4)*(1.2)        # oxidation of elemental sulfur with nitrate
                    - (p_doc_denit)*(0.8)            # recycling of DOC using nitrate (denitrification)
                    - (p_dop_denit)*(84.8)           # recycling of DOP using nitrate (denitrification)
                    - (p_don_denit)*(5.3)            # recycling of DON using nitrate (denitrification)
                ) 
             
                change_of_t_po4           = change_of_t_po4           + cgt_timestep*(0.0 
                    + p_pocp_resp                    # respiration of POCP
                    + p_pocp_denit                   # recycling of POC using nitrate (denitrification)
                    + p_pocp_sulf                    # Mineralization of POC, e-acceptor sulfate (sulfate reduction)
                    + (p_lpp_resp_nh4)*(rfr_p)       # respiration of large-cell phytoplankton
                    + (p_spp_resp_nh4)*(rfr_p)       # respiration of small-cell phytoplankton
                    + (p_lip_resp_nh4)*(rfr_p)       # respiration of limnic phytoplankton
                    + (p_cya_resp_nh4)*(rfr_p)       # respiration of diazotroph cyanobacteria
                    + (p_zoo_resp_nh4)*(rfr_p)       # respiration of zooplankton
                    + (p_det_resp_nh4)*(rfr_p)       # recycling of detritus using oxygen (respiration)
                    + (p_det_denit_nh4)*(rfr_p)      # recycling of detritus using nitrate (denitrification)
                    + (p_det_sulf_nh4)*(rfr_p)       # recycling of detritus using sulfate (sulfate reduction)
                    + p_dop_resp                     # respiration of DOP
                    + p_dop_denit                    # recycling of DOP using nitrate (denitrification)
                    + p_dop_sulf                     # Mineralization of DOP, e-acceptor sulfate (sulfate reduction)
                    - (p_no3_assim_lpp)*(rfr_p)      # assimilation of nitrate by large-cell phytoplankton
                    - (p_nh4_assim_lpp)*(rfr_p)      # assimilation of ammonium by large-cell phytoplankton
                    - (p_no3_assim_spp)*(rfr_p)      # assimilation of nitrate by small-cell phytoplankton
                    - (p_nh4_assim_spp)*(rfr_p)      # assimilation of ammonium by small-cell phytoplankton
                    - (p_nh4_assim_lip)*(rfr_p)      # assimilation of ammonium by limnic phytoplankton
                    - (p_no3_assim_lip)*(rfr_p)      # assimilation of nitrate by limnic phytoplankton
                    - (p_n2_assim_cya)*(rfr_p)       # fixation of dinitrogen by diazotroph cyanobacteria
                    - p_assim_lpp_dop                # Production of DOP by LPP
                    - p_assim_spp_dop                # Production of DOP by SPP
                    - p_assim_lip_dop                # Production of DOP by LIP
                ) 
             
                change_of_t_spp           = change_of_t_spp           + cgt_timestep*(0.0 
                    + p_no3_assim_spp                # assimilation of nitrate by small-cell phytoplankton
                    + p_nh4_assim_spp                # assimilation of ammonium by small-cell phytoplankton
                    - p_spp_graz_zoo                 # grazing of zooplankton eating small-cell phytoplankton
                    - p_spp_resp_nh4                 # respiration of small-cell phytoplankton
                    - p_spp_mort_det                 # mortality of small-scale phytoplankton
                ) 
             
                change_of_t_zoo           = change_of_t_zoo           + cgt_timestep*(0.0 
                    + p_lpp_graz_zoo                 # grazing of zooplankton eating large-cell phytoplankton
                    + p_spp_graz_zoo                 # grazing of zooplankton eating small-cell phytoplankton
                    + p_cya_graz_zoo                 # grazing of zooplankton eating diazotroph cyanobacteria
                    + p_lip_graz_zoo                 # grazing of zooplankton eating limnic phytoplankton
                    - p_zoo_resp_nh4                 # respiration of zooplankton
                    - p_zoo_mort_det                 # mortality of zooplankton
                ) 
             
                change_of_t_h2s           = change_of_t_h2s           + cgt_timestep*(0.0 
                    + (p_poc_sulf)*(0.5)             # Mineralization of POC, e-acceptor sulfate (sulfate reduction)
                    + (p_pocp_sulf)*(53)             # Mineralization of POC, e-acceptor sulfate (sulfate reduction)
                    + (p_pocn_sulf)*(3.3125)         # Mineralization of POCN, e-acceptor sulfate (sulfate reduction)
                    + (p_det_sulf_nh4)*(3.3125)      # recycling of detritus using sulfate (sulfate reduction)
                    + (p_doc_sulf)*(0.5)             # Mineralization of DOC, e-acceptor sulfate (sulfate reduction)
                    + (p_dop_sulf)*(53)              # Mineralization of DOP, e-acceptor sulfate (sulfate reduction)
                    + (p_don_sulf)*(3.3125)          # Mineralization of DON, e-acceptor sulfate (sulfate reduction)
                    - p_h2s_oxo2_sul                 # oxidation of hydrogen sulfide with oxygen
                    - p_h2s_oxno3_sul                # oxidation of hydrogen sulfide with nitrate
                ) 
             
                change_of_t_sul           = change_of_t_sul           + cgt_timestep*(0.0 
                    + p_h2s_oxo2_sul                 # oxidation of hydrogen sulfide with oxygen
                    + p_h2s_oxno3_sul                # oxidation of hydrogen sulfide with nitrate
                    - p_sul_oxo2_so4                 # oxidation of elemental sulfur with oxygen
                    - p_sul_oxno3_so4                # oxidation of elemental sulfur with nitrate
                ) 
             
                change_of_t_alk           = change_of_t_alk           + cgt_timestep*(0.0 
                    + (1)*(p_pocn_resp)*(0.5)        # respiration of POCN (produces ohminus)
                    + (1)*(p_pocn_denit)*(0.5)       # recycling of POCN using nitrate (denitrification) (produces ohminus)
                    + (1)*(p_pocn_sulf)*(0.5)        # Mineralization of POCN, e-acceptor sulfate (sulfate reduction) (produces ohminus)
                    + (1)*(p_don_resp)*(0.5)         # respiration of DON (produces ohminus)
                    + (1)*(p_don_denit)*(0.5)        # recycling of DON using nitrate (denitrification) (produces ohminus)
                    + (1)*(p_don_sulf)*(0.5)         # Mineralization of DON, e-acceptor sulfate (sulfate reduction) (produces ohminus)
                    - (1)*(p_nh4_assim_lpp_don)      # Production of DON by LPP (consumes ohminus)
                    - (1)*(p_nh4_assim_spp_don)      # Production of DON by SPP (consumes ohminus)
                    - (1)*(p_nh4_assim_lip_don)      # Production of DON by LIP (consumes ohminus)
                    - (1)*(p_pocp_denit)*(3)         # recycling of POC using nitrate (denitrification) (consumes ohminus)
                    - (1)*(p_pocp_sulf)*(3)          # Mineralization of POC, e-acceptor sulfate (sulfate reduction) (consumes ohminus)
                    - (1)*(p_dop_denit)*(3)          # recycling of DOP using nitrate (denitrification) (consumes ohminus)
                    - (1)*(p_dop_sulf)*(3)           # Mineralization of DOP, e-acceptor sulfate (sulfate reduction) (consumes ohminus)
                    + (-1)*(p_nh4_assim_lpp)*(0.8125)   # assimilation of ammonium by large-cell phytoplankton (produces h3oplus)
                    + (-1)*(p_nh4_assim_spp)*(0.8125)   # assimilation of ammonium by small-cell phytoplankton (produces h3oplus)
                    + (-1)*(p_nh4_assim_lip)*(0.8125)   # assimilation of ammonium by limnic phytoplankton (produces h3oplus)
                    + (-1)*(p_pocp_resp)*(3)         # respiration of POCP (produces h3oplus)
                    + (-1)*(p_nh4_nit_no3)*(2)       # nitrification (produces h3oplus)
                    + (-1)*(p_sul_oxo2_so4)*(2)      # oxidation of elemental sulfur with oxygen (produces h3oplus)
                    + (-1)*(p_sul_oxno3_so4)*(0.8)   # oxidation of elemental sulfur with nitrate (produces h3oplus)
                    + (-1)*(p_dop_resp)*(3)          # respiration of DOP (produces h3oplus)
                    - (-1)*(p_no3_assim_lpp)*(1.1875)   # assimilation of nitrate by large-cell phytoplankton (consumes h3oplus)
                    - (-1)*(p_no3_assim_spp)*(1.1875)   # assimilation of nitrate by small-cell phytoplankton (consumes h3oplus)
                    - (-1)*(p_no3_assim_lip)*(1.1875)   # assimilation of nitrate by limnic phytoplankton (consumes h3oplus)
                    - (-1)*(p_n2_assim_cya)*(3*rfr_p)   # fixation of dinitrogen by diazotroph cyanobacteria (consumes h3oplus)
                    - (-1)*(p_assim_lpp_dop)*(3)     # Production of DOP by LPP (consumes h3oplus)
                    - (-1)*(p_assim_spp_dop)*(3)     # Production of DOP by SPP (consumes h3oplus)
                    - (-1)*(p_assim_lip_dop)*(3)     # Production of DOP by LIP (consumes h3oplus)
                    - (-1)*(p_no3_assim_lpp_don)     # Production of DON by LPP (consumes h3oplus)
                    - (-1)*(p_no3_assim_spp_don)     # Production of DON by SPP (consumes h3oplus)
                    - (-1)*(p_no3_assim_lip_don)     # Production of DON by LIP (consumes h3oplus)
                    - (-1)*(p_poc_denit)*(0.8)       # recycling of POC using nitrate (denitrification) (consumes h3oplus)
                    - (-1)*(p_poc_sulf)              # Mineralization of POC, e-acceptor sulfate (sulfate reduction) (consumes h3oplus)
                    - (-1)*(p_pocp_denit)*(84.8)     # recycling of POC using nitrate (denitrification) (consumes h3oplus)
                    - (-1)*(p_pocp_sulf)*(106)       # Mineralization of POC, e-acceptor sulfate (sulfate reduction) (consumes h3oplus)
                    - (-1)*(p_pocn_resp)*(0.5)       # respiration of POCN (consumes h3oplus)
                    - (-1)*(p_pocn_denit)*(5.8)      # recycling of POCN using nitrate (denitrification) (consumes h3oplus)
                    - (-1)*(p_pocn_sulf)*(7.125)     # Mineralization of POCN, e-acceptor sulfate (sulfate reduction) (consumes h3oplus)
                    - (-1)*(p_lpp_resp_nh4)*(0.8125)   # respiration of large-cell phytoplankton (consumes h3oplus)
                    - (-1)*(p_spp_resp_nh4)*(0.8125)   # respiration of small-cell phytoplankton (consumes h3oplus)
                    - (-1)*(p_lip_resp_nh4)*(0.8125)   # respiration of limnic phytoplankton (consumes h3oplus)
                    - (-1)*(p_cya_resp_nh4)*(0.8125)   # respiration of diazotroph cyanobacteria (consumes h3oplus)
                    - (-1)*(p_zoo_resp_nh4)*(0.8125)   # respiration of zooplankton (consumes h3oplus)
                    - (-1)*(p_det_resp_nh4)*(0.8125)   # recycling of detritus using oxygen (respiration) (consumes h3oplus)
                    - (-1)*(p_det_denit_nh4)*(6.1125)   # recycling of detritus using nitrate (denitrification) (consumes h3oplus)
                    - (-1)*(p_det_sulf_nh4)*(7.4375)   # recycling of detritus using sulfate (sulfate reduction) (consumes h3oplus)
                    - (-1)*(p_h2s_oxno3_sul)*(0.4)   # oxidation of hydrogen sulfide with nitrate (consumes h3oplus)
                    - (-1)*(p_doc_denit)*(0.8)       # recycling of DOC using nitrate (denitrification) (consumes h3oplus)
                    - (-1)*(p_doc_sulf)              # Mineralization of DOC, e-acceptor sulfate (sulfate reduction) (consumes h3oplus)
                    - (-1)*(p_dop_denit)*(84.8)      # recycling of DOP using nitrate (denitrification) (consumes h3oplus)
                    - (-1)*(p_dop_sulf)*(106)        # Mineralization of DOP, e-acceptor sulfate (sulfate reduction) (consumes h3oplus)
                    - (-1)*(p_don_resp)*(0.5)        # respiration of DON (consumes h3oplus)
                    - (-1)*(p_don_denit)*(5.8)       # recycling of DON using nitrate (denitrification) (consumes h3oplus)
                    - (-1)*(p_don_sulf)*(7.125)      # Mineralization of DON, e-acceptor sulfate (sulfate reduction) (consumes h3oplus)
                    + (2)*(p_pocp_resp)              # respiration of POCP (produces t_po4)
                    + (2)*(p_pocp_denit)             # recycling of POC using nitrate (denitrification) (produces t_po4)
                    + (2)*(p_pocp_sulf)              # Mineralization of POC, e-acceptor sulfate (sulfate reduction) (produces t_po4)
                    + (2)*(p_lpp_resp_nh4)*(rfr_p)   # respiration of large-cell phytoplankton (produces t_po4)
                    + (2)*(p_spp_resp_nh4)*(rfr_p)   # respiration of small-cell phytoplankton (produces t_po4)
                    + (2)*(p_lip_resp_nh4)*(rfr_p)   # respiration of limnic phytoplankton (produces t_po4)
                    + (2)*(p_cya_resp_nh4)*(rfr_p)   # respiration of diazotroph cyanobacteria (produces t_po4)
                    + (2)*(p_zoo_resp_nh4)*(rfr_p)   # respiration of zooplankton (produces t_po4)
                    + (2)*(p_det_resp_nh4)*(rfr_p)   # recycling of detritus using oxygen (respiration) (produces t_po4)
                    + (2)*(p_det_denit_nh4)*(rfr_p)   # recycling of detritus using nitrate (denitrification) (produces t_po4)
                    + (2)*(p_det_sulf_nh4)*(rfr_p)   # recycling of detritus using sulfate (sulfate reduction) (produces t_po4)
                    + (2)*(p_dop_resp)               # respiration of DOP (produces t_po4)
                    + (2)*(p_dop_denit)              # recycling of DOP using nitrate (denitrification) (produces t_po4)
                    + (2)*(p_dop_sulf)               # Mineralization of DOP, e-acceptor sulfate (sulfate reduction) (produces t_po4)
                    - (2)*(p_no3_assim_lpp)*(rfr_p)   # assimilation of nitrate by large-cell phytoplankton (consumes t_po4)
                    - (2)*(p_nh4_assim_lpp)*(rfr_p)   # assimilation of ammonium by large-cell phytoplankton (consumes t_po4)
                    - (2)*(p_no3_assim_spp)*(rfr_p)   # assimilation of nitrate by small-cell phytoplankton (consumes t_po4)
                    - (2)*(p_nh4_assim_spp)*(rfr_p)   # assimilation of ammonium by small-cell phytoplankton (consumes t_po4)
                    - (2)*(p_nh4_assim_lip)*(rfr_p)   # assimilation of ammonium by limnic phytoplankton (consumes t_po4)
                    - (2)*(p_no3_assim_lip)*(rfr_p)   # assimilation of nitrate by limnic phytoplankton (consumes t_po4)
                    - (2)*(p_n2_assim_cya)*(rfr_p)   # fixation of dinitrogen by diazotroph cyanobacteria (consumes t_po4)
                    - (2)*(p_assim_lpp_dop)          # Production of DOP by LPP (consumes t_po4)
                    - (2)*(p_assim_spp_dop)          # Production of DOP by SPP (consumes t_po4)
                    - (2)*(p_assim_lip_dop)          # Production of DOP by LIP (consumes t_po4)
                ) 
             
                change_of_t_lip           = change_of_t_lip           + cgt_timestep*(0.0 
                    + p_nh4_assim_lip                # assimilation of ammonium by limnic phytoplankton
                    + p_no3_assim_lip                # assimilation of nitrate by limnic phytoplankton
                    - p_lip_graz_zoo                 # grazing of zooplankton eating limnic phytoplankton
                    - p_lip_resp_nh4                 # respiration of limnic phytoplankton
                    - p_lip_mort_det                 # mortality of limnic phytoplankton
                ) 
             
                change_of_t_doc           = change_of_t_doc           + cgt_timestep*(0.0 
                    + p_assim_lpp_doc                # Production of DOC by LIP
                    + p_assim_spp_doc                # Production of DOC by SPP
                    + p_assim_lip_doc                # Production of DOC by LPP
                    + p_assim_cya_doc                # Production of DOC by CYA
                    - p_doc2pco                      # particle formation from DOC
                    - p_doc_resp                     # respiration of DOC
                    - p_doc_denit                    # recycling of DOC using nitrate (denitrification)
                    - p_doc_sulf                     # Mineralization of DOC, e-acceptor sulfate (sulfate reduction)
                ) 
             
                change_of_t_dop           = change_of_t_dop           + cgt_timestep*(0.0 
                    + p_assim_lpp_dop                # Production of DOP by LPP
                    + p_assim_spp_dop                # Production of DOP by SPP
                    + p_assim_lip_dop                # Production of DOP by LIP
                    - p_dop2pocp                     # particle formation from DOP
                    - p_dop_resp                     # respiration of DOP
                    - p_dop_denit                    # recycling of DOP using nitrate (denitrification)
                    - p_dop_sulf                     # Mineralization of DOP, e-acceptor sulfate (sulfate reduction)
                ) 
             
                change_of_t_don           = change_of_t_don           + cgt_timestep*(0.0 
                    + p_nh4_assim_lpp_don            # Production of DON by LPP
                    + p_no3_assim_lpp_don            # Production of DON by LPP
                    + p_nh4_assim_spp_don            # Production of DON by SPP
                    + p_no3_assim_spp_don            # Production of DON by SPP
                    + p_nh4_assim_lip_don            # Production of DON by LIP
                    + p_no3_assim_lip_don            # Production of DON by LIP
                    + (p_lpp_resp_nh4)*(don_fraction)   # respiration of large-cell phytoplankton
                    + (p_spp_resp_nh4)*(don_fraction)   # respiration of small-cell phytoplankton
                    + (p_lip_resp_nh4)*(don_fraction)   # respiration of limnic phytoplankton
                    + (p_cya_resp_nh4)*(don_fraction)   # respiration of diazotroph cyanobacteria
                    + (p_zoo_resp_nh4)*(don_fraction)   # respiration of zooplankton
                    - p_don2pocn                     # particle formation from DON
                    - p_don_resp                     # respiration of DON
                    - p_don_denit                    # recycling of DON using nitrate (denitrification)
                    - p_don_sulf                     # Mineralization of DON, e-acceptor sulfate (sulfate reduction)
                ) 
             
                change_of_t_cdom          = change_of_t_cdom          + cgt_timestep*(0.0 
                    - p_cdom_decay                   # decay of cdom due to light
                ) 
             
                change_of_t_cya           = change_of_t_cya           + cgt_timestep*(0.0 
                    + p_n2_assim_cya                 # fixation of dinitrogen by diazotroph cyanobacteria
                    - p_cya_graz_zoo                 # grazing of zooplankton eating diazotroph cyanobacteria
                    - p_cya_resp_nh4                 # respiration of diazotroph cyanobacteria
                    - p_cya_mort_det                 # mortality of diazotroph cyanobacteria
                    - p_cya_mort_det_diff            # mortality of diazotroph cyanobacteria due to strong turbulence
                ) 
             
                change_of_t_det           = change_of_t_det           + cgt_timestep*(0.0 
                    + p_lpp_mort_det                 # mortality of large-cell phytoplankton
                    + p_spp_mort_det                 # mortality of small-scale phytoplankton
                    + p_lip_mort_det                 # mortality of limnic phytoplankton
                    + p_cya_mort_det                 # mortality of diazotroph cyanobacteria
                    + p_cya_mort_det_diff            # mortality of diazotroph cyanobacteria due to strong turbulence
                    + p_zoo_mort_det                 # mortality of zooplankton
                    - p_det_resp_nh4                 # recycling of detritus using oxygen (respiration)
                    - p_det_denit_nh4                # recycling of detritus using nitrate (denitrification)
                    - p_det_sulf_nh4                 # recycling of detritus using sulfate (sulfate reduction)
                ) 
             
                change_of_t_poc           = change_of_t_poc           + cgt_timestep*(0.0 
                    + p_doc2pco                      # particle formation from DOC
                    - p_poc_resp                     # respiration of POC
                    - p_poc_denit                    # recycling of POC using nitrate (denitrification)
                    - p_poc_sulf                     # Mineralization of POC, e-acceptor sulfate (sulfate reduction)
                ) 
             
                change_of_t_pocp          = change_of_t_pocp          + cgt_timestep*(0.0 
                    + p_dop2pocp                     # particle formation from DOP
                    - p_pocp_resp                    # respiration of POCP
                    - p_pocp_denit                   # recycling of POC using nitrate (denitrification)
                    - p_pocp_sulf                    # Mineralization of POC, e-acceptor sulfate (sulfate reduction)
                ) 
             
                change_of_t_pocn          = change_of_t_pocn          + cgt_timestep*(0.0 
                    + p_don2pocn                     # particle formation from DON
                    - p_pocn_resp                    # respiration of POCN
                    - p_pocn_denit                   # recycling of POCN using nitrate (denitrification)
                    - p_pocn_sulf                    # Mineralization of POCN, e-acceptor sulfate (sulfate reduction)
                ) 
             
                change_of_t_lpp           = change_of_t_lpp           + cgt_timestep*(0.0 
                    + p_no3_assim_lpp                # assimilation of nitrate by large-cell phytoplankton
                    + p_nh4_assim_lpp                # assimilation of ammonium by large-cell phytoplankton
                    - p_lpp_graz_zoo                 # grazing of zooplankton eating large-cell phytoplankton
                    - p_lpp_resp_nh4                 # respiration of large-cell phytoplankton
                    - p_lpp_mort_det                 # mortality of large-cell phytoplankton
                ) 
             
                change_of_t_ipw           = change_of_t_ipw           + cgt_timestep*(0.0 
                ) 

                if (k == 0):
                    cgt_dummyvar = 0.0

                    change_of_t_n2            = change_of_t_n2            + cgt_timestep*(0.0 
                        + p_n2_stf_down/(cgt_cellheight*cgt_density)   # downward nitrogen flux through the surface
                        - p_n2_stf_up/(cgt_cellheight*cgt_density)   # upward nitrogen flux through the surface
                    ) 

                    change_of_t_o2            = change_of_t_o2            + cgt_timestep*(0.0 
                        + p_o2_stf_down/(cgt_cellheight*cgt_density)   # downward oxygen flux through the surface
                        - p_o2_stf_up/(cgt_cellheight*cgt_density)   # upward oxygen flux through the surface
                    ) 

                    change_of_t_dic           = change_of_t_dic           + cgt_timestep*(0.0 
                        + p_co2_stf_down/(cgt_cellheight*cgt_density)   # downward co2 flux through the surface
                        - p_co2_stf_up/(cgt_cellheight*cgt_density)   # upward co2 flux through the surface
                    ) 

                    change_of_t_nh4           = change_of_t_nh4           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_no3           = change_of_t_no3           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_po4           = change_of_t_po4           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_spp           = change_of_t_spp           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_zoo           = change_of_t_zoo           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_h2s           = change_of_t_h2s           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_sul           = change_of_t_sul           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_alk           = change_of_t_alk           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_lip           = change_of_t_lip           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_doc           = change_of_t_doc           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_dop           = change_of_t_dop           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_don           = change_of_t_don           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_cdom          = change_of_t_cdom          + cgt_timestep*(0.0 
                    ) 

                    change_of_t_cya           = change_of_t_cya           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_det           = change_of_t_det           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_poc           = change_of_t_poc           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_pocp          = change_of_t_pocp          + cgt_timestep*(0.0 
                    ) 

                    change_of_t_pocn          = change_of_t_pocn          + cgt_timestep*(0.0 
                    ) 

                    change_of_t_lpp           = change_of_t_lpp           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_ipw           = change_of_t_ipw           + cgt_timestep*(0.0 
                    ) 
                 

                if (k == kmax-1):
                    cgt_dummyvar = 0.0

                    change_of_t_n2            = change_of_t_n2            + cgt_timestep*(0.0 
                        + (p_sed_denit_nh4)*(2.65)/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using nitrate (denitrification)
                        + (p_sed_poc_denit)*(0.4)/(cgt_cellheight*cgt_density)   # recycling of sedimentary poc to dic using nitrate (denitrification)
                        + (p_sed_pocn_denit)*(2.65)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocn to dic and NH4 using nitrate (denitrification)
                        + (p_sed_pocp_denit)*(42.4)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using nitrate (denitrification)
                        + (p_nh4_nitdenit_n2)*(0.5)/(cgt_cellheight*cgt_density)   # coupled nitrification and denitrification after mineralization of detritus in oxic sediments
                    ) 

                    change_of_t_o2            = change_of_t_o2            + cgt_timestep*(0.0 
                        - (p_sed_resp_nh4)*(6.625)/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using oxygen (respiration)
                        - p_sed_poc_resp/(cgt_cellheight*cgt_density)   # recycling of sedimentary poc to dic using oxygen (respiration)
                        - (p_sed_pocn_resp)*(6.625)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocn to dic and NH4 using oxygen (respiration)
                        - (p_sed_pocp_resp)*(106)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using oxygen (respiration)
                        - (p_nh4_nitdenit_n2)*(0.75)/(cgt_cellheight*cgt_density)   # coupled nitrification and denitrification after mineralization of detritus in oxic sediments
                    ) 

                    change_of_t_dic           = change_of_t_dic           + cgt_timestep*(0.0 
                        + (p_sed_resp_nh4)*(rfr_c)/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using oxygen (respiration)
                        + (p_sed_denit_nh4)*(rfr_c)/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using nitrate (denitrification)
                        + (p_sed_sulf_nh4)*(rfr_c)/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using sulfate (sulfate reduction)
                        + p_sed_poc_resp/(cgt_cellheight*cgt_density)   # recycling of sedimentary poc to dic using oxygen (respiration)
                        + p_sed_poc_denit/(cgt_cellheight*cgt_density)   # recycling of sedimentary poc to dic using nitrate (denitrification)
                        + p_sed_poc_sulf/(cgt_cellheight*cgt_density)   # recycling of sedimentary poc to dic using sulfate (sulfate reduction)
                        + (p_sed_pocn_resp)*(6.625)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocn to dic and NH4 using oxygen (respiration)
                        + (p_sed_pocp_resp)*(106)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using oxygen (respiration)
                        + (p_sed_pocn_denit)*(6.625)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocn to dic and NH4 using nitrate (denitrification)
                        + (p_sed_pocp_denit)*(106)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using nitrate (denitrification)
                        + (p_sed_pocn_sulf)*(6.625)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocn to dic and NH4 using sulfate (sulfate reduction)
                        + (p_sed_pocp_sulf)*(106)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using sulfate (sulfate reduction)
                        + p_alk_btf/(cgt_cellheight*cgt_density)   # calcium carbonate dissolution from till sediments
                    ) 

                    change_of_t_nh4           = change_of_t_nh4           + cgt_timestep*(0.0 
                        + p_sed_resp_nh4/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using oxygen (respiration)
                        + p_sed_denit_nh4/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using nitrate (denitrification)
                        + p_sed_sulf_nh4/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using sulfate (sulfate reduction)
                        + p_sed_pocn_resp/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocn to dic and NH4 using oxygen (respiration)
                        + p_sed_pocn_denit/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocn to dic and NH4 using nitrate (denitrification)
                        + p_sed_pocn_sulf/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocn to dic and NH4 using sulfate (sulfate reduction)
                        - p_nh4_nitdenit_n2/(cgt_cellheight*cgt_density)   # coupled nitrification and denitrification after mineralization of detritus in oxic sediments
                    ) 

                    change_of_t_no3           = change_of_t_no3           + cgt_timestep*(0.0 
                        - (p_sed_denit_nh4)*(5.3)/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using nitrate (denitrification)
                        - (p_sed_poc_denit)*(0.8)/(cgt_cellheight*cgt_density)   # recycling of sedimentary poc to dic using nitrate (denitrification)
                        - (p_sed_pocn_denit)*(5.3)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocn to dic and NH4 using nitrate (denitrification)
                        - (p_sed_pocp_denit)*(84.8)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using nitrate (denitrification)
                    ) 

                    change_of_t_po4           = change_of_t_po4           + cgt_timestep*(0.0 
                        + (p_sed_resp_nh4)*(rfr_p)/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using oxygen (respiration)
                        + (p_sed_denit_nh4)*(rfr_p)/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using nitrate (denitrification)
                        + (p_sed_sulf_nh4)*(rfr_p)/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using sulfate (sulfate reduction)
                        + p_ips_liber_po4/(cgt_cellheight*cgt_density)   # liberation of phosphate from the sediment under anoxic conditions
                        + p_sed_pocp_resp/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using oxygen (respiration)
                        + p_sed_pocp_denit/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using nitrate (denitrification)
                        + p_sed_pocp_sulf/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using sulfate (sulfate reduction)
                        - (p_po4_retent_ips)*(rfr_p)/(cgt_cellheight*cgt_density)   # retention of phosphate in the sediment under oxic conditions
                    ) 

                    change_of_t_spp           = change_of_t_spp           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_zoo           = change_of_t_zoo           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_h2s           = change_of_t_h2s           + cgt_timestep*(0.0 
                        + (p_sed_sulf_nh4)*(3.3125)/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using sulfate (sulfate reduction)
                        + (p_sed_poc_sulf)*(0.5)/(cgt_cellheight*cgt_density)   # recycling of sedimentary poc to dic using sulfate (sulfate reduction)
                        + (p_sed_pocn_sulf)*(3.3125)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocn to dic and NH4 using sulfate (sulfate reduction)
                        + (p_sed_pocp_sulf)*(53)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using sulfate (sulfate reduction)
                    ) 

                    change_of_t_sul           = change_of_t_sul           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_alk           = change_of_t_alk           + cgt_timestep*(0.0 
                        + (1)*(p_sed_pocn_resp)*(0.5)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocn to dic and NH4 using oxygen (respiration) (produces ohminus)
                        + (1)*(p_sed_pocn_denit)*(0.5)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocn to dic and NH4 using nitrate (denitrification) (produces ohminus)
                        + (1)*(p_sed_pocn_sulf)*(0.5)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocn to dic and NH4 using sulfate (sulfate reduction) (produces ohminus)
                        - (1)*(p_sed_pocp_denit)*(3)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using nitrate (denitrification) (consumes ohminus)
                        - (1)*(p_sed_pocp_sulf)*(3)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using sulfate (sulfate reduction) (consumes ohminus)
                        + (-1)*(p_sed_pocp_resp)*(3)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using oxygen (respiration) (produces h3oplus)
                        + (-1)*(p_nh4_nitdenit_n2)/(cgt_cellheight*cgt_density)   # coupled nitrification and denitrification after mineralization of detritus in oxic sediments (produces h3oplus)
                        - (-1)*(p_sed_resp_nh4)*(0.8125)/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using oxygen (respiration) (consumes h3oplus)
                        - (-1)*(p_sed_denit_nh4)*(6.1125)/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using nitrate (denitrification) (consumes h3oplus)
                        - (-1)*(p_sed_sulf_nh4)*(7.4375)/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using sulfate (sulfate reduction) (consumes h3oplus)
                        - (-1)*(p_sed_poc_denit)*(0.8)/(cgt_cellheight*cgt_density)   # recycling of sedimentary poc to dic using nitrate (denitrification) (consumes h3oplus)
                        - (-1)*(p_sed_poc_sulf)/(cgt_cellheight*cgt_density)   # recycling of sedimentary poc to dic using sulfate (sulfate reduction) (consumes h3oplus)
                        - (-1)*(p_sed_pocn_resp)*(0.5)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocn to dic and NH4 using oxygen (respiration) (consumes h3oplus)
                        - (-1)*(p_sed_pocn_denit)*(5.8)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocn to dic and NH4 using nitrate (denitrification) (consumes h3oplus)
                        - (-1)*(p_sed_pocp_denit)*(84.8)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using nitrate (denitrification) (consumes h3oplus)
                        - (-1)*(p_sed_pocn_sulf)*(7.125)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocn to dic and NH4 using sulfate (sulfate reduction) (consumes h3oplus)
                        - (-1)*(p_sed_pocp_sulf)*(106)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using sulfate (sulfate reduction) (consumes h3oplus)
                        - (-1)*(p_alk_btf)*(2)/(cgt_cellheight*cgt_density)   # calcium carbonate dissolution from till sediments (consumes h3oplus)
                        + (2)*(p_sed_resp_nh4)*(rfr_p)/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using oxygen (respiration) (produces t_po4)
                        + (2)*(p_sed_denit_nh4)*(rfr_p)/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using nitrate (denitrification) (produces t_po4)
                        + (2)*(p_sed_sulf_nh4)*(rfr_p)/(cgt_cellheight*cgt_density)   # recycling of sedimentary detritus to ammonium using sulfate (sulfate reduction) (produces t_po4)
                        + (2)*(p_ips_liber_po4)/(cgt_cellheight*cgt_density)   # liberation of phosphate from the sediment under anoxic conditions (produces t_po4)
                        + (2)*(p_sed_pocp_resp)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using oxygen (respiration) (produces t_po4)
                        + (2)*(p_sed_pocp_denit)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using nitrate (denitrification) (produces t_po4)
                        + (2)*(p_sed_pocp_sulf)/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using sulfate (sulfate reduction) (produces t_po4)
                        - (2)*(p_po4_retent_ips)*(rfr_p)/(cgt_cellheight*cgt_density)   # retention of phosphate in the sediment under oxic conditions (consumes t_po4)
                    ) 

                    change_of_t_lip           = change_of_t_lip           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_doc           = change_of_t_doc           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_dop           = change_of_t_dop           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_don           = change_of_t_don           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_cdom          = change_of_t_cdom          + cgt_timestep*(0.0 
                    ) 

                    change_of_t_cya           = change_of_t_cya           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_det           = change_of_t_det           + cgt_timestep*(0.0 
                        + p_sed_ero_det/(cgt_cellheight*cgt_density)   # sedimentary detritus erosion
                        + p_sed_biores_det/(cgt_cellheight*cgt_density)   # bio resuspension of sedimentary detritus
                        - p_det_sedi_sed/(cgt_cellheight*cgt_density)   # detritus sedimentation
                    ) 

                    change_of_t_poc           = change_of_t_poc           + cgt_timestep*(0.0 
                        + p_sed_ero_poc/(cgt_cellheight*cgt_density)   # sedimentary poc erosion
                        + p_sed_biores_poc/(cgt_cellheight*cgt_density)   # bio resuspension of sedimentary poc
                        - p_poc_sedi_sed/(cgt_cellheight*cgt_density)   # poc sedimentation
                    ) 

                    change_of_t_pocp          = change_of_t_pocp          + cgt_timestep*(0.0 
                        + p_sed_ero_pocp/(cgt_cellheight*cgt_density)   # sedimentary pocp erosion
                        + p_sed_biores_pocp/(cgt_cellheight*cgt_density)   # bio resuspension of sedimentary pocp
                        - p_pocp_sedi_sed/(cgt_cellheight*cgt_density)   # pocp sedimentation
                        - p_sed_pocp_sulf/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocp to dic and PO4 using sulfate (sulfate reduction)
                    ) 

                    change_of_t_pocn          = change_of_t_pocn          + cgt_timestep*(0.0 
                        + p_sed_ero_pocn/(cgt_cellheight*cgt_density)   # sedimentary pocn erosion
                        + p_sed_biores_pocn/(cgt_cellheight*cgt_density)   # bio resuspension of sedimentary pocn
                        - p_pocn_sedi_sed/(cgt_cellheight*cgt_density)   # pocn sedimentation
                        - p_sed_pocn_sulf/(cgt_cellheight*cgt_density)   # recycling of sedimentary pocn to dic and NH4 using sulfate (sulfate reduction)
                    ) 

                    change_of_t_lpp           = change_of_t_lpp           + cgt_timestep*(0.0 
                    ) 

                    change_of_t_ipw           = change_of_t_ipw           + cgt_timestep*(0.0 
                        + p_ips_ero_ipw/(cgt_cellheight*cgt_density)   # erosion of iron PO4
                        + p_ips_biores_ipw/(cgt_cellheight*cgt_density)   # bio resuspension of iron PO4
                        - p_ipw_sedi_ips/(cgt_cellheight*cgt_density)   # sedimentation of iron PO4
                    ) 

                    change_of_t_sed           = change_of_t_sed           + cgt_timestep*(0.0 
                        + p_det_sedi_sed                 # detritus sedimentation
                        - p_sed_resp_nh4                 # recycling of sedimentary detritus to ammonium using oxygen (respiration)
                        - p_sed_denit_nh4                # recycling of sedimentary detritus to ammonium using nitrate (denitrification)
                        - p_sed_sulf_nh4                 # recycling of sedimentary detritus to ammonium using sulfate (sulfate reduction)
                        - p_sed_ero_det                  # sedimentary detritus erosion
                        - p_sed_biores_det               # bio resuspension of sedimentary detritus
                        - p_sed_burial                   # burial of detritus deeper than max_sed
                    ) 

                    change_of_t_ips           = change_of_t_ips           + cgt_timestep*(0.0 
                        + (p_po4_retent_ips)*(rfr_p)     # retention of phosphate in the sediment under oxic conditions
                        + p_ipw_sedi_ips                 # sedimentation of iron PO4
                        - p_ips_liber_po4                # liberation of phosphate from the sediment under anoxic conditions
                        - p_ips_ero_ipw                  # erosion of iron PO4
                        - p_ips_biores_ipw               # bio resuspension of iron PO4
                        - p_ips_burial                   # burial of iron PO4
                    ) 

                    change_of_t_sed_poc       = change_of_t_sed_poc       + cgt_timestep*(0.0 
                        + p_poc_sedi_sed                 # poc sedimentation
                        - p_sed_poc_resp                 # recycling of sedimentary poc to dic using oxygen (respiration)
                        - p_sed_poc_denit                # recycling of sedimentary poc to dic using nitrate (denitrification)
                        - p_sed_poc_sulf                 # recycling of sedimentary poc to dic using sulfate (sulfate reduction)
                        - p_sed_ero_poc                  # sedimentary poc erosion
                        - p_sed_biores_poc               # bio resuspension of sedimentary poc
                        - p_poc_burial                   # burial of poc deeper than max_sed
                    ) 

                    change_of_t_sed_pocn      = change_of_t_sed_pocn      + cgt_timestep*(0.0 
                        + p_pocn_sedi_sed                # pocn sedimentation
                        - p_sed_ero_pocn                 # sedimentary pocn erosion
                        - p_sed_biores_pocn              # bio resuspension of sedimentary pocn
                        - p_pocn_burial                  # burial of pocn deeper than max_sed
                        - p_sed_pocn_resp                # recycling of sedimentary pocn to dic and NH4 using oxygen (respiration)
                        - p_sed_pocn_denit               # recycling of sedimentary pocn to dic and NH4 using nitrate (denitrification)
                    ) 

                    change_of_t_sed_pocp      = change_of_t_sed_pocp      + cgt_timestep*(0.0 
                        + p_pocp_sedi_sed                # pocp sedimentation
                        - p_sed_ero_pocp                 # sedimentary pocp erosion
                        - p_sed_biores_pocp              # bio resuspension of sedimentary pocp
                        - p_pocp_burial                  # burial of pocp deeper than max_sed
                        - p_sed_pocp_resp                # recycling of sedimentary pocp to dic and PO4 using oxygen (respiration)
                        - p_sed_pocp_denit               # recycling of sedimentary pocp to dic and PO4 using nitrate (denitrification)
                    ) 
                            

                #------------------------------------
                # STEP 6.3: calculate maximum fraction of the timestep before some tracer gets exhausted
                #------------------------------------

                timestep_fraction = 1.0 
                which_tracer_exhausted = -1 

                # find the tracer which is exhausted after the shortest period of time

                # in the water column
             
                # check if tracer t_n2            was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_n2           [k] <= 0.0) & (change_of_t_n2            < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 1 
                 
                # check if tracer t_n2            was present, but got exhausted
                if ((tracer_vector_t_n2           [k] > 0.0) & (tracer_vector_t_n2           [k] + change_of_t_n2            < 0.0)):
                    timestep_fraction_new = tracer_vector_t_n2           [k] / (0.0 - change_of_t_n2           ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 1 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_o2            was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_o2           [k] <= 0.0) & (change_of_t_o2            < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 2 
                 
                # check if tracer t_o2            was present, but got exhausted
                if ((tracer_vector_t_o2           [k] > 0.0) & (tracer_vector_t_o2           [k] + change_of_t_o2            < 0.0)):
                    timestep_fraction_new = tracer_vector_t_o2           [k] / (0.0 - change_of_t_o2           ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 2 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_dic           was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_dic          [k] <= 0.0) & (change_of_t_dic           < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 3 
                 
                # check if tracer t_dic           was present, but got exhausted
                if ((tracer_vector_t_dic          [k] > 0.0) & (tracer_vector_t_dic          [k] + change_of_t_dic           < 0.0)):
                    timestep_fraction_new = tracer_vector_t_dic          [k] / (0.0 - change_of_t_dic          ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 3 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_nh4           was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_nh4          [k] <= 0.0) & (change_of_t_nh4           < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 4 
                 
                # check if tracer t_nh4           was present, but got exhausted
                if ((tracer_vector_t_nh4          [k] > 0.0) & (tracer_vector_t_nh4          [k] + change_of_t_nh4           < 0.0)):
                    timestep_fraction_new = tracer_vector_t_nh4          [k] / (0.0 - change_of_t_nh4          ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 4 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_no3           was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_no3          [k] <= 0.0) & (change_of_t_no3           < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 5 
                 
                # check if tracer t_no3           was present, but got exhausted
                if ((tracer_vector_t_no3          [k] > 0.0) & (tracer_vector_t_no3          [k] + change_of_t_no3           < 0.0)):
                    timestep_fraction_new = tracer_vector_t_no3          [k] / (0.0 - change_of_t_no3          ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 5 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_po4           was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_po4          [k] <= 0.0) & (change_of_t_po4           < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 6 
                 
                # check if tracer t_po4           was present, but got exhausted
                if ((tracer_vector_t_po4          [k] > 0.0) & (tracer_vector_t_po4          [k] + change_of_t_po4           < 0.0)):
                    timestep_fraction_new = tracer_vector_t_po4          [k] / (0.0 - change_of_t_po4          ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 6 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_spp           was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_spp          [k] <= 0.0) & (change_of_t_spp           < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 7 
                 
                # check if tracer t_spp           was present, but got exhausted
                if ((tracer_vector_t_spp          [k] > 0.0) & (tracer_vector_t_spp          [k] + change_of_t_spp           < 0.0)):
                    timestep_fraction_new = tracer_vector_t_spp          [k] / (0.0 - change_of_t_spp          ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 7 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_zoo           was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_zoo          [k] <= 0.0) & (change_of_t_zoo           < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 8 
                 
                # check if tracer t_zoo           was present, but got exhausted
                if ((tracer_vector_t_zoo          [k] > 0.0) & (tracer_vector_t_zoo          [k] + change_of_t_zoo           < 0.0)):
                    timestep_fraction_new = tracer_vector_t_zoo          [k] / (0.0 - change_of_t_zoo          ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 8 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_h2s           was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_h2s          [k] <= 0.0) & (change_of_t_h2s           < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 9 
                 
                # check if tracer t_h2s           was present, but got exhausted
                if ((tracer_vector_t_h2s          [k] > 0.0) & (tracer_vector_t_h2s          [k] + change_of_t_h2s           < 0.0)):
                    timestep_fraction_new = tracer_vector_t_h2s          [k] / (0.0 - change_of_t_h2s          ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 9 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_sul           was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_sul          [k] <= 0.0) & (change_of_t_sul           < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 10 
                 
                # check if tracer t_sul           was present, but got exhausted
                if ((tracer_vector_t_sul          [k] > 0.0) & (tracer_vector_t_sul          [k] + change_of_t_sul           < 0.0)):
                    timestep_fraction_new = tracer_vector_t_sul          [k] / (0.0 - change_of_t_sul          ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 10 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_lip           was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_lip          [k] <= 0.0) & (change_of_t_lip           < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 14 
                 
                # check if tracer t_lip           was present, but got exhausted
                if ((tracer_vector_t_lip          [k] > 0.0) & (tracer_vector_t_lip          [k] + change_of_t_lip           < 0.0)):
                    timestep_fraction_new = tracer_vector_t_lip          [k] / (0.0 - change_of_t_lip          ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 14 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_doc           was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_doc          [k] <= 0.0) & (change_of_t_doc           < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 15 
                 
                # check if tracer t_doc           was present, but got exhausted
                if ((tracer_vector_t_doc          [k] > 0.0) & (tracer_vector_t_doc          [k] + change_of_t_doc           < 0.0)):
                    timestep_fraction_new = tracer_vector_t_doc          [k] / (0.0 - change_of_t_doc          ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 15 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_dop           was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_dop          [k] <= 0.0) & (change_of_t_dop           < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 16 
                 
                # check if tracer t_dop           was present, but got exhausted
                if ((tracer_vector_t_dop          [k] > 0.0) & (tracer_vector_t_dop          [k] + change_of_t_dop           < 0.0)):
                    timestep_fraction_new = tracer_vector_t_dop          [k] / (0.0 - change_of_t_dop          ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 16 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_don           was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_don          [k] <= 0.0) & (change_of_t_don           < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 17 
                 
                # check if tracer t_don           was present, but got exhausted
                if ((tracer_vector_t_don          [k] > 0.0) & (tracer_vector_t_don          [k] + change_of_t_don           < 0.0)):
                    timestep_fraction_new = tracer_vector_t_don          [k] / (0.0 - change_of_t_don          ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 17 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_cdom          was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_cdom         [k] <= 0.0) & (change_of_t_cdom          < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 21 
                 
                # check if tracer t_cdom          was present, but got exhausted
                if ((tracer_vector_t_cdom         [k] > 0.0) & (tracer_vector_t_cdom         [k] + change_of_t_cdom          < 0.0)):
                    timestep_fraction_new = tracer_vector_t_cdom         [k] / (0.0 - change_of_t_cdom         ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 21 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_cya           was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_cya          [k] <= 0.0) & (change_of_t_cya           < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 22 
                 
                # check if tracer t_cya           was present, but got exhausted
                if ((tracer_vector_t_cya          [k] > 0.0) & (tracer_vector_t_cya          [k] + change_of_t_cya           < 0.0)):
                    timestep_fraction_new = tracer_vector_t_cya          [k] / (0.0 - change_of_t_cya          ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 22 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_det           was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_det          [k] <= 0.0) & (change_of_t_det           < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 23 
                 
                # check if tracer t_det           was present, but got exhausted
                if ((tracer_vector_t_det          [k] > 0.0) & (tracer_vector_t_det          [k] + change_of_t_det           < 0.0)):
                    timestep_fraction_new = tracer_vector_t_det          [k] / (0.0 - change_of_t_det          ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 23 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_poc           was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_poc          [k] <= 0.0) & (change_of_t_poc           < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 24 
                 
                # check if tracer t_poc           was present, but got exhausted
                if ((tracer_vector_t_poc          [k] > 0.0) & (tracer_vector_t_poc          [k] + change_of_t_poc           < 0.0)):
                    timestep_fraction_new = tracer_vector_t_poc          [k] / (0.0 - change_of_t_poc          ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 24 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_pocp          was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_pocp         [k] <= 0.0) & (change_of_t_pocp          < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 25 
                 
                # check if tracer t_pocp          was present, but got exhausted
                if ((tracer_vector_t_pocp         [k] > 0.0) & (tracer_vector_t_pocp         [k] + change_of_t_pocp          < 0.0)):
                    timestep_fraction_new = tracer_vector_t_pocp         [k] / (0.0 - change_of_t_pocp         ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 25 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_pocn          was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_pocn         [k] <= 0.0) & (change_of_t_pocn          < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 26 
                 
                # check if tracer t_pocn          was present, but got exhausted
                if ((tracer_vector_t_pocn         [k] > 0.0) & (tracer_vector_t_pocn         [k] + change_of_t_pocn          < 0.0)):
                    timestep_fraction_new = tracer_vector_t_pocn         [k] / (0.0 - change_of_t_pocn         ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 26 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_lpp           was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_lpp          [k] <= 0.0) & (change_of_t_lpp           < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 27 
                 
                # check if tracer t_lpp           was present, but got exhausted
                if ((tracer_vector_t_lpp          [k] > 0.0) & (tracer_vector_t_lpp          [k] + change_of_t_lpp           < 0.0)):
                    timestep_fraction_new = tracer_vector_t_lpp          [k] / (0.0 - change_of_t_lpp          ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 27 
                        timestep_fraction = timestep_fraction_new 
                    
                 
             
                # check if tracer t_ipw           was exhausted from the beginning and is still consumed
                if ((tracer_vector_t_ipw          [k] <= 0.0) & (change_of_t_ipw           < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = 28 
                 
                # check if tracer t_ipw           was present, but got exhausted
                if ((tracer_vector_t_ipw          [k] > 0.0) & (tracer_vector_t_ipw          [k] + change_of_t_ipw           < 0.0)):
                    timestep_fraction_new = tracer_vector_t_ipw          [k] / (0.0 - change_of_t_ipw          ) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = 28 
                        timestep_fraction = timestep_fraction_new 
                    
                 
          
                # in the bottom layer
                if (k == kmax-1):
                    cgt_dummyvar = 0.0

                    # check if tracer t_sed           was exhausted from the beginning and is still consumed
                    if ((tracer_scalar_t_sed           <= 0.0) & (change_of_t_sed           < 0.0)):
                        timestep_fraction = 0.0 
                        which_tracer_exhausted = 12 
                   
                    # check if tracer t_sed           was present, but got exhausted
                    if ((tracer_scalar_t_sed           > 0.0) & (tracer_scalar_t_sed           + change_of_t_sed           < 0.0)):
                        timestep_fraction_new = tracer_scalar_t_sed           / (0.0 - change_of_t_sed          ) 
                        if (timestep_fraction_new <= timestep_fraction):
                            which_tracer_exhausted = 12 
                            timestep_fraction = timestep_fraction_new 
                       
                    

                    # check if tracer t_ips           was exhausted from the beginning and is still consumed
                    if ((tracer_scalar_t_ips           <= 0.0) & (change_of_t_ips           < 0.0)):
                        timestep_fraction = 0.0 
                        which_tracer_exhausted = 13 
                   
                    # check if tracer t_ips           was present, but got exhausted
                    if ((tracer_scalar_t_ips           > 0.0) & (tracer_scalar_t_ips           + change_of_t_ips           < 0.0)):
                        timestep_fraction_new = tracer_scalar_t_ips           / (0.0 - change_of_t_ips          ) 
                        if (timestep_fraction_new <= timestep_fraction):
                            which_tracer_exhausted = 13 
                            timestep_fraction = timestep_fraction_new 
                       
                    

                    # check if tracer t_sed_poc       was exhausted from the beginning and is still consumed
                    if ((tracer_scalar_t_sed_poc       <= 0.0) & (change_of_t_sed_poc       < 0.0)):
                        timestep_fraction = 0.0 
                        which_tracer_exhausted = 18 
                   
                    # check if tracer t_sed_poc       was present, but got exhausted
                    if ((tracer_scalar_t_sed_poc       > 0.0) & (tracer_scalar_t_sed_poc       + change_of_t_sed_poc       < 0.0)):
                        timestep_fraction_new = tracer_scalar_t_sed_poc       / (0.0 - change_of_t_sed_poc      ) 
                        if (timestep_fraction_new <= timestep_fraction):
                            which_tracer_exhausted = 18 
                            timestep_fraction = timestep_fraction_new 
                       
                    

                    # check if tracer t_sed_pocn      was exhausted from the beginning and is still consumed
                    if ((tracer_scalar_t_sed_pocn      <= 0.0) & (change_of_t_sed_pocn      < 0.0)):
                        timestep_fraction = 0.0 
                        which_tracer_exhausted = 19 
                   
                    # check if tracer t_sed_pocn      was present, but got exhausted
                    if ((tracer_scalar_t_sed_pocn      > 0.0) & (tracer_scalar_t_sed_pocn      + change_of_t_sed_pocn      < 0.0)):
                        timestep_fraction_new = tracer_scalar_t_sed_pocn      / (0.0 - change_of_t_sed_pocn     ) 
                        if (timestep_fraction_new <= timestep_fraction):
                            which_tracer_exhausted = 19 
                            timestep_fraction = timestep_fraction_new 
                       
                    

                    # check if tracer t_sed_pocp      was exhausted from the beginning and is still consumed
                    if ((tracer_scalar_t_sed_pocp      <= 0.0) & (change_of_t_sed_pocp      < 0.0)):
                        timestep_fraction = 0.0 
                        which_tracer_exhausted = 20 
                   
                    # check if tracer t_sed_pocp      was present, but got exhausted
                    if ((tracer_scalar_t_sed_pocp      > 0.0) & (tracer_scalar_t_sed_pocp      + change_of_t_sed_pocp      < 0.0)):
                        timestep_fraction_new = tracer_scalar_t_sed_pocp      / (0.0 - change_of_t_sed_pocp     ) 
                        if (timestep_fraction_new <= timestep_fraction):
                            which_tracer_exhausted = 20 
                            timestep_fraction = timestep_fraction_new 
                       
                    
                           

                # now, update the limitations: rates of the processes limited by this tracer become zero in the future

                if (1 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_n2_7           = 0.0 
                 
                if (2 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_o2_0           = 0.0 
                    lim_t_o2_2           = 0.0 
                    lim_t_o2_4           = 0.0 
                    lim_t_o2_6           = 0.0 
                 
                if (3 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_dic_8          = 0.0 
                 
                if (4 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_nh4_11         = 0.0 
                 
                if (5 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_no3_1          = 0.0 
                    lim_t_no3_3          = 0.0 
                    lim_t_no3_9          = 0.0 
                 
                if (6 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_po4_10         = 0.0 
                 
                if (7 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_spp_16         = 0.0 
                 
                if (8 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_zoo_19         = 0.0 
                 
                if (9 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_h2s_5          = 0.0 
                    lim_t_h2s_24         = 0.0 
                 
                if (10 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_sul_25         = 0.0 
                 
                if (12 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_sed_21         = 0.0 
                 
                if (13 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_ips_23         = 0.0 
                 
                if (14 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_lip_18         = 0.0 
                 
                if (15 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_doc_29         = 0.0 
                 
                if (16 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_dop_30         = 0.0 
                 
                if (17 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_don_31         = 0.0 
                 
                if (18 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_sed_poc_22     = 0.0 
                 
                if (19 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_sed_pocn_27    = 0.0 
                 
                if (20 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_sed_pocp_28    = 0.0 
                 
                if (21 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_cdom_32        = 0.0 
                 
                if (22 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_cya_17         = 0.0 
                 
                if (23 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_det_20         = 0.0 
                 
                if (24 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_poc_12         = 0.0 
                 
                if (25 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_pocp_13        = 0.0 
                 
                if (26 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_pocn_14        = 0.0 
                 
                if (27 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_lpp_15         = 0.0 
                 
                if (28 == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                    lim_t_ipw_26         = 0.0 
                 

                #------------------------------------
                # STEP 6.4: apply a Euler-forward timestep with the fraction of the time
                #------------------------------------ 

                # in the water column
             
                # tracer t_n2            (dissolved molecular nitrogen):
                tracer_vector_t_n2           [k] = tracer_vector_t_n2           [k] + change_of_t_n2            * timestep_fraction 
             
                # tracer t_o2            (dissolved oxygen):
                tracer_vector_t_o2           [k] = tracer_vector_t_o2           [k] + change_of_t_o2            * timestep_fraction 
             
                # tracer t_dic           (dissolved inorganic carbon, treated as carbon dioxide):
                tracer_vector_t_dic          [k] = tracer_vector_t_dic          [k] + change_of_t_dic           * timestep_fraction 
             
                # tracer t_nh4           (ammonium):
                tracer_vector_t_nh4          [k] = tracer_vector_t_nh4          [k] + change_of_t_nh4           * timestep_fraction 
             
                # tracer t_no3           (nitrate):
                tracer_vector_t_no3          [k] = tracer_vector_t_no3          [k] + change_of_t_no3           * timestep_fraction 
             
                # tracer t_po4           (phosphate):
                tracer_vector_t_po4          [k] = tracer_vector_t_po4          [k] + change_of_t_po4           * timestep_fraction 
             
                # tracer t_spp           (small-cell phytoplankton):
                tracer_vector_t_spp          [k] = tracer_vector_t_spp          [k] + change_of_t_spp           * timestep_fraction 
             
                # tracer t_zoo           (zooplankton):
                tracer_vector_t_zoo          [k] = tracer_vector_t_zoo          [k] + change_of_t_zoo           * timestep_fraction 
             
                # tracer t_h2s           (hydrogen sulfide):
                tracer_vector_t_h2s          [k] = tracer_vector_t_h2s          [k] + change_of_t_h2s           * timestep_fraction 
             
                # tracer t_sul           (sulfur):
                tracer_vector_t_sul          [k] = tracer_vector_t_sul          [k] + change_of_t_sul           * timestep_fraction 
             
                # tracer t_alk           (total alkalinity):
                tracer_vector_t_alk          [k] = tracer_vector_t_alk          [k] + change_of_t_alk           * timestep_fraction 
             
                # tracer t_lip           (limnic phytoplankton):
                tracer_vector_t_lip          [k] = tracer_vector_t_lip          [k] + change_of_t_lip           * timestep_fraction 
             
                # tracer t_doc           (dissolved organic carbon):
                tracer_vector_t_doc          [k] = tracer_vector_t_doc          [k] + change_of_t_doc           * timestep_fraction 
             
                # tracer t_dop           (phosphorus in dissolved organic carbon in Redfield ratio):
                tracer_vector_t_dop          [k] = tracer_vector_t_dop          [k] + change_of_t_dop           * timestep_fraction 
             
                # tracer t_don           (nitrogen in dissolved organic carbon in Redfield ratio):
                tracer_vector_t_don          [k] = tracer_vector_t_don          [k] + change_of_t_don           * timestep_fraction 
             
                # tracer t_cdom          (colored dissolved organic carbon):
                tracer_vector_t_cdom         [k] = tracer_vector_t_cdom         [k] + change_of_t_cdom          * timestep_fraction 
             
                # tracer t_cya           (diazotroph cyanobacteria):
                tracer_vector_t_cya          [k] = tracer_vector_t_cya          [k] + change_of_t_cya           * timestep_fraction 
             
                # tracer t_det           (detritus):
                tracer_vector_t_det          [k] = tracer_vector_t_det          [k] + change_of_t_det           * timestep_fraction 
             
                # tracer t_poc           (particulate organic carbon):
                tracer_vector_t_poc          [k] = tracer_vector_t_poc          [k] + change_of_t_poc           * timestep_fraction 
             
                # tracer t_pocp          (phosphorus in particulate organic carbon in Redfield ratio):
                tracer_vector_t_pocp         [k] = tracer_vector_t_pocp         [k] + change_of_t_pocp          * timestep_fraction 
             
                # tracer t_pocn          (nitrogen in particulate organic carbon in Redfield ratio):
                tracer_vector_t_pocn         [k] = tracer_vector_t_pocn         [k] + change_of_t_pocn          * timestep_fraction 
             
                # tracer t_lpp           (large-cell phytoplankton):
                tracer_vector_t_lpp          [k] = tracer_vector_t_lpp          [k] + change_of_t_lpp           * timestep_fraction 
             
                # tracer t_ipw           (suspended iron phosphate):
                tracer_vector_t_ipw          [k] = tracer_vector_t_ipw          [k] + change_of_t_ipw           * timestep_fraction 
          
                # in the bottom layer
                if (k == kmax-1):
                    cgt_dummyvar = 0.0

                    # tracer t_sed           (sediment detritus)
                    tracer_scalar_t_sed           = tracer_scalar_t_sed           + change_of_t_sed           * timestep_fraction 

                    # tracer t_ips           (iron phosphate in sediment)
                    tracer_scalar_t_ips           = tracer_scalar_t_ips           + change_of_t_ips           * timestep_fraction 

                    # tracer t_sed_poc       (sediment particular carbon)
                    tracer_scalar_t_sed_poc       = tracer_scalar_t_sed_poc       + change_of_t_sed_poc       * timestep_fraction 

                    # tracer t_sed_pocn      (sediment particular organic N+C)
                    tracer_scalar_t_sed_pocn      = tracer_scalar_t_sed_pocn      + change_of_t_sed_pocn      * timestep_fraction 

                    # tracer t_sed_pocp      (sediment particular organic P+C)
                    tracer_scalar_t_sed_pocp      = tracer_scalar_t_sed_pocp      + change_of_t_sed_pocp      * timestep_fraction 
                            

                #------------------------------------
                # STEP 6.5: output of process rates
                #------------------------------------
                output_vector_p_no3_assim_lpp[k] = output_vector_p_no3_assim_lpp[k] + p_no3_assim_lpp * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_nh4_assim_lpp[k] = output_vector_p_nh4_assim_lpp[k] + p_nh4_assim_lpp * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_no3_assim_spp[k] = output_vector_p_no3_assim_spp[k] + p_no3_assim_spp * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_nh4_assim_spp[k] = output_vector_p_nh4_assim_spp[k] + p_nh4_assim_spp * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_n2_assim_cya [k] = output_vector_p_n2_assim_cya [k] + p_n2_assim_cya  * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_assim_lpp_doc[k] = output_vector_p_assim_lpp_doc[k] + p_assim_lpp_doc * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_assim_spp_doc[k] = output_vector_p_assim_spp_doc[k] + p_assim_spp_doc * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_assim_cya_doc[k] = output_vector_p_assim_cya_doc[k] + p_assim_cya_doc * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_assim_lpp_dop[k] = output_vector_p_assim_lpp_dop[k] + p_assim_lpp_dop * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_assim_spp_dop[k] = output_vector_p_assim_spp_dop[k] + p_assim_spp_dop * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_nh4_assim_lpp_don[k] = output_vector_p_nh4_assim_lpp_don[k] + p_nh4_assim_lpp_don * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_no3_assim_lpp_don[k] = output_vector_p_no3_assim_lpp_don[k] + p_no3_assim_lpp_don * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_nh4_assim_spp_don[k] = output_vector_p_nh4_assim_spp_don[k] + p_nh4_assim_spp_don * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_no3_assim_spp_don[k] = output_vector_p_no3_assim_spp_don[k] + p_no3_assim_spp_don * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_pocp_resp    [k] = output_vector_p_pocp_resp    [k] + p_pocp_resp     * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_pocn_resp    [k] = output_vector_p_pocn_resp    [k] + p_pocn_resp     * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_cya_mort_det_diff[k] = output_vector_p_cya_mort_det_diff[k] + p_cya_mort_det_diff * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_det_resp_nh4 [k] = output_vector_p_det_resp_nh4 [k] + p_det_resp_nh4  * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_det_denit_nh4[k] = output_vector_p_det_denit_nh4[k] + p_det_denit_nh4 * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_det_sulf_nh4 [k] = output_vector_p_det_sulf_nh4 [k] + p_det_sulf_nh4  * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_h2s_oxno3_sul[k] = output_vector_p_h2s_oxno3_sul[k] + p_h2s_oxno3_sul * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_doc2pco      [k] = output_vector_p_doc2pco      [k] + p_doc2pco       * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_dop2pocp     [k] = output_vector_p_dop2pocp     [k] + p_dop2pocp      * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_don2pocn     [k] = output_vector_p_don2pocn     [k] + p_don2pocn      * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_doc_resp     [k] = output_vector_p_doc_resp     [k] + p_doc_resp      * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_dop_resp     [k] = output_vector_p_dop_resp     [k] + p_dop_resp      * timestep_fraction * fraction_of_total_timestep 
                output_vector_p_don_resp     [k] = output_vector_p_don_resp     [k] + p_don_resp      * timestep_fraction * fraction_of_total_timestep 
                if (k == kmax-1):
                    cgt_dummyvar = 0.0
                    output_scalar_p_sed_resp_nh4  = output_scalar_p_sed_resp_nh4  + p_sed_resp_nh4  * timestep_fraction * fraction_of_total_timestep 
                    output_scalar_p_sed_biores_poc = output_scalar_p_sed_biores_poc + p_sed_biores_poc * timestep_fraction * fraction_of_total_timestep 
                    output_scalar_p_sed_burial    = output_scalar_p_sed_burial    + p_sed_burial    * timestep_fraction * fraction_of_total_timestep 
                    output_scalar_p_ips_burial    = output_scalar_p_ips_burial    + p_ips_burial    * timestep_fraction * fraction_of_total_timestep 
                    output_scalar_p_poc_burial    = output_scalar_p_poc_burial    + p_poc_burial    * timestep_fraction * fraction_of_total_timestep 
                    output_scalar_p_pocn_burial   = output_scalar_p_pocn_burial   + p_pocn_burial   * timestep_fraction * fraction_of_total_timestep 
                    output_scalar_p_pocp_burial   = output_scalar_p_pocp_burial   + p_pocp_burial   * timestep_fraction * fraction_of_total_timestep 
                    output_scalar_p_alk_btf       = output_scalar_p_alk_btf       + p_alk_btf       * timestep_fraction * fraction_of_total_timestep 
                 
                if (k == 1):
                    cgt_dummyvar = 0.0
                 
             
                #------------------------------------
                # STEP 6.6: set timestep to remaining timestep only
                #------------------------------------

                cgt_timestep = cgt_timestep * (1.0 - timestep_fraction)                           # remaining timestep
                fraction_of_total_timestep = fraction_of_total_timestep * (1.0 - timestep_fraction)   # how much of the original timestep is remaining


                if (number_of_loop > 100):
                    error('aborted positive-definite scheme: more than 100 iterations') 
                 
                number_of_loop=number_of_loop+1 

              
            #------------------------------------
            #-- END OF POSITIVE-DEFINITE SCHEME -
            #------------------------------------  
             
            #------------------------------------
            # STEP 7.1: output of new tracer concentrations
            #------------------------------------
            output_vector_t_n2           [k] = output_vector_t_n2           [k] + t_n2            
            output_vector_t_o2           [k] = output_vector_t_o2           [k] + t_o2            
            output_vector_t_dic          [k] = output_vector_t_dic          [k] + t_dic           
            output_vector_t_nh4          [k] = output_vector_t_nh4          [k] + t_nh4           
            output_vector_t_no3          [k] = output_vector_t_no3          [k] + t_no3           
            output_vector_t_po4          [k] = output_vector_t_po4          [k] + t_po4           
            output_vector_t_spp          [k] = output_vector_t_spp          [k] + t_spp           
            output_vector_t_zoo          [k] = output_vector_t_zoo          [k] + t_zoo           
            output_vector_t_h2s          [k] = output_vector_t_h2s          [k] + t_h2s           
            output_vector_t_sul          [k] = output_vector_t_sul          [k] + t_sul           
            output_vector_t_alk          [k] = output_vector_t_alk          [k] + t_alk           
            output_vector_t_lip          [k] = output_vector_t_lip          [k] + t_lip           
            output_vector_t_doc          [k] = output_vector_t_doc          [k] + t_doc           
            output_vector_t_dop          [k] = output_vector_t_dop          [k] + t_dop           
            output_vector_t_don          [k] = output_vector_t_don          [k] + t_don           
            output_vector_t_cdom         [k] = output_vector_t_cdom         [k] + t_cdom          
            output_vector_t_cya          [k] = output_vector_t_cya          [k] + t_cya           
            output_vector_t_det          [k] = output_vector_t_det          [k] + t_det           
            output_vector_t_poc          [k] = output_vector_t_poc          [k] + t_poc           
            output_vector_t_pocp         [k] = output_vector_t_pocp         [k] + t_pocp          
            output_vector_t_pocn         [k] = output_vector_t_pocn         [k] + t_pocn          
            output_vector_t_lpp          [k] = output_vector_t_lpp          [k] + t_lpp           
            output_vector_t_ipw          [k] = output_vector_t_ipw          [k] + t_ipw           
            if (k == kmax-1):
                cgt_dummyvar = 0.0
                output_scalar_t_sed           = output_scalar_t_sed           + t_sed           
                output_scalar_t_ips           = output_scalar_t_ips           + t_ips           
                output_scalar_t_sed_poc       = output_scalar_t_sed_poc       + t_sed_poc       
                output_scalar_t_sed_pocn      = output_scalar_t_sed_pocn      + t_sed_pocn      
                output_scalar_t_sed_pocp      = output_scalar_t_sed_pocp      + t_sed_pocp      
              
            if (k==0):
                cgt_dummyvar = 0.0
              
             
            #------------------------------------
            # STEP 7.2: calculate "late" auxiliaries
            #------------------------------------

            if (k == kmax-1):
                cgt_dummyvar = 0.0
              
             
            if (k == 0):
                cgt_dummyvar = 0.0
              
             
            #------------------------------------
            # STEP 7.3: output of "late" auxiliaries
            #------------------------------------
            if (k == kmax-1):
                cgt_dummyvar = 0.0
              
            if (k == 0):
                cgt_dummyvar = 0.0
              

            #---------------------------------------
            # STEP 7.4: passing vertical velocity and diffusivity to the coupler
            #---------------------------------------

            # EXPLICIT MOVEMENT
            vertical_speed_of_t_cya          [k]=(w_cya)/(24*3600.0)   # convert to m/s
            vertical_diffusivity_of_t_cya          [k]=(0.0)          # leave as m2/s
            vertical_speed_of_t_det          [k]=(w_det)/(24*3600.0)   # convert to m/s
            vertical_diffusivity_of_t_det          [k]=(0.0)          # leave as m2/s
            vertical_speed_of_t_poc          [k]=(w_poc_var)/(24*3600.0)   # convert to m/s
            vertical_diffusivity_of_t_poc          [k]=(0.0)          # leave as m2/s
            vertical_speed_of_t_pocp         [k]=(w_pocp)/(24*3600.0)   # convert to m/s
            vertical_diffusivity_of_t_pocp         [k]=(0.0)          # leave as m2/s
            vertical_speed_of_t_pocn         [k]=(w_pocn)/(24*3600.0)   # convert to m/s
            vertical_diffusivity_of_t_pocn         [k]=(0.0)          # leave as m2/s
            vertical_speed_of_t_lpp          [k]=(w_lpp)/(24*3600.0)   # convert to m/s
            vertical_diffusivity_of_t_lpp          [k]=(0.0)          # leave as m2/s
            vertical_speed_of_t_ipw          [k]=(w_ipw)/(24*3600.0)   # convert to m/s
            vertical_diffusivity_of_t_ipw          [k]=(0.0)          # leave as m2/s
     
    
    #---------------------------------------
    # biological timestep has ended
    #---------------------------------------
    
    #---------------------------------------
    # vertical movement follows
    #---------------------------------------
    
    # calculate total colored element concentrations at bottom
