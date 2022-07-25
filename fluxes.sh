#! /bin/bash

ncrcat -O -v MARS_TSURF,HFX,FLUXSURF_SW,FLUXSURF_LW,FLUXABS_SW,FLXGRD ../wrfout_d01_9999-01-* FLUXSURF.nc
ncwa -O -a south_north,west_east FLUXSURF.nc FLUXSURFave.nc
ncap2 -O -s "HFX=-HFX;surfbudget=FLUXSURF_SW+HFX+FLXGRD" FLUXSURFave.nc FLUXSURFavesum.nc

pp.py FLUXSURFavesum.nc -x 0 -y 0 \
  --xoffset 4.18 \
  -v FLUXSURF_SW -v HFX -v FLXGRD -v surfbudget \
  -Q orange -Q blue -Q green -Q magenta \
  -F '%.1f' \
  -S -K '' \
  --xcoeff 0.00695 --xlabel 'Local time (Titan hours)' \
  --ylabel 'W m$^{-2}$' \
  -L '-' -L '-' -L '-' -L '--' -L '-' \
  -E '$\Phi_{SW}$' -E '$-H_s$' -E '$G$' -E '$\Phi_{SW}-H_s+G$' \
  --ymin -2 --ymax 2 --nyticks 18 \
  --xp 12 --yp 6 \
  -O png -o fluxsurf

# 0.00695
#--xmin 7.5 --xmax 19.4 --nxticks 12 \

# -v FLUXSURF_LW -Q red -E '$\Phi_{LW}$'

#titanpbl_exp_wind/
