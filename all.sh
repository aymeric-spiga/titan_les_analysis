#! /bin/bash

./fluxes.sh
./les.py wrfout*red
./pblh.py
./vehf.py
./wmax.py
./hfx.py
