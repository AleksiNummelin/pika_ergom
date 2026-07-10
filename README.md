# ~~~~~~~~~~~~~~~~ pika-ERGOM ~~~~~~~~~~~~~~~ #

# --- What is in this repository? --- #

This repository contains a modified version of the standalone Python-based application of the Ecological ReGional Ocean Model ERGOM.  The original Python code (and code templates) can be found at https://git.iow.de/ERGOM/Templates/src/branch/kpar-cdom/1d_python.  So far (10.07.2026) only the code itself has been edited at FMI, and thus the code templates are out of date and shouldn't be used.

Inside the _code_ directory there are two further sub-directories, _init_ and _physics_, providing initial biogeochemical conditions and physical forcing respectively.  The textfiles contained within were obtained from Hagen Radtke at the Leibniz Institute for Baltic Sea Research (IOW), and were used for initial testing.  Subsewuently, the initial conditions and forcing have been updated at FMI.

# --- What is ERGOM? --- #

The Ecological ReGional Ocean Model (ERGOM, https://ergom.net/) was developed at IOW in order to model biogeochemical cycles in the Baltic Sea.  It has most often been used online coupled to the Modular Ocean Model (MOM), but has also been coupled to various other hydrodynamic models, including via the Framework for Aquatic Biogeochemical Models (FABM, https://github.com/fabm-model/fabm).  As part of the Baltic Sea Monitoring Forecasting Centre (BALMFC, https://marine.copernicus.eu/about/producers/bal-mfc), ERGOM is coupled, via FABM to the Nucleus for European Modelling of the Ocean (NEMO, https://forge.nemo-ocean.eu/nemo).  NEMO-Ergom is also being developed further (https://github.com/atwelves/ERGOM) for application to the Gulf of Finland as part of the Coastal Waters under Pressure (CoWup, ) project



# --- What is pika-ERGOM? --- #

# --- Instructions for use --- #

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
