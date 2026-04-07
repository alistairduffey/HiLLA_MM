This repo contains all code to produce the analysis and figures in Duffey et al., 2026: _The global climate response to High-Latitude Low-Altitude Stratospheric Aerosol Injection (HiLLA-SAI) (ESD)_

The main analysis is under 'Prod_analysis'. The 'regrid_E3SM' directory contains regridding maps, and a readme with how to on using the nco regridding tool which was used to regrid E3SM data from the native to a regular lat/lon grid. Several intermediate data files produced during the analysis are saved under 'intermediate_outputs/'. 

NOTE - this code was written to be run on the UK's JASMIN supercomputer, and uses file paths to the CEDA archive to work with CMIP6 and ARISE simulations in place, as well as to our archive of HiLLA data stored on a group-workspace on JASMIN. Reproducing the analysis outside of this system requires (1) downloading our HiLLA data from the [zenodo archive](https://doi.org/10.5281/zenodo.17466719), and (2) downloading various UKESM1.0 and CESM2-WACCM SSP2-4.5 and ARISE-SAI-1.5K simulation model outputs for their respective public stores (ESGF and NCAR GDEX), (3) updating file paths in the code to point to the reproducers local directory. 

My future projects will use the [Reflective Cloud Hub](https://reflectivecloud.github.io/Book/intro.html) in order to avoid these barriers to reproduction :)

This repo does not contain code to run the earth system simulations themselves (on three earth system models) or to do some initial postprocessing steps (e.g. converting UKESM's .pp file outputs into netcdf timeseries), which were carried out on the HPCs that completed the simulations (by Alistair Duffey, Walker Lee, and Lauren Wheeler, for UKESM, CESM and E3SM, respectively). 


[![DOI](https://zenodo.org/badge/1042630813.svg)](https://doi.org/10.5281/zenodo.17472546)
