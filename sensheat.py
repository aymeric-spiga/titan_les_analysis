#! /usr/bin/env python

from ppclass import pp
import numpy as np

## classic constants
kappa = 0.4
## from planets
cp = 1040.
R = 299.
g = 1.35
## Charnay & Lebonnois 2012
z0 = 0.005 

theta0=94.
pref=92.e5

xx = 10
yy = 10

tt = 9.33065e8
tt = 9.33548e8
tt = None


tt6 = 9.332e8
tt12 = 9.336e8
#tt = tt12

rq = pp(file="wrfout_all.nc",t=tt,z=1e10,x=xx,y=yy,verbose=True)
rq.var = "MARS_TSURF" ; ts = rq.getf()
rq.var = "T" ; tp = rq.getf()
rq.var = "PTOT" ; pr = rq.getf()
rq.var = "PHTOT" ; ph = rq.getf()



tp = tp+theta0
print tp

import ppplot
pl = ppplot.plot1d()
pl.f = ts
pl.make()
pl.f = tp
pl.make()
ppplot.show()




print pr

ex = pref/pr
ex = ex**(R/cp)

tk = tp * ex

print tk



