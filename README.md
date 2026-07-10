# ~~~~~~~~~~~~~~~~ pika-ERGOM ~~~~~~~~~~~~~~~ #

# --- Why pika-ERGOM? --- #

Running a coupled hydrodynamic-biogeochemical model typically takes many times longer than running the hydrodynamics alone; hence several days or weeks of computer time are required for each model iteration.  In addition, biogeochemical models tyically contain a large number of poorly-constrained parameters.  A standalone (water-column) biogeochemical model such as **pika-ERGOM** can be used to understand biogeochemical processes and build intuition on how biogeochemical processes, but also to narrow down the parameter-space to be explored with the full 3D coupled model.  On an ordinary laptop, **pika-ergom** simulates one year (at a timestep of one hour) within less than a minute.   

# --- What is in this repository? --- #

This repository contains a modified version of the standalone Python-based application of the Ecological ReGional Ocean Model ERGOM.  The original Python code (and code templates) can be found at https://git.iow.de/ERGOM/Templates/src/branch/kpar-cdom/1d_python.  So far (10.07.2026) only the code itself has been edited at FMI, and thus the code templates are out of date and shouldn't be used.

Inside the _code_ directory there are two further sub-directories, _init_ and _physics_, providing initial biogeochemical conditions and physical forcing respectively.  The textfiles contained within were obtained from Hagen Radtke at the Leibniz Institute for Baltic Sea Research (IOW), and were used for initial testing.  Subsewuently, the initial conditions and forcing have been updated at FMI.

When run 'out-the-box', **pika-ERGOM** simulates conditions close to Utö in the Archipelago Sea (https://en-beta.ilmatieteenlaitos.fi/uto).  It can in principle be applied at any location where inputs for temperature, salinity, mixed layer depth, wind and solar radiation inputs can be obtained.

# --- What is ERGOM? --- #

The Ecological ReGional Ocean Model (ERGOM, https://ergom.net/) was developed at IOW in order to model biogeochemical cycles in the Baltic Sea.  It has most often been used online coupled to the Modular Ocean Model (MOM), but has also been coupled to various other hydrodynamic models, including via the Framework for Aquatic Biogeochemical Models (FABM, https://github.com/fabm-model/fabm).  As part of the Baltic Sea Monitoring Forecasting Centre (BALMFC, https://marine.copernicus.eu/about/producers/bal-mfc), ERGOM is coupled, via FABM to the Nucleus for European Modelling of the Ocean (NEMO, https://forge.nemo-ocean.eu/nemo).  NEMO-Ergom is also being developed further (https://github.com/atwelves/ERGOM) for application to the Gulf of Finland as part of the Coastal Waters under Pressure (CoWup, project https://cowup.fmi.fi/).

ERGOM is not in general distrubuted as a traditional code base.  Instead the ERGOM model is designed to be generated from two distinct components.  The first is a set of textfiles that describe the biogeochemical processes; the second is a template (or set of templates) that dictate how these processes should be written for compatibility with a given programming language and hydrodynamic model.  For standalone versions of ERGOM such as this one, where physical constraints are imposed as forcing without coupling to a hydrodynamic model, the template (s) simply translate the text files into the intended language -- in this case, Python.

# --- What has changed with pika-ERGOM? --- #

The original Python implementation of ERGOM simulated a single year using textfiles as inputs and forcing.  In **pika-ERGOM** the code has been updated so that it can also read and write netCDF files.  Currently it is set up to read hourly temperature and salinity profiles from a netCDF file extracted from the BALMFC Physics Reanalysis (https://data.marine.copernicus.eu/product/BALTICSEA_MULTIYEAR_PHY_003_011/description).  Hourly mixed layer depth is also read in from this same reanalysis file, while hourly data for solar radiation and wind speed are read from a csv file, with the data obtained from Utö weather station via the FMI open-data portal (https://en.ilmatieteenlaitos.fi/open-data).  

In the original 

Currently (10.07.2026), bottom stress and background water opacity are still read from the original text files, as are initial conditions for...

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
