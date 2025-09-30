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
color='RdBu_r'

lonw=-180#-150+360
lone=180#-0+360
lats=-90
latn=90

lats=[lats,latn,5]
lons=[lonw,lone,5]



####################################################
#Nome para salval figura
#Ao nome é adicionado a variavel correspondente. 
#Nome da figura 

lev   =  500
#Data do plote
date ='2024-04-29T00:00'
name  = 'anomaly_zgeo_'

label = f"ERA5 Geoptential Height Anomaly, \n Level {lev} [hPa] for 00Z29APR2024"
ma.cartopy_plot(cl.anom_zgeo,lat=lats,lon=lons, lev=lev,date_str=date,bcolor=[-300,300,6],color=color,units='[m]',figname=name+'era5',plotname=label  , show=False)

label = f"BAMHY Geoptential Height Anomaly, \n Level {lev} [hPa] for 00Z29APR2024"
ma.cartopy_plot(cl.anom_zgeo_bam,lat=lats,lon=lons, lev=lev,date_str=date,bcolor=[-300,300,6],color=color,units='[m]',figname=name+'bam',plotname=label  , show=False)

label = f"MONAN Geoptential Height Anomaly, \n Level {lev} [hPa] for 00Z29APR2024"
ma.cartopy_plot(cl.anom_zgeo_monan,lat=lats,lon=lons, lev=lev,date_str=date,bcolor=[-300,300,6],color=color,units='[m]',figname=name+'monan',plotname=label  , show=False)


plt.show()

