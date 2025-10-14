#!/usr/bin/env python
"""
#################################
#################################
#PYTHON CODE TO PLOT DIFFERENS 
#MONAN_MPAS DATA USING 
#LES_GLOBAL_PYTHON.
#################################
#PYTHON CODE TO PLOT DIFFERENS 
# Data:17/09/2025
#################################
# By: Jhonatan A. A Manco
#################################
"""
####################################################
#IMPORTAR DO LES_GLOBAL_PYTHON
####################################################
#Para o plote temporal 
from     sources import functions as fnc 

import numpy as np

# Function with the definition of differents projetions
import   sources.cartopyplot   as ma 

import matplotlib.pyplot as plt

#Carregando os experimentos
####################################################
#ERA5 
import Parameters_clim   as cl


####################################################


#color='ocean_r'
#color='gist_ncar'
color='YlGnBu'

lonw=-00
lone=360
lats=-90
latn= 00

#color='ocean_r'
color='YlGnBu'

lats=[lats,latn,6]
lons=[lonw,lone,6]



####################################################
#Nome para salval figura
#Ao nome é adicionado a variavel correspondente. 
#Nome da figura 



bcolor=[-20,50,8]
levels= np.linspace(bcolor[0],bcolor[1],bcolor[2],endpoint=True)
dco=levels[1]-levels[0]
xlabel= f"São Sebastião - Contours: {bcolor[0]} to {bcolor[1]} by {dco:.1f}"

lev   =  200
label = f"ERA5 Mean Zonal Wind, \n Analysis: for February 2023 - Level: {lev} [hPa] "
#Data do plote
date  = '2023-02-01T15:00'
name  = 'mean_uvel_'+'era5'


#"""
ma.cartopy_plot(cl.era5_c,varname='uvel',lat=lats,lon=lons, lev=lev,date_str=date,bcolor=bcolor,color=color,units='[m$^{-1}$]',figname=name,plotname=label  , show=True,xtitle=xlabel)


lev   =  200
label = f"ERA5 Zonal Wind, \n Analysis: for 00Z14FEB2023 - Level: {lev} [hPa] "
#Data do plote
date  = '2023-02-14T00:00'
name  = 'uvel_'+'era5'
ma.cartopy_plot(cl.era5_t,varname='uvel',lat=lats,lon=lons, lev=lev,date_str=date,bcolor=bcolor,color=color,units='[m$^{-1}$]',figname=name,plotname=label  , show=True,xtitle=xlabel)

lev   =  200
label = f"BAMHY Zonal Wind, \n 3 Days Forecast: for 00Z14FEB2023 - Level: {lev} [hPa] "
#Data do plote
date  = '2023-02-14T00:00'
name  = 'uvel_'+'bam'
ma.cartopy_plot(cl.bamt_t,varname='uvel',lat=lats,lon=lons, lev=lev,date_str=date,bcolor=bcolor,color=color,units='[m$^{-1}$]',figname=name,plotname=label  , show=True,xtitle=xlabel)
#"""

#Anommaly

bcolor=[-30,30,6]
levels= np.linspace(bcolor[0],bcolor[1],bcolor[2],endpoint=True)
dco=levels[1]-levels[0]
xlabel= f"São Sebastião - Contours: {bcolor[0]} to {bcolor[1]} by {dco:.1f}"

#Data do plote
date ='2023-02-14T00:00'
lev   =200
color ='RdBu_r'

label = f"ERA5 Zonal Wind Deviation,\n  Analysis: for  00Z14FEB2023 - Level: {lev} [hPa]"
name  = 'anomaly_uvel_'+'era5'
ma.cartopy_plot(cl.anom_u,lat=lats,lon=lons, lev=lev,date_str=date,bcolor=[-30,30,6],color=color,units='[m/s]',figname=name,plotname=label  , show=False,xtitle=xlabel)

label = f"BAMHY Zonal Wind Deviation,\n 3 Days Forecast: for 00Z14FEB2023 - Level {lev} [hPa] "
name  = 'anomaly_uvel_'+'bam'
ma.cartopy_plot(cl.anom_u_bam,lat=lats,lon=lons, lev=lev,date_str=date,bcolor=[-30,30,6],color=color,units='[m/s]',figname=name,plotname=label  , show=False,xtitle=xlabel)

 

plt.show()

