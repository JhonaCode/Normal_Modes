"""
!/usr/bin/python
 -*- coding: UTF-8 -*-
##################################################
PYTHON CODE TO PLOT DIFFERENS 
MODEL NORMAL  DATA USING CARTOPY AND XARRAY. 
##################################################
 By: Jhonatan A. A Manco
##################################################
"""

import  grads.data_own   as down
import  pandas           as pd


computer='/pesq'
exp_name='ERA_5'
path='%s/dados/bam/paulo.bonatti/Modal_Energetics_Data'%(computer)       
exp='ERA_5_PrecRS_Sfc'
ctl='ERA_5_PrecRS_Sfc.ctl'

fileg=path+'/'+exp+'/'+ctl

prec = down.open_grads(fileg,exp_name)

#print(prec.time)
#prec
#agcl
#print(prec.variables.values)
#print(prec.variables.values)

