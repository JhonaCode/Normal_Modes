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
color='RdBu_r'

lonw=0#-150+360
lone=360#-0+360
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
date ='2023-02-14T00:00'
name  = 'anomaly_zgeo_'

bcolor=[-300,300,7]
levels= np.linspace(bcolor[0],bcolor[1],bcolor[2],endpoint=True)
dco=levels[1]-levels[0]
xlabel= f"São Sebastião - Contours: {bcolor[0]} to {bcolor[1]} by {dco:.1f}"


label = f"ERA5 Geoptential Height Anomaly, \n Analysis: for 00Z14FEB2024 Level: {lev} [hPa] "
ma.cartopy_plot(cl.anom_zgeo,lat=lats,lon=lons, lev=lev,date_str=date,bcolor=bcolor,color=color,units='[m]',figname=name+'era5',plotname=label  , show=False,xtitle=xlabel)

label = f"BAMHY Geoptential Height Anomaly, \n 3 Days Forecast: for 00Z14FEB2024 Level: {lev} [hPa] "
ma.cartopy_plot(cl.anom_zgeo_bam,lat=lats,lon=lons, lev=lev,date_str=date,bcolor=bcolor,color=color,units='[m]',figname=name+'bam',plotname=label  , show=False,xtitle=xlabel)




plt.show()

