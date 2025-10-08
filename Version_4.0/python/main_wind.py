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

lonw=-150+360
lone=-20+360
lats=-60
latn=15

lats=[lats,latn,6]
lons=[lonw+360,lone+360,5]



####################################################
#Nome para salval figura
#Ao nome é adicionado a variavel correspondente. 
#Nome da figura 

lev   =  250
label = f"ERA5 Mean Zonal Wind, \n Level {lev} [hPa] for APRIL 2024"
#Data do plote
date  = '2024-04-01T15:00'
name  = 'uvel_'

#"""
ma.cartopy_plot(cl.era5_c,varname='uvel',lat=lats,lon=lons, lev=lev,date_str=date,bcolor=[0,50,6],color=color,units='[m$^{-1}$]',figname=name+'era5',plotname=label  , show=False)

lev   =850
label = f"ERA5 Mean Meridional Wind, \n Level {lev} [hPa] for APRIL 2024"
name  = 'vvel_'
ma.cartopy_plot(cl.era5_c,varname='vvel',lat=lats,lon=lons, lev=lev,date_str=date,bcolor=[-3,3,6],color=color,units=r'[m$^{-1}$]',figname=name+'era5',plotname=label  , show=False)

#"""

#Anommaly

#Data do plote
date ='2024-04-29T00:00'
label = f"ERA5 Zonal Wind Deviation,\n Level {lev} [hPa] for APRIL 00Z29APR2024"
lev   =250
color ='RdBu_r'
name  = 'anomaly_uvel_'

ma.cartopy_plot(cl.anom_u,lat=lats,lon=lons, lev=lev,date_str=date,bcolor=[-20,20,6],color=color,units='[m/s]',figname=name+'era5',plotname=label  , show=False)

label = f"BAM Zonal Wind Deviation,\n Level {lev} [hPa] for APRIL 00Z29APR2024"
ma.cartopy_plot(cl.anom_u_bam,lat=lats,lon=lons, lev=lev,date_str=date,bcolor=[-20,20,6],color=color,units='[m/s]',figname=name+'bam',plotname=label  , show=False)

label = f"MONAN Zonal Wind Deviation,\n Level {lev} [hPa] for APRIL 00Z29APR2024"
ma.cartopy_plot(cl.anom_u_monan,lat=lats,lon=lons, lev=lev,date_str=date,bcolor=[-20,20,6],color=color,units='[m/s]',figname=name+'monan',plotname=label  , show=False)

lev   = 850
label = f"ERA5 Meridional Wind Deviation, \n Level {lev} [hPa] for APRIL 00Z29APR2024"
name  = 'anomaly_vvel_'
ma.cartopy_plot(cl.anom_v,lat=lats,lon=lons, lev=lev,date_str=date,bcolor=[-20,20,6],color=color,units='[m/s]',figname=name+'era5',plotname=label  , show=False)

label = f"BAM Meridional Wind Deviation, \n Level {lev} [hPa] for APRIL 00Z29APR2024"
name  = 'anomaly_vvel_'
ma.cartopy_plot(cl.anom_v_bam,lat=lats,lon=lons, lev=lev,date_str=date,bcolor=[-20,20,6],color=color,units='[m/s]',figname=name+'bam',plotname=label  , show=False)

label = f"MONAN Meridional Wind Deviation, \n Level {lev} [hPa] for APRIL 00Z29APR2024"
name  = 'anomaly_vvel_'
ma.cartopy_plot(cl.anom_v_monan,lat=lats,lon=lons, lev=lev,date_str=date,bcolor=[-20,20,6],color=color,units='[m/s]',figname=name+'monan',plotname=label  , show=False)



plt.show()

