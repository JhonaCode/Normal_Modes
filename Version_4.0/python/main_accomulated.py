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

lats=[-40,-15,6]
lons=[-90+360,-30+360,5]

#Experimentos a plotar 
####################################################
#Dados MONAN
prec=[
      pr.era5,
      pr.gpcp,
      pr.bam,
      pr.monan,
      ]

####################################################
#Variveis a comparara para cada experimento
vars  =[ 
             ['prec'],
             ['precip'],
             ['prec'],
             ['prec'],
            ]

####################################################
#Nome para salval figura
#Ao nome é adicionado a variavel correspondente. 
#Nome da figura 
name  = 'accomulated_precipitation_'

####################################################
#Fator de multiplicacao para cada variavel.
#
var2  =   [[1],[1],[1],[1]]

acomm=fnc.accomulate(prec,vars,dates,var2=var2,lats=lats,lons=lons)

label = f"ERA5 Accumulated Precipitation, \n from 00Z29APR2024 to 00Z04MAY2024"
ma.cartopy_plot(acomm[0],bcolor=[0,300,6],color=color,units='[mm]',figname=name+'era5',plotname=label , show=False,)
label = f"GPCP Accumulated Precipitation, \n from 00Z29APR2024 to 00Z04MAY2024"
ma.cartopy_plot(acomm[1],bcolor=[0,300,6],color=color,units='[mm]',figname=name+'gpcp', plotname=label , show=False)
label = f"BAMHY Accumulated Precipitation, \n from 00Z29APR2024 to 00Z04MAY2024"
ma.cartopy_plot(acomm[2],bcolor=[0,300,6],color=color,units='[mm]',figname=name+'bam' , plotname=label , show=False)
label = f"MONAN Accumulated Precipitation, \n from 00Z29APR2024 to 00Z04MAY2024"
ma.cartopy_plot(acomm[3],bcolor=[0,300,6],color=color,units='[mm]',figname=name+'monan',plotname=label , show=False)

plt.show()

