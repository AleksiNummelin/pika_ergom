### --- pika-ERGOM --- ###

This repository contains a modified version of the standalone Python-based application of the Ecological ReGional Ocean Model (ERGOM).  The original Python code (and code templates) can be found at https://git.iow.de/ERGOM/Templates/src/branch/kpar-cdom/1d_python 

To run: 

**python code/run.py**

This generates netcdf files as outputs.  To plot stuff quickly, go to the file code/comp_cmems.py and choose the parameters

run_id =  # names of pika-ergom iterations

dpt    =  # depth

units  =  # units

var    =  # variable

ALSO make sure the variable name matches on the line below!

And then 

**python code/comp_cmems.py**

will generate time series comparing pika-ergom with cmems reanalysis for the given variable and depth.

To make a new pika-ergom run with different parameter choices:

1) Make a new run_id in the configure.py file
2) Edit parameter values in cgt_init_constants.py
3) Add your new run_id array in the comp_cmems.py file
