#! /usr/bin/env python
from ppclass import pp
import ppplot
import numpy as np
from ppcompute import smooth2diter

## options
from optparse import OptionParser ### TBR by argparse
parser = OptionParser()
parser.usage = "les.py netCDF_file(s)" #les.py becomes a commandline applicable to a netcdf file
(opt,files) = parser.parse_args()

recalculate = False
recalculate = True


nfilespinup = 2.
foutput = 400.
noutput = 100.
startlt = 6.
titanhour = 3600.*16.
## 1 Titan day == nearly 16 Earth days
## 1 Titan hour == 16/24 Earth days == 3600*24*16/24 == 3600*16


limpercent = 50.
#####


### constants
#t0 = 220.
#p0 = 610.
#r_cp = 1.0/4.4
#grav = 3.72
#R = 192.

#r_cp = 0.28758
#R = 299.

### from module_model_constants
g            = 1.35
r_d          = 290.6
cp           = 1051.
t0           = 94.
p0           = 1.45e5
p1000mb      = 1.45e5
reradius     = 1./2575500.0
wdaysec      = 1377665.28

r_cp = r_d / cp
grav = g



if recalculate:

    ## dimensions
    foo1,foo2,foo3,z,t = pp(file=files[0],var="T",x=0,y=0).getfd()
    nz,nt = z.size,t.size
    nf = len(files)
    print nf
    ntt = nt*nf
    
    ## arrays for time series
    tprimemean,tmean = np.zeros([ntt,nz]),np.zeros([ntt,nz])
    wprimemean,wmean = np.zeros([ntt,nz]),np.zeros([ntt,nz])
    wmax = np.zeros([ntt,nz])
    vehfmean = np.zeros([ntt,nz])
    pblh,pblh1,pblh2,pblh3 = np.zeros(ntt),np.zeros(ntt),np.zeros(ntt),np.zeros(ntt)
    tsurfmean = np.zeros([ntt])
    
    pl = ppplot.plot1d() # plot of the boundary layer height time evolution
    
    
    
    ## loop
    indt = -1
    
    for ff in files:
    
     print "### PROCESSING FILE:",ff
     print "### --> T"
     t = pp(file=ff,var="T").getf() + t0
     print "### --> W"
     w = pp(file=ff,var="W").getf()
     print "### --> PHTOT"
     geop = pp(file=ff,var="PHTOT").getf()
     geop = geop - np.mean(geop[:,0,:,:])
     print "### --> MARS_TSURF"
     tsurf = pp(file=ff,var="MARS_TSURF").getf()
     
     for tt in range(nt):
    
      indt = indt + 1
    
      tsurfmean[indt] = np.mean(tsurf[tt,:,:])
     
      for zz in range(nz):
        #print tt, indt
        tprime = t[tt,zz,:,:]
        tmean[indt,zz] = np.mean(tprime)
        tprime = tprime - tmean[indt,zz]
    
        wprime = w[tt,zz,:,:]
        wmean[indt,zz] = np.mean(wprime)
        wmax[indt,zz] = np.max(np.abs(wprime))
        wprime = wprime - wmean[indt,zz]
     
        vehfmean[indt,zz] = np.mean(tprime*wprime)
        tprimemean[indt,zz] = np.mean(tprime)
        wprimemean[indt,zz] = np.mean(wprime)
    
      ###########
      ## method 1: potential temperature profile
      #diff = np.abs(tmean[indt,2:]-tmean[indt,1])
      #wheremin = np.argmin(diff) + 2
      reft = 0.5*(tsurfmean[indt]+tmean[indt,0]) 
      reft = tmean[indt,0]
      diff = np.abs(tmean[indt,1:]-reft)
      wheremin = np.argmin(diff) + 1
      #print indt, tt
      pblh1[indt] = np.mean(geop[tt,wheremin,:,:]) / grav #Height of the geopotential of the boundary layer
      pblh[indt] = pblh1[indt]
      nnn = 1
    
      ###########
      ## method 2: minimum of vertical eddy heat flux
      wheremin = np.argmin(vehfmean[indt,:]) 
      pblh2[indt] = 1.1*np.mean(geop[tt,wheremin,:,:]) / grav
      ## sometimes spurious values caused by GW
      diff = 100.*np.abs(pblh2[indt]-pblh1[indt])/pblh1[indt]
      if diff > limpercent: 
          pblh2[indt] = np.nan
      else:
          pblh[indt] = pblh[indt]+pblh2[indt]
          nnn = nnn+1
    
      ###########
      ## method 3: convective motions
      diff = np.abs(wmax[indt,8:]-np.max(wmax[indt,:]/3.))
      wheremin = np.argmin(diff) + 8
      pblh3[indt] = np.mean(geop[tt,wheremin,:,:]) / grav
      ## sometimes spurious values caused by GW
      diff = 100.*np.abs(pblh3[indt]-pblh1[indt])/pblh1[indt]
      if diff > limpercent: 
          pblh3[indt] = np.nan
      else:
          pblh[indt] = pblh[indt]+pblh3[indt]
          nnn = nnn+1
   
      ########### 
      pblh[indt] = pblh[indt]/nnn
    
    
    
    ### remove small or negative values 
    #pblh = pblh[pblh > 100.]
    
    ## compute mean height
    altitude = np.mean(np.mean(np.mean(geop,axis=3),axis=2),axis=0)/grav
    altitude = altitude[0:nz]
   
    ## compute time axis 
    nnn = np.size(pblh1)
    xaxis = startlt + nfilespinup*foutput*noutput/titanhour + foutput*np.arange(nnn)/titanhour
    
    
    
    file1=open('pblh1.txt','w')
    for val in pblh1:
      file1.write("%8.3f\n"%(val))
    file1.close()
    
    file2=open('pblh2.txt','w')
    for val in pblh2:
      file2.write("%8.3f\n"%(val))
    file2.close()
    
    file3=open('pblh3.txt','w')
    for val in pblh3:
      file3.write("%8.3f\n"%(val))
    file3.close()
    
    file4=open('xaxis.txt','w')
    for val in xaxis:
      file4.write("%8.3f\n"%(val))
    file4.close()
    
    file5=open('pblh.txt','w')
    for val in pblh:
      file5.write("%8.3f\n"%(val))
    file5.close()
    

else:

    pass



#####
#pl = ppplot.plot2d() # shade of the vertical eddy heat flux time evolution
#pl.f = np.transpose(vehfmean[:,:])*1e5
#pl.y = altitude/1000.
#pl.x = xaxis
#pl.vmax = 15
#pl.vmin = -pl.vmax
#pl.div = 30
#pl.fmt = '%.0f'
#pl.ymax = 3.
#pl.ylabel = "altitude (km)"
#pl.xlabel = "simulated Titan local time (hours)"
#pl.nyticks = 10
#pl.colorbar = "seismic"
#pl.units = r'10$^{-5}$ K m s$^{-1}$'
#
##pl.makeshow()
#pl.makesave(mode="png",filename="vehf")
#
