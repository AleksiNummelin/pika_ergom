import datetime as dt
import numpy as np

def load_profiles(forcing_matrix,model_day,forcing_day,forcing_index,kmax):

  # check to see if we are on a new day
  if(model_day>forcing_day+1):  
      forcing_index = forcing_index + 1
      forcing_day   = forcing_day + 1

  # load the ocean profiles
  final_vector = forcing_matrix[forcing_index,:kmax]
  final_vector = np.squeeze(final_vector)
  return(final_vector,forcing_day,forcing_index)

