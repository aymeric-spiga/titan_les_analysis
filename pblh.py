#! /usr/bin/env python
import ppplot
import numpy as np
import ppcompute
  
pblh1 = np.loadtxt("pblh1.txt")
pblh2 = np.loadtxt("pblh2.txt")
pblh3 = np.loadtxt("pblh3.txt")
pblh = np.loadtxt("pblh.txt")
xaxis = np.loadtxt("xaxis.txt")

## correcting case with no mixing layer
## ... (index 0 cannot be caught in procedure)
#w = pblh1 < 100. ; pblh1[w] = 0.
#w = pblh < 100. ; pblh[w] = 0.

win=100
#win=0
#win=3
#win=5
#win=10

spblh = ppcompute.smooth1d(pblh,window=win)
sxaxiss = ppcompute.smooth1d(xaxis,window=win)
win=0
spblh1 = ppcompute.smooth1d(pblh1,window=win)
sxaxis = ppcompute.smooth1d(xaxis,window=win)

w = np.isfinite(pblh2)
spblh2 = ppcompute.smooth1d(pblh2[w],window=win)
sxaxis2 = ppcompute.smooth1d(xaxis[w],window=win)

w = np.isfinite(pblh3)
spblh3 = ppcompute.smooth1d(pblh3[w],window=win)
sxaxis3 = ppcompute.smooth1d(xaxis[w],window=win)

ppplot.changefont(12)
fig = ppplot.figuref(x=12,y=8) ## 16 6
pl = ppplot.plot1d(fig=fig) # plot of the boundary layer height time evolution
##########################
pl.ymin = 0.
pl.ymax = 3200.
pl.nyticks = 32
pl.xmin = 6
pl.xmax = 24
pl.nxticks = 20
##########################
pl.f = spblh1
pl.x = sxaxis
pl.linestyle = ""
pl.marker = "x"
pl.ylabel = "PBL mixing height (m)"
pl.xlabel = "Local time (Titan hours)"
pl.legend = "potential temperature profile"
pl.color = "c"
#pl.modx = 24
pl.make()
pl.f = spblh2
pl.x = sxaxis2
pl.legend = "eddy heat flux top inversion"
pl.color = "m"
pl.make()
pl.f = spblh3
pl.x = sxaxis3
pl.legend = "plumes' vertical velocities"
pl.color = "y"
pl.make()
pl.f = spblh
pl.x = sxaxiss
pl.linestyle = '-'
pl.marker = ""
pl.color = "k"
pl.legend = "all-method average (smoothed)"
#pl.makeshow()
pl.makesave(mode="png",filename="pblh")

