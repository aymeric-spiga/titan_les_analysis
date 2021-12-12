#! /usr/bin/env python
import ppplot
import numpy as np
import ppcompute

fieldname = "hfx"
#fieldname = "ustm"  
fieldname = "tsurf"

for fieldname in ["hfx","tsurf"]:

 fifi = np.loadtxt(fieldname+".txt")
 xaxis = np.loadtxt("xaxis.txt")

 win=20
 win=0
 win=50
 sfifi = ppcompute.smooth1d(fifi,window=win)
 sxaxis = ppcompute.smooth1d(xaxis,window=win)
 
 ppplot.changefont(12)
 fig = ppplot.figuref(x=12,y=8)
 pl = ppplot.plot1d(fig=fig)
 #pl.ymin = 0.
 pl.xmax = 16.
 pl.f = sfifi
 pl.x = sxaxis
 pl.linestyle = "-"
 pl.marker = ""
 #pl.ylabel = "Sensible heat flux (ground to atmosphere)"
 pl.xlabel = "Titan local time (hours)"
 pl.color = "b"
 pl.fmt = "%.2f"
 pl.make()
 pl.makesave(mode="png",filename=fieldname)

