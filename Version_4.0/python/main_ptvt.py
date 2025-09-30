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
import Parameters_ptvt   as cl


####################################################


#color='ocean_r'
color='RdBu_r'

#lonw=-150
#lone=-1
lonw=-150
lone=-1
lats=-75
latn=0

lats=[lats,latn,5]
lons=[lonw,lone,5]


####################################################
#Nome para salval figura
#Ao nome é adicionado a variavel correspondente. 
#Nome da figura 

lev   =  200
#Data do plote
date ='2024-04-29T00:00'
name  = 'anomaly_ptvt_april_'

#"""
label = f"ERA5 Potential Vorticity Anomaly, \n Level {lev} [hPa] for APRIL 2024"
ma.cartopy_plot(cl.anom_april*1e6,lat=lats,lon=lons,bcolor=[-2,2,6],color=color,units=r'[K m$^2$kg$^{-1}$s$^{-1}$]x10$^{-6}$',figname=name+'era5',plotname=label  , show=False,contours=False)

name  = 'anomaly_ptvt_may_'

label = f"ERA5 Potential Vorticity Anomaly, \n Level {lev} [hPa] for MAY 2024"
ma.cartopy_plot(cl.anom_may*1e6,lat=lats,lon=lons,bcolor=[-2,2,6],color=color,units=r'[K m$^2$kg$^{-1}$s$^{-1}$]x10$^{-6}$',figname=name+'era5',plotname=label  , show=False,contours=False)

plt.show()
