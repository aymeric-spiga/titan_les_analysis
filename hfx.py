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
 sfifi = ppcompute.smooth1d(fifi,window=win)
 sxaxis = ppcompute.smooth1d(xaxis,window=win)
 
 ppplot.changefont(12)
 fig = ppplot.figuref(x=16,y=4)
 pl = ppplot.plot1d(fig=fig)

 ##########################
 pl.xmin = 7.5
 pl.xmax = 19.4
 pl.nxticks = 24
 ##########################
 pl.ymin = 93.25
 pl.ymax = 93.85
 pl.nyticks = 12
 ##########################

 pl.f = sfifi
 pl.x = sxaxis
 pl.linestyle = "-"
 pl.marker = ""
 pl.ylabel = "Surface temperature (K)"
 pl.xlabel = "Local time (Titan hours)"
 pl.color = "b"
 pl.fmt = "%.2f"
 pl.make()
 pl.makesave(mode="png",filename=fieldname)

