Map file downloaded from https://web.lcrc.anl.gov/public/e3sm/diagnostics/maps/

nco regridding follows directions here https://e3sm.atlassian.net/wiki/spaces/DOC/pages/754286611/Regridding+E3SM+Data+with+ncremap

from preprint https://essopenarchive.org/doi/full/10.22541/essoar.175097464.44666291/v1
, the grid we want to start from is ne30pg2. 

on jasmin, start with 

module load esmvaltool


then run (to one directory at a time):

ncremap -m /home/users/a_duffey/UKESM_runs_analysis/HiLLA-SAI/Multimodel_Analysis/Regridding_E3SM/maps/map_ne30pg2_to_cmip6_180x360_aave.20200201.nc -I burdenSO4/ -O regridded/burdensSO4
