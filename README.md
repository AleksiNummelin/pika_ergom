# ~~~~~~~~~~~~~~~~ pika-ERGOM ~~~~~~~~~~~~~~~ #

# --- Why pika-ERGOM? --- #

Running a coupled hydrodynamic-biogeochemical model typically takes many times longer than running the hydrodynamics alone; hence several days or weeks of computer time are required for each model iteration.  In addition, biogeochemical models tyically contain a large number of poorly-constrained parameters.  A standalone (water-column) biogeochemical model such as **pika-ERGOM** can be used to understand biogeochemical processes and build intuition on how biogeochemical processes, but also to narrow down the parameter-space to be explored with the full 3D coupled model.  On an ordinary laptop, **pika-ERGOM** simulates one year (at a timestep of one hour) within less than a minute.   

# --- What is in this repository? --- #

This repository contains a modified version of the standalone Python-based application of the Ecological ReGional Ocean Model ERGOM.  The original Python code (and code templates) can be found at https://git.iow.de/ERGOM/Templates/src/branch/kpar-cdom/1d_python.  So far (10.07.2026) only the code itself has been edited at FMI, and thus the code templates are out of date and shouldn't be used.

Inside the _code_ directory there are two further sub-directories, _init_ and _physics_, providing initial biogeochemical conditions and physical forcing respectively.  The textfiles contained within were obtained from Hagen Radtke at the Leibniz Institute for Baltic Sea Research (IOW), and were used for initial testing.  Subsequently, the initial conditions and forcing have been updated at FMI as detailed below.

When run 'out-the-box', **pika-ERGOM** simulates 2020 conditions close to Utö in the Archipelago Sea (https://en-beta.ilmatieteenlaitos.fi/uto).  It can in principle be applied at any location where inputs for temperature, salinity, mixed layer depth, wind and solar radiation inputs can be obtained.

# --- What is ERGOM? --- #

The Ecological ReGional Ocean Model (ERGOM, https://ergom.net/) was developed at IOW in order to model biogeochemical cycles in the Baltic Sea.  It has most often been used online coupled to the Modular Ocean Model (MOM), but has also been coupled to various other hydrodynamic models, including via the Framework for Aquatic Biogeochemical Models (FABM, https://github.com/fabm-model/fabm).  As part of the Baltic Sea Monitoring Forecasting Centre (BALMFC, https://marine.copernicus.eu/about/producers/bal-mfc), ERGOM is coupled, via FABM to the Nucleus for European Modelling of the Ocean (NEMO, https://forge.nemo-ocean.eu/nemo).  NEMO-Ergom is also being developed further (https://github.com/atwelves/ERGOM) for application to the Gulf of Finland as part of the Coastal Waters under Pressure (CoWup, project https://cowup.fmi.fi/).

ERGOM is not in general distrubuted as a traditional code base.  Instead the ERGOM model is designed to be generated from two distinct components.  The first is a set of textfiles that describe the biogeochemical processes; the second is a template (or set of templates) that dictate how these processes should be written for compatibility with a given programming language and hydrodynamic model.  For standalone versions of ERGOM such as this one, where physical constraints are imposed as forcing without coupling to a hydrodynamic model, the template(s) simply translate the text files into the intended language - in this case, Python.

# --- What has changed with pika-ERGOM? --- #

The original Python implementation of ERGOM simulated a single year using textfiles as inputs and forcing.  In **pika-ERGOM** the code has been updated so that it can also read and write netCDF files.  Currently it is set up to read hourly temperature and salinity profiles from a netCDF file extracted from the BALMFC Physics Reanalysis (https://doi.org/10.48670/moi-00013).  Hourly mixed layer depth is also read in from this same reanalysis file, while hourly data for solar radiation and wind speed are read from a csv file, with the data obtained from Utö weather station via the FMI open-data portal (https://en.ilmatieteenlaitos.fi/open-data).  

In the original standalone version of ERGOM, diffusivity is read off from a text file as forcing.  In **pika-ERGOM**, diffusivity is instead calculated on-the-fly at each timestep from the wind speed and mixed layer inputs, using the vertical diffusivity calculator built for the Lagrangian modelling framework OpenDrift (https://github.com/OpenDrift/opendrift/tree/master/opendrift/models).  By default, **pika-ERGOM** uses the Large et al. (1994) parameterization of vertical diffusivity (https://doi.org/10.1029/94RG01872).

For oxygen, nitrate, phosphate and ammonium, initial conditions are taken from the BALMFC Biogeochemical Reanalysis (https://doi.org/10.48670/moi-00012).  Note that units for these variables are converted from mmol m⁻³ to mol kg⁻¹ for use in **pika-ERGOM**, and then are converted back to mmol m⁻³ when they are produced from **pika-ERGOM** as outputs.

Currently (10.07.2026), bottom stress and background water opacity are still read from the original text files, as are initial conditions for nitrogen, dissolved inorganic carbon, phytoplankton, zooplankton, hydrogen sulpihde, total alkalinity, detritus and sediment variables.  

# --- Instructions for use --- #

Once you have cloned this repository, no futher preparation steps are needed to run **pika-ERGOM**.  Simply execute

**python code/run.py**

and the model will run an iteration with the run_id "_ctrl_"

This generates netcdf files as outputs.  To plot stuff quickly, go to the file code/comp_cmems.py and choose the parameters

run_id =  [] # names of pika-ergom iterations

dpt    =  [] # depth 

units  =  [] # units

var    =  [] # variable

       .[]   # variables
       
Make sure the variable name matches on both lines!

And then 

**python code/comp_cmems.py**

will generate time series comparing pika-ergom with cmems reanalysis for the given variable and depth.

To make a new pika-ergom run with different parameter choices:

1) Make a new run_id in the configure.py file
2) Edit parameter values in cgt_init_constants.py
3) Add your new run_id array in the comp_cmems.py file
