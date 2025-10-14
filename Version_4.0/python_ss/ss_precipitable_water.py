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

import numpy as np

import matplotlib.pyplot as plt

#Carregando os experimentos
####################################################
#ERA5 
import Parameters_prec   as pr


####################################################
#Data do plote
datei='2023021600'
datef='2023022000'

dates=[datei,datef]

lonw=-80
lone=-20
lats=-45
latn=-15

#color='ocean_r'
color='YlGnBu'

lats=[lats,latn,6]
lons=[lonw+360,lone+360,6]

#Experimentos a plotar 
####################################################
#Dados MONAN
prec=[
      pr.era5,
      pr.bam,
      ]

####################################################
#Variveis a comparara para cada experimento
vars  =[ 
             ['agpl'],
             ['agpl'],
            ]

####################################################
#Nome para salval figura
#Ao nome é adicionado a variavel correspondente. 
#Nome da figura 
name  = 'mean_precipitable_water_'

####################################################
#Fator de multiplicacao para cada variavel.
#
var2  =   [[1],[1],[1],[1]]

mean=fnc.mean(prec,vars,dates,var2=var2,lats=lats,lons=lons)

bcolor=[0,60,6]
levels= np.linspace(bcolor[0],bcolor[1],bcolor[2],endpoint=True)
dco=levels[1]-levels[0]
xlabel= f"São Sebastião - Contours: {bcolor[0]} to {bcolor[1]} by {dco:.1f}"

label = f"ERA5  Mean Precipitable Water, \n Analysis: from 00Z16FEB2023 to 00Z20FEB2023"
ma.cartopy_plot(mean[0],bcolor=bcolor,color=color,units='[kgm$^{-2}$]',figname=name+'era5'  ,plotname=label , show=False,xtitle=xlabel)

label = f"BAMHY Mean Precipitable Water, \n 3 Days Forecast from 00Z16FEB2023 to 00Z20FEB2023"
ma.cartopy_plot(mean[1],bcolor=bcolor,color=color,units='[kgm$^{-2}$]',figname=name+'bam'   ,plotname=label , show=False,xtitle=xlabel)

plt.show()

