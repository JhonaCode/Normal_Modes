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
import  sources.cartopyplot   as ma 

import  grads.data_own   as down

import  xarray as xr

computer='/pesq'
path='%s/dados/bam/paulo.bonatti/Modal_Energetics_Data'%(computer)       

mh='02'
exp_name='ERA_5_ptvt'
exp='ERA_5_ClimSS_Sfc'
ctl='ERA_5_ptvt_1940_2025_%s_200hPa.ctl'%(mh)
fileg=path+'/'+exp+'/'+ctl
#era5_feb_1  = down.open_grads(fileg,exp_name)

grib='ERA_5_ptvt_1940_2025_%s_200hPa.grib'%(mh)
fileg=grib
era5_feb  = xr.open_dataset(fileg,engine='cfgrib')


mean_feb_ptvt = era5_feb['pv'].mean(axis=0)

date='2023-02-01T00:00'
feb_ptvt=ma.time_select(date,era5_feb['pv'])
anom_feb=feb_ptvt-mean_feb_ptvt




