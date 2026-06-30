def cgt_get_description( name ):
#CGT_GET_DESCRIPTION get the description for a cgt output variable name
  
    description = '';
#  <tracers isOutput=1; isFlat=0>
#    if strcmpi(strtrim(name),strtrim('ERGOM'))
#        description = 'Ecological ReGional Ocean Model [mol/kg]';
#    end
#  </tracers>
#  <tracers isOutput=1; isFlat/=0>
#    if strcmpi(strtrim(name),strtrim('ERGOM'))
#        description = 'Ecological ReGional Ocean Model [mol/m2]';
#    end
#  </tracers>
#  <auxiliaries isOutput=1>
#    if strcmpi(strtrim(name),strtrim('ERGOM'))
#        description = 'Ecological ReGional Ocean Model';
#    end
#  </auxiliaries>
#  <processes isOutput=1>
#    if strcmpi(strtrim(name),strtrim('ERGOM'))
#        description = 'Ecological ReGional Ocean Model';
#    end
#  </processes>
    return(description)

