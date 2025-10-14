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
exp_name='ERA_5_SS'
path='%s/dados/bam/paulo.bonatti/Modal_Energetics_Data'%(computer)       
exp='ERA_5_PrecSS_Sfc'
ctl='ERA_5_PrecSS_Sfc.ctl'

fileg=path+'/'+exp+'/'+ctl

prec_ss = down.open_grads(fileg,exp_name)
