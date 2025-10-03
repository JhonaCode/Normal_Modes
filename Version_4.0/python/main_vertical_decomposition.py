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
import Parameters_plot_vertical_modes as pa 

#print(pa.vm.variables)
#print(pa.vd.variables)


####################################################
color='ocean_r'

####################################################
#var=getattr(pa.vd,f'etn{pa.argum.cas}')
#exit()


#'draw title `1'caso' 'tita'\`1'titb'\`1Class 'cs' : H'za'='ha' to H'zb'='hb

