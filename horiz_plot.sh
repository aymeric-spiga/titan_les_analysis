#! /bin/bash


pp.py \
 wrfout_d01_9999-01-07_22\:40\:00_red \
 --xp 8 --yp 6 -O png \
 -v HFX -o horiz_HFX \
 -t 0 \
 -C magma \
 --xcoeff 0.1 --ycoeff 0.1 \
 --xlabel "west-east axis (km)" --ylabel "south-north axis (km)" \
 -N 0 -M 2 -F '%.1f' -D 40 

pp.py \
 wrfout_d01_9999-01-07_22\:40\:00_red \
 --xp 8 --yp 6 -O png \
 -v USTM -o horiz_USTM \
 -t 0 \
 -C cividis \
 --xcoeff 0.1 --ycoeff 0.1 \
 --xlabel "west-east axis (km)" --ylabel "south-north axis (km)" \
 --mult 100 -U 'cm s$^{-1}$' \
 -N 0 -M 4 -F '%.1f' -D 40

