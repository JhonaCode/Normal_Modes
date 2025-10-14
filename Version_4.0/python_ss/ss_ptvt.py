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
import Parameters_ptvt   as cl


####################################################


#color='ocean_r'
color='RdBu_r'

#lonw=-150
#lone=-1
lonw=-120
lone=-1
lats=-45
latn=-15

lats=[lats,latn,6]
lons=[lonw+360,lone+360,6]


####################################################
#Nome para salval figura
#Ao nome é adicionado a variavel correspondente. 
#Nome da figura 

lev   =  200
#Data do plote
date='2023-02-01T00:00'
name  = 'anomaly_ptvt_feb_'
units=r'     [K m$^2$kg$^{-1}$s$^{-1}$]x10$^{-6}$'

bcolor=[-1.5,1.2,6]
levels= np.linspace(bcolor[0],bcolor[1],bcolor[2],endpoint=True)
dco=levels[1]-levels[0]
xlabel= f"São Sebastião - Contours: {bcolor[0]} to {bcolor[1]} by {dco:.1f}"

#"""
label = f"ERA5 Potential Vorticity Anomaly, \n  Analysis for February 2023 - Level: {lev} [hPa] "
ma.cartopy_plot(cl.anom_feb*1e6,lat=lats,lon=lons,bcolor=bcolor,color=color,units=units,figname=name+'era5',plotname=label  , show=True,contours=True,xtitle=xlabel,fmt='.2F')

