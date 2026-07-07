import datetime as dt
import numpy as np

def load_forcing( input_matrix, orig_date, start_date, end_date, kmax, old_i_to_load ):
  # if the same forcing is repeated several times, find the correct date
  # within the forcing period
  
  date=orig_date
  refdatetime = dt.datetime.combine(dt.date(1899,12,30),dt.time())
  while date >= end_date:
      date = date - (end_date-start_date)
  # seek the index to load
  # check if current index is still valid
  i=old_i_to_load
  newdate1=dt.datetime.combine(dt.date(int(input_matrix[i][0]),int(input_matrix[i][1]),int(input_matrix[i][2])),dt.time())+dt.timedelta(days=input_matrix[i][3]/24.0)
  newdate1=(newdate1 - refdatetime).total_seconds()/24/3600
  if i<input_matrix.shape[0]-1:
    newdate2=dt.datetime.combine(dt.date(int(input_matrix[i+1][0]),int(input_matrix[i+1][1]),int(input_matrix[i+1][2])),dt.time())+dt.timedelta(days=input_matrix[i+1][3]/24.0)
    newdate2=(newdate2 - refdatetime).total_seconds()/24/3600
  else:
    newdate2=date
  if (newdate1<date) & (newdate2>=date):
      #everything is fine, the current vector is good
      i_to_load=i
  else:
      if (newdate1 > date): #some time loop has finished and the date moved backwards behind the loaded date
          i=0
      while (i<input_matrix.shape[0]-1):
          newdate2=dt.datetime.combine(dt.date(int(input_matrix[i+1][0]),int(input_matrix[i+1][1]),int(input_matrix[i+1][2])),dt.time())+dt.timedelta(days=input_matrix[i+1][3]/24.0)
          newdate2=(newdate2 - refdatetime).total_seconds()/24/3600
          if newdate2<date:
              i=i+1
          else:
              i_to_load=i
              i=input_matrix.shape[0]+1000
      if i<=input_matrix.shape[0]: #found no good i in the middle => use the last one
          i_to_load=i=input_matrix.shape[0]-1

  # load the forcing
  final_vector=input_matrix[i_to_load,4:min(4+kmax,input_matrix.shape[1])]
  if len(final_vector)==1:
      final_vector=final_vector[0]
  return(final_vector, i_to_load)

