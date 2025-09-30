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
import Parameters_prec   as pr


####################################################
#Data do plote
datei='2024042300'
datef='2024050400'

dates=[datei,datef]

lonw=-80+360
lone=-20+360
lats=-45
latn=-15

color='ocean_r'
#color='gist_earth'

lats=[-55,-15,6]
lons=[-90+360,-30+360,5]

#Experimentos a plotar 
####################################################
#Dados MONAN
prec=[
      pr.era5,
      pr.bam,
      pr.monan,
      #pr.gpcp,
      ]

####################################################
#Variveis a comparara para cada experimento
vars  =[ 
             ['agpl'],
             ['agpl'],
             ['agpl'],
             #['agpl'],
            #
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


label = f"ERA5  Mean Precipitable Water, \n from 00Z23APR2024 to 00Z04MAY2024"
ma.cartopy_plot(mean[0],bcolor=[0,60,6],color=color,units='[kgm$^{-2}$]',figname=name+'era5'  ,plotname=label , show=False)

label = f"BAMHY Mean Precipitable Water, \n from 00Z23APR2024 to 00Z04MAY2024"
ma.cartopy_plot(mean[1],bcolor=[0,60,6],color=color,units='[kgm$^{-2}$]',figname=name+'bam'   ,plotname=label , show=False)

label = f"MONAN Mean Precipitable Water, \n from 00Z23APR2024 to 00Z04MAY2024"
ma.cartopy_plot(mean[2],bcolor=[0,60,6],color=color,units='[kgm$^{-2}$]',figname=name+'monan' ,plotname=label  , show=False)

plt.show()

