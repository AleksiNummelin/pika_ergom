import datetime as dt
import numpy as np

def load_qsw(input_scalar, forcing_matrix, counter):
 
#  print("model day","forcing day")  
#  print(model_day,forcing_day)

  final_scalar = forcing_matrix.iloc[counter].values 
#  print(final_scalar)
  if(final_scalar=="-"):
      final_scalar = input_scalar
  
  final_scalar = final_scalar.astype(float)

  # don't allow negative values
  final_scalar = np.nanmax(final_scalar,0)
  return(final_scalar)

