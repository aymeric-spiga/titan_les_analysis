#! /bin/bash

ncrcat -O -v MARS_TSURF,HFX,FLUXSURF_SW,FLUXSURF_LW,FLUXABS_SW,FLXGRD wrfout_d01_9999-01-* FLUXSURF.nc
ncwa -O -a south_north,west_east FLUXSURF.nc FLUXSURFave.nc
ncap2 -O -s "surfbudget=FLUXSURF_SW-HFX+FLXGRD" FLUXSURFave.nc FLUXSURFavesum.nc

pp.py FLUXSURFavesum.nc -x 0 -y 0 \
  -v FLUXSURF_SW -v FLUXSURF_LW -v FLXGRD -v HFX -v surfbudget \
  -S -K '' \
  --xcoeff 0.00695 --xlabel Titan_hours_after_6AM \
  --ylabel W/m2 \
  -L '-' -L '-' -L '-' -L '-' -L '--' \
  -E '$\Phi_{SW}$' -E '$\Phi_{LW}$' -E '$G$' -E '$H_s$' -E '$\delta F$' \
  --ymin -4 --ymax 4 --nyticks 8 \
  --xmin 0 --xmax 12 --nxticks 12 \
  --xp 8 --yp 4 \
  -O png -o fluxsurf

# = \Phi_{SW} - (\Phi_{LW} + H_s)
