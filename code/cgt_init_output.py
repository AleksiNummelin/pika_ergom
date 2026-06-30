def cgt_init_output():
    #-----------------------------
    # initialize the output arrays
    #-----------------------------
    import numpy as np
    # auxiliary variables
    # growth rate of large-cell phytoplankton, limited by DIN, DIP, light and oxygen [1/day] :
    global output_lr_assim_lpp   
    output_lr_assim_lpp    = np.full((max_output_index,kmax),np.nan)
    global output_vector_lr_assim_lpp   
    output_vector_lr_assim_lpp    = np.zeros(kmax)
    # growth rate of small-cell phytoplankton, limited by DIN, DIP, light, oxygen and temperature [1/day] :
    global output_lr_assim_spp   
    output_lr_assim_spp    = np.full((max_output_index,kmax),np.nan)
    global output_vector_lr_assim_spp   
    output_vector_lr_assim_spp    = np.zeros(kmax)
    # growth rate of diazotroph cyanobacteria, limited by DIP, light, oxygen, temperature and salinity [1/day] :
    global output_lr_assim_cya   
    output_lr_assim_cya    = np.full((max_output_index,kmax),np.nan)
    global output_vector_lr_assim_cya   
    output_vector_lr_assim_cya    = np.zeros(kmax)
    # production rate of DOC by LPP :
    global output_lr_assim_lpp_doc
    output_lr_assim_lpp_doc = np.full((max_output_index,kmax),np.nan)
    global output_vector_lr_assim_lpp_doc
    output_vector_lr_assim_lpp_doc = np.zeros(kmax)
    # production rate of DOC by SPP :
    global output_lr_assim_spp_doc
    output_lr_assim_spp_doc = np.full((max_output_index,kmax),np.nan)
    global output_vector_lr_assim_spp_doc
    output_vector_lr_assim_spp_doc = np.zeros(kmax)
    # production rate of DOC by CYA :
    global output_lr_assim_cya_doc
    output_lr_assim_cya_doc = np.full((max_output_index,kmax),np.nan)
    global output_vector_lr_assim_cya_doc
    output_vector_lr_assim_cya_doc = np.zeros(kmax)
    # production rate of DOP by LPP :
    global output_lr_assim_lpp_dop
    output_lr_assim_lpp_dop = np.full((max_output_index,kmax),np.nan)
    global output_vector_lr_assim_lpp_dop
    output_vector_lr_assim_lpp_dop = np.zeros(kmax)
    # production rate of DOP by SPP :
    global output_lr_assim_spp_dop
    output_lr_assim_spp_dop = np.full((max_output_index,kmax),np.nan)
    global output_vector_lr_assim_spp_dop
    output_vector_lr_assim_spp_dop = np.zeros(kmax)
    # production rate of DON by LPP :
    global output_lr_assim_lpp_don
    output_lr_assim_lpp_don = np.full((max_output_index,kmax),np.nan)
    global output_vector_lr_assim_lpp_don
    output_vector_lr_assim_lpp_don = np.zeros(kmax)
    # production rate of DON by SPP :
    global output_lr_assim_spp_don
    output_lr_assim_spp_don = np.full((max_output_index,kmax),np.nan)
    global output_vector_lr_assim_spp_don
    output_vector_lr_assim_spp_don = np.zeros(kmax)
    # modifies pocp recycling towards Redfield ratio if PO4 is depleted :
    global output_ref_p_sw       
    output_ref_p_sw        = np.full((max_output_index,kmax),np.nan)
    global output_vector_ref_p_sw       
    output_vector_ref_p_sw        = np.zeros(kmax)
    # modifies pocn recycling towards Redfield ratio if DIN is depleted :
    global output_ref_n_sw       
    output_ref_n_sw        = np.full((max_output_index,kmax),np.nan)
    global output_vector_ref_n_sw       
    output_vector_ref_n_sw        = np.zeros(kmax)
    # add an additional POCP recycling if PO4 below Redfield but sufficient DIN :
    global output_lr_pocp        
    output_lr_pocp         = np.full((max_output_index,kmax),np.nan)
    global output_vector_lr_pocp        
    output_vector_lr_pocp         = np.zeros(kmax)
    # add an additional DOP recycling if PO4 is below Redfield but sufficient DIN :
    global output_lr_dop         
    output_lr_dop          = np.full((max_output_index,kmax),np.nan)
    global output_vector_lr_dop         
    output_vector_lr_dop          = np.zeros(kmax)
    # add an additional POCN recycling if DIN below Redfield but sufficient PO4 :
    global output_lr_pocn        
    output_lr_pocn         = np.full((max_output_index,kmax),np.nan)
    global output_vector_lr_pocn        
    output_vector_lr_pocn         = np.zeros(kmax)
    # add an additional DON recycling if DIN below Redfield but sufficient PO4 :
    global output_lr_don         
    output_lr_don          = np.full((max_output_index,kmax),np.nan)
    global output_vector_lr_don         
    output_vector_lr_don          = np.zeros(kmax)
    # depth dependent POC sinking speed :
    global output_w_poc_var      
    output_w_poc_var       = np.full((max_output_index,kmax),np.nan)
    global output_vector_w_poc_var      
    output_vector_w_poc_var       = np.zeros(kmax)
    # depth dependent POCN sinking speed :
    global output_w_pocn_var     
    output_w_pocn_var      = np.full((max_output_index,kmax),np.nan)
    global output_vector_w_pocn_var     
    output_vector_w_pocn_var      = np.zeros(kmax)
    # depth dependent POCP sinking speed :
    global output_w_pocp_var     
    output_w_pocp_var      = np.full((max_output_index,kmax),np.nan)
    global output_vector_w_pocp_var     
    output_vector_w_pocp_var      = np.zeros(kmax)
    # Solubility of CO2 [mol/kg/Pa] :
    global output_k0_co2         
    output_k0_co2          = [np.nan for l in range(max_output_index)]
    global output_scalar_k0_co2         
    output_scalar_k0_co2          = 0.0
    # Acid dissociation constant CO2 + 2 H2O <-> HCO3- + H3O+ [mol/kg] :
    global output_k1_co2         
    output_k1_co2          = [np.nan for l in range(max_output_index)]
    global output_scalar_k1_co2         
    output_scalar_k1_co2          = 0.0
    # Acid dissociation constant HCO3- + H2O <-> [CO3 2-] + H3O+ [mol/kg] :
    global output_k2_co2         
    output_k2_co2          = [np.nan for l in range(max_output_index)]
    global output_scalar_k2_co2         
    output_scalar_k2_co2          = 0.0
    # boron alkalinity [mol/kg] :
    global output_alk_boron      
    output_alk_boron       = [np.nan for l in range(max_output_index)]
    global output_scalar_alk_boron      
    output_scalar_alk_boron       = 0.0
    # hydrogen sulfide alkalinity [mol/kg] :
    global output_alk_h2s        
    output_alk_h2s         = [np.nan for l in range(max_output_index)]
    global output_scalar_alk_h2s        
    output_scalar_alk_h2s         = 0.0
    # water alkalinity [mol/kg] :
    global output_alk_water      
    output_alk_water       = [np.nan for l in range(max_output_index)]
    global output_scalar_alk_water      
    output_scalar_alk_water       = 0.0
    # phosphate alkalinity [mol/kg] :
    global output_alk_po4        
    output_alk_po4         = [np.nan for l in range(max_output_index)]
    global output_scalar_alk_po4        
    output_scalar_alk_po4         = 0.0
    # carbonate alkalinity [mol/kg] :
    global output_alk_co2        
    output_alk_co2         = [np.nan for l in range(max_output_index)]
    global output_scalar_alk_co2        
    output_scalar_alk_co2         = 0.0
    # error in total alkalinity calculation at the assumed pH [mol/kg] :
    global output_alk_residual   
    output_alk_residual    = [np.nan for l in range(max_output_index)]
    global output_scalar_alk_residual   
    output_scalar_alk_residual    = 0.0
    # derivative of carbonate alkalinity with respect to h3o [1] :
    global output_dalkc_dh3o     
    output_dalkc_dh3o      = [np.nan for l in range(max_output_index)]
    global output_scalar_dalkc_dh3o     
    output_scalar_dalkc_dh3o      = 0.0
    # derivative of residual_alk with respect to pH [mol/kg] :
    global output_dalkresidual_dpH
    output_dalkresidual_dpH = [np.nan for l in range(max_output_index)]
    global output_scalar_dalkresidual_dpH
    output_scalar_dalkresidual_dpH = 0.0
    # newly determined pH value [1] :
    global output_ph             
    output_ph              = [np.nan for l in range(max_output_index)]
    global output_scalar_ph             
    output_scalar_ph              = 0.0
    # h3o ion concentration [mol/kg] :
    global output_h3o            
    output_h3o             = [np.nan for l in range(max_output_index)]
    global output_scalar_h3o            
    output_scalar_h3o             = 0.0
    # co2 partial pressure [Pa] :
    global output_pco2           
    output_pco2            = [np.nan for l in range(max_output_index)]
    global output_scalar_pco2           
    output_scalar_pco2            = 0.0
    # Schmidt number for CO2 surface flux [1] :
    global output_schmidtnumber_co2
    output_schmidtnumber_co2 = [np.nan for l in range(max_output_index)]
    global output_scalar_schmidtnumber_co2
    output_scalar_schmidtnumber_co2 = 0.0
    # Schmidt number for oxygen surface flux [1] :
    global output_schmidtnumber_o2
    output_schmidtnumber_o2 = [np.nan for l in range(max_output_index)]
    global output_scalar_schmidtnumber_o2
    output_scalar_schmidtnumber_o2 = 0.0
    # Schmidt number for nitrogen surface flux [1] :
    global output_schmidtnumber_n2
    output_schmidtnumber_n2 = [np.nan for l in range(max_output_index)]
    global output_scalar_schmidtnumber_n2
    output_scalar_schmidtnumber_n2 = 0.0

    # tracers
    # dissolved molecular nitrogen :
    global output_t_n2           
    output_t_n2            = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_n2           
    output_vector_t_n2            = [0 for k in range(kmax)]
    # dissolved oxygen :
    global output_t_o2           
    output_t_o2            = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_o2           
    output_vector_t_o2            = [0 for k in range(kmax)]
    # dissolved inorganic carbon, treated as carbon dioxide :
    global output_t_dic          
    output_t_dic           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_dic          
    output_vector_t_dic           = [0 for k in range(kmax)]
    # ammonium :
    global output_t_nh4          
    output_t_nh4           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_nh4          
    output_vector_t_nh4           = [0 for k in range(kmax)]
    # nitrate :
    global output_t_no3          
    output_t_no3           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_no3          
    output_vector_t_no3           = [0 for k in range(kmax)]
    # phosphate :
    global output_t_po4          
    output_t_po4           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_po4          
    output_vector_t_po4           = [0 for k in range(kmax)]
    # small-cell phytoplankton :
    global output_t_spp          
    output_t_spp           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_spp          
    output_vector_t_spp           = [0 for k in range(kmax)]
    # zooplankton :
    global output_t_zoo          
    output_t_zoo           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_zoo          
    output_vector_t_zoo           = [0 for k in range(kmax)]
    # hydrogen sulfide :
    global output_t_h2s          
    output_t_h2s           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_h2s          
    output_vector_t_h2s           = [0 for k in range(kmax)]
    # sulfur :
    global output_t_sul          
    output_t_sul           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_sul          
    output_vector_t_sul           = [0 for k in range(kmax)]
    # total alkalinity :
    global output_t_alk          
    output_t_alk           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_alk          
    output_vector_t_alk           = [0 for k in range(kmax)]
    # limnic phytoplankton :
    global output_t_lip          
    output_t_lip           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_lip          
    output_vector_t_lip           = [0 for k in range(kmax)]
    # dissolved organic carbon :
    global output_t_doc          
    output_t_doc           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_doc          
    output_vector_t_doc           = [0 for k in range(kmax)]
    # phosphorus in dissolved organic carbon in Redfield ratio :
    global output_t_dop          
    output_t_dop           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_dop          
    output_vector_t_dop           = [0 for k in range(kmax)]
    # nitrogen in dissolved organic carbon in Redfield ratio :
    global output_t_don          
    output_t_don           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_don          
    output_vector_t_don           = [0 for k in range(kmax)]
    # colored dissolved organic carbon :
    global output_t_cdom         
    output_t_cdom          = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_cdom         
    output_vector_t_cdom          = [0 for k in range(kmax)]
    # diazotroph cyanobacteria :
    global output_t_cya          
    output_t_cya           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_cya          
    output_vector_t_cya           = [0 for k in range(kmax)]
    # detritus :
    global output_t_det          
    output_t_det           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_det          
    output_vector_t_det           = [0 for k in range(kmax)]
    # particulate organic carbon :
    global output_t_poc          
    output_t_poc           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_poc          
    output_vector_t_poc           = [0 for k in range(kmax)]
    # phosphorus in particulate organic carbon in Redfield ratio :
    global output_t_pocp         
    output_t_pocp          = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_pocp         
    output_vector_t_pocp          = [0 for k in range(kmax)]
    # nitrogen in particulate organic carbon in Redfield ratio :
    global output_t_pocn         
    output_t_pocn          = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_pocn         
    output_vector_t_pocn          = [0 for k in range(kmax)]
    # large-cell phytoplankton :
    global output_t_lpp          
    output_t_lpp           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_lpp          
    output_vector_t_lpp           = [0 for k in range(kmax)]
    # suspended iron phosphate :
    global output_t_ipw          
    output_t_ipw           = np.full((max_output_index,kmax),np.nan)
    global output_vector_t_ipw          
    output_vector_t_ipw           = [0 for k in range(kmax)]
    # sediment detritus :
    global output_t_sed          
    output_t_sed           = [np.nan for l in range(max_output_index)]
    global output_scalar_t_sed          
    output_scalar_t_sed           = 0.0
    # iron phosphate in sediment :
    global output_t_ips          
    output_t_ips           = [np.nan for l in range(max_output_index)]
    global output_scalar_t_ips          
    output_scalar_t_ips           = 0.0
    # sediment particular carbon :
    global output_t_sed_poc      
    output_t_sed_poc       = [np.nan for l in range(max_output_index)]
    global output_scalar_t_sed_poc      
    output_scalar_t_sed_poc       = 0.0
    # sediment particular organic N+C :
    global output_t_sed_pocn     
    output_t_sed_pocn      = [np.nan for l in range(max_output_index)]
    global output_scalar_t_sed_pocn     
    output_scalar_t_sed_pocn      = 0.0
    # sediment particular organic P+C :
    global output_t_sed_pocp     
    output_t_sed_pocp      = [np.nan for l in range(max_output_index)]
    global output_scalar_t_sed_pocp     
    output_scalar_t_sed_pocp      = 0.0

    # processes
    # assimilation of nitrate by large-cell phytoplankton :
    global output_p_no3_assim_lpp
    output_p_no3_assim_lpp = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_no3_assim_lpp
    output_vector_p_no3_assim_lpp = [0 for k in range(kmax)]
    # assimilation of ammonium by large-cell phytoplankton :
    global output_p_nh4_assim_lpp
    output_p_nh4_assim_lpp = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_nh4_assim_lpp
    output_vector_p_nh4_assim_lpp = [0 for k in range(kmax)]
    # assimilation of nitrate by small-cell phytoplankton :
    global output_p_no3_assim_spp
    output_p_no3_assim_spp = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_no3_assim_spp
    output_vector_p_no3_assim_spp = [0 for k in range(kmax)]
    # assimilation of ammonium by small-cell phytoplankton :
    global output_p_nh4_assim_spp
    output_p_nh4_assim_spp = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_nh4_assim_spp
    output_vector_p_nh4_assim_spp = [0 for k in range(kmax)]
    # fixation of dinitrogen by diazotroph cyanobacteria :
    global output_p_n2_assim_cya 
    output_p_n2_assim_cya  = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_n2_assim_cya 
    output_vector_p_n2_assim_cya  = [0 for k in range(kmax)]
    # Production of DOC by LIP :
    global output_p_assim_lpp_doc
    output_p_assim_lpp_doc = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_assim_lpp_doc
    output_vector_p_assim_lpp_doc = [0 for k in range(kmax)]
    # Production of DOC by SPP :
    global output_p_assim_spp_doc
    output_p_assim_spp_doc = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_assim_spp_doc
    output_vector_p_assim_spp_doc = [0 for k in range(kmax)]
    # Production of DOC by CYA :
    global output_p_assim_cya_doc
    output_p_assim_cya_doc = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_assim_cya_doc
    output_vector_p_assim_cya_doc = [0 for k in range(kmax)]
    # Production of DOP by LPP :
    global output_p_assim_lpp_dop
    output_p_assim_lpp_dop = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_assim_lpp_dop
    output_vector_p_assim_lpp_dop = [0 for k in range(kmax)]
    # Production of DOP by SPP :
    global output_p_assim_spp_dop
    output_p_assim_spp_dop = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_assim_spp_dop
    output_vector_p_assim_spp_dop = [0 for k in range(kmax)]
    # Production of DON by LPP :
    global output_p_nh4_assim_lpp_don
    output_p_nh4_assim_lpp_don = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_nh4_assim_lpp_don
    output_vector_p_nh4_assim_lpp_don = [0 for k in range(kmax)]
    # Production of DON by LPP :
    global output_p_no3_assim_lpp_don
    output_p_no3_assim_lpp_don = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_no3_assim_lpp_don
    output_vector_p_no3_assim_lpp_don = [0 for k in range(kmax)]
    # Production of DON by SPP :
    global output_p_nh4_assim_spp_don
    output_p_nh4_assim_spp_don = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_nh4_assim_spp_don
    output_vector_p_nh4_assim_spp_don = [0 for k in range(kmax)]
    # Production of DON by SPP :
    global output_p_no3_assim_spp_don
    output_p_no3_assim_spp_don = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_no3_assim_spp_don
    output_vector_p_no3_assim_spp_don = [0 for k in range(kmax)]
    # respiration of POCP :
    global output_p_pocp_resp    
    output_p_pocp_resp     = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_pocp_resp    
    output_vector_p_pocp_resp     = [0 for k in range(kmax)]
    # respiration of POCN :
    global output_p_pocn_resp    
    output_p_pocn_resp     = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_pocn_resp    
    output_vector_p_pocn_resp     = [0 for k in range(kmax)]
    # mortality of diazotroph cyanobacteria due to strong turbulence :
    global output_p_cya_mort_det_diff
    output_p_cya_mort_det_diff = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_cya_mort_det_diff
    output_vector_p_cya_mort_det_diff = [0 for k in range(kmax)]
    # recycling of detritus using oxygen (respiration) :
    global output_p_det_resp_nh4 
    output_p_det_resp_nh4  = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_det_resp_nh4 
    output_vector_p_det_resp_nh4  = [0 for k in range(kmax)]
    # recycling of detritus using nitrate (denitrification) :
    global output_p_det_denit_nh4
    output_p_det_denit_nh4 = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_det_denit_nh4
    output_vector_p_det_denit_nh4 = [0 for k in range(kmax)]
    # recycling of detritus using sulfate (sulfate reduction) :
    global output_p_det_sulf_nh4 
    output_p_det_sulf_nh4  = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_det_sulf_nh4 
    output_vector_p_det_sulf_nh4  = [0 for k in range(kmax)]
    # oxidation of hydrogen sulfide with nitrate :
    global output_p_h2s_oxno3_sul
    output_p_h2s_oxno3_sul = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_h2s_oxno3_sul
    output_vector_p_h2s_oxno3_sul = [0 for k in range(kmax)]
    # particle formation from DOC :
    global output_p_doc2pco      
    output_p_doc2pco       = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_doc2pco      
    output_vector_p_doc2pco       = [0 for k in range(kmax)]
    # particle formation from DOP :
    global output_p_dop2pocp     
    output_p_dop2pocp      = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_dop2pocp     
    output_vector_p_dop2pocp      = [0 for k in range(kmax)]
    # particle formation from DON :
    global output_p_don2pocn     
    output_p_don2pocn      = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_don2pocn     
    output_vector_p_don2pocn      = [0 for k in range(kmax)]
    # respiration of DOC :
    global output_p_doc_resp     
    output_p_doc_resp      = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_doc_resp     
    output_vector_p_doc_resp      = [0 for k in range(kmax)]
    # respiration of DOP :
    global output_p_dop_resp     
    output_p_dop_resp      = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_dop_resp     
    output_vector_p_dop_resp      = [0 for k in range(kmax)]
    # respiration of DON :
    global output_p_don_resp     
    output_p_don_resp      = np.full((max_output_index,kmax),np.nan)
    global output_vector_p_don_resp     
    output_vector_p_don_resp      = [0 for k in range(kmax)]
    # recycling of sedimentary detritus to ammonium using oxygen (respiration) :
    global output_p_sed_resp_nh4 
    output_p_sed_resp_nh4  = [np.nan for l in range(max_output_index)]
    global output_scalar_p_sed_resp_nh4 
    output_scalar_p_sed_resp_nh4  = 0.0
    # bio resuspension of sedimentary poc :
    global output_p_sed_biores_poc
    output_p_sed_biores_poc = [np.nan for l in range(max_output_index)]
    global output_scalar_p_sed_biores_poc
    output_scalar_p_sed_biores_poc = 0.0
    # burial of detritus deeper than max_sed :
    global output_p_sed_burial   
    output_p_sed_burial    = [np.nan for l in range(max_output_index)]
    global output_scalar_p_sed_burial   
    output_scalar_p_sed_burial    = 0.0
    # burial of iron PO4 :
    global output_p_ips_burial   
    output_p_ips_burial    = [np.nan for l in range(max_output_index)]
    global output_scalar_p_ips_burial   
    output_scalar_p_ips_burial    = 0.0
    # burial of poc deeper than max_sed :
    global output_p_poc_burial   
    output_p_poc_burial    = [np.nan for l in range(max_output_index)]
    global output_scalar_p_poc_burial   
    output_scalar_p_poc_burial    = 0.0
    # burial of pocn deeper than max_sed :
    global output_p_pocn_burial  
    output_p_pocn_burial   = [np.nan for l in range(max_output_index)]
    global output_scalar_p_pocn_burial  
    output_scalar_p_pocn_burial   = 0.0
    # burial of pocp deeper than max_sed :
    global output_p_pocp_burial  
    output_p_pocp_burial   = [np.nan for l in range(max_output_index)]
    global output_scalar_p_pocp_burial  
    output_scalar_p_pocp_burial   = 0.0
    # calcium carbonate dissolution from till sediments :
    global output_p_alk_btf      
    output_p_alk_btf       = [np.nan for l in range(max_output_index)]
    global output_scalar_p_alk_btf      
    output_scalar_p_alk_btf       = 0.0
