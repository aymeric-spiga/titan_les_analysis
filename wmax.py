#! /usr/bin/env python
import ppplot
import numpy as np
import ppcompute

xaxis = np.loadtxt("xaxis.txt")
altitude = np.loadtxt("altitude.txt")

yaa = np.loadtxt("wmax.txt")
nt = int(yaa[0])
nz = int(yaa[1])
wmax = np.zeros([nt,nz])
nnn = 1
for tt in range(nt):    
 for zz in range(nz):
  nnn = nnn+1 
  wmax[tt,zz] = yaa[nnn]


ppplot.changefont(12)
fig = ppplot.figuref(x=16,y=6)
pl = ppplot.plot2d(fig=fig) # shade of the vertical eddy heat flux time evolution
pl.f = np.transpose(wmax[:,:])
pl.y = altitude #/1000.
pl.x = xaxis
##########################
pl.ymin = 0.
pl.ymax = 3200.
pl.nyticks = 16
pl.xmin = 6
pl.xmax = 24
pl.nxticks = 20
##########################
pl.vmax = 1.
pl.vmin = 0.
pl.div = 40
pl.fmt = '%.2f'
pl.ylabel = "altitude (km)"
pl.xlabel = "Local time (Titan hours)"
pl.colorbar = "hot"
pl.units = r'm s$^{-1}$'

#pl.makeshow()
pl.makesave(mode="png",filename="wmax")

