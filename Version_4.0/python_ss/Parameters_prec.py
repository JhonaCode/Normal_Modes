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

computer='/pesq'
path='%s/dados/bam/paulo.bonatti/Modal_Energetics_Data'%(computer)       

exp_name='ERA_5'
exp='ERA_5_PrecSS_Sfc'
ctl='ERA_5_PrecSS_Sfc.ctl'
fileg=path+'/'+exp+'/'+ctl
era5 = down.open_grads(fileg,exp_name)


exp_name='GPCP'
exp='GPCP_PrecSS_Sfc'
ctl='GPCP_PrecSS_Sfc.ctl'

#wrong ctl ???
#fileg=path+'/'+exp+'/'+ctl
#gpcp = down.open_grads(fileg,exp_name)

fileg = path+'/'+exp
gpcp  = down.open_netcdfs(fileg,exp_name)
#print(gpcp)

exp_name='BAMHY'
exp='BAMHY_PrecSS_Sfc/'
ctl='BAMHY_PrecSS_Sfc.ctl'
fileg=path+'/'+exp+'/'+ctl
bam = down.open_grads(fileg,exp_name)



