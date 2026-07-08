import datetime as dt
import numpy as np

def load_weather(input_scalar, forcing_matrix, counter):
 
#  print("model day","forcing day")  
#  print(model_day,forcing_day)

  final_scalar = forcing_matrix.iloc[counter].values 
  
  if(final_scalar=="-"):
      # missing values
      final_scalar = input_scalar
  
  final_scalar = final_scalar.astype(float)

  return(final_scalar)

