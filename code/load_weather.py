import datetime as dt
import numpy as np

def load_weather(input_scalar, forcing_matrix, counter):

  final_scalar = forcing_matrix.iloc[counter].values #assumes that forcing and model both have hourly timestep... 
  
  if(final_scalar=="-"):
      # deal with missing values by using last valid measurement
      final_scalar = input_scalar
  
  #final_scalar = final_scalar.astype(float)

  return np.asarray(final_scalar, dtype=float).item()

