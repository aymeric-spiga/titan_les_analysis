#! /usr/bin/env python
from ppclass import pp
import matplotlib.pyplot as mpl
import numpy as np
import ppplot

u = pp()
#u.file = "/home/aymeric/Big_Data/ustar.101x101x201.CaseA.w30_zipbl.nc"
#u.file = "BIGLES10m_wind5_USTM_9-11.nc"
u.file = "/home/aspiga/data/TITAN_LES/HF1.1/wrfout_d01_9999-01-07_00:26:40"
u.file = "/home/aspiga/data/TITAN_LES/HF1.1/wrfout_d01_9999-01-01_22:13:20"
u.file = "wrfout_d01_9999-01-07_00:26:40"
#u.file = "wrfout_d01_9999-01-05_15:06:40"
u.var = "W"
u.x = "0,1000"
u.y = "0,1000"
u.z = 3

tttall = "0,1e10"

for yeah in [tttall]:
#for yeah in ["0"]:
  u.t = yeah
  u.compute = "nothing"
  ustm = u.getf()
  
  u.var = "U"
  uu = u.getf()
  u.var = "V"
  vv = u.getf()
  print uu.shape
  print vv.shape
  ustm = np.sqrt(uu[:,:,:,:100]**2 + vv[:,:,:100,:]**2)
  #ustm = uu[:,:,:,:100]#+vv[:,:,:100,:]

  #u.compute = "max" ; zemax = u.getf()
  #u.compute = "min" ; zemin = u.getf()
  #u.compute = "mean" ; zemean = u.getf()

  zemax = np.max(ustm)
  print zemax
  zemin = np.min(ustm)
  zemean = np.mean(ustm)

  ustm = ustm - zemean
  zemax = np.max(ustm)
  zemin = np.min(ustm)
  zemean = np.mean(ustm)


  ppplot.figuref(x=6,y=4)
  dval = (zemax-zemin)/100
  bins = np.arange(zemin,zemax,dval)
  hh = mpl.hist(np.ravel(ustm),bins,log=True)
  print hh
  mpl.title("$\mu$=%.2f / m=%.2f / M=%.2f" % (zemean,zemin,zemax))
  #mpl.xlabel('Friction velocity $u_{\star}$ (m s$^{-1}$)')
  mpl.xlabel('Horizontal wind speed (m s$^{-1}$)')
  mpl.ylabel('Population')
  ppplot.save(mode="png",filename="roughness_hist")
  ppplot.close()


u.x = None
u.y = None
u.t = tttall
u.compute = "max"
u.xcoeff = 0.01
u.ycoeff = 0.01
u.xlabel = "x (km)"
u.ylabel = "y (km)"
u.title = 'maximum $u\star$'
u.vmin = 0.4
u.vmax = 1.1
u.div = 70
u.colorbar = "gist_ncar" #"CMRmap"
u.fmt = "%.3f"
u.xp = 10
u.yp = 8
u.filename = "maxustm"
u.includedate = False
u.out = "png"
u.getplot()

