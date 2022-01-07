#! /bin/bash

./les.py ../initial/wrfout*red
./pblh.py
./vehf.py
./wmax.py
./hfx.py
