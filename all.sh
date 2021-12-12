#! /bin/bash

./les.py wrfout*
./pblh.py
./vehf.py
./wmax.py
./hfx.py
