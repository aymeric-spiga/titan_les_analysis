#! /usr/bin/env python
import ppplot
import numpy as np
import ppcompute

xaxis = np.loadtxt("xaxis.txt")
altitude = np.loadtxt("altitude.txt")

yaa = np.loadtxt("vehf.txt")
nt = int(yaa[0])
nz = int(yaa[1])
vehfmean = np.zeros([nt,nz])
nnn = 1
for tt in range(nt):    
 for zz in range(nz):
  nnn = nnn+1 
  vehfmean[tt,zz] = yaa[nnn]

ppplot.changefont(12)
fig = ppplot.figuref(x=16,y=6)
pl = ppplot.plot2d(fig=fig) # shade of the vertical eddy heat flux time evolution
pl.f = np.transpose(vehfmean[:,:])*1e5
pl.y = altitude #/1000.
pl.x = xaxis
##########################
pl.ymin = 0.
pl.ymax = 4000.
pl.nyticks = 20
pl.xmin = 6
pl.xmax = 20
pl.nxticks = 14
##########################
pl.vmax = 12
pl.vmin = -pl.vmax
pl.div = 25
pl.fmt = '%.0f'
pl.ylabel = "altitude (km)"
pl.xlabel = "Local time (Titan hours)"
pl.colorbar = "seismic"
pl.units = r'10$^{-5}$ K m s$^{-1}$'

#pl.makeshow()
pl.makesave(mode="png",filename="vehf")

