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

mh='04'
exp_name='ERA_5_ptvt'
exp='ERA_5_ClimRS_Sfc'
ctl='ERA_5_ptvt_1940_2025_%s_200hPa.grib'%(mh)
fileg=path+'/'+exp+'/'+ctl
era5_april  = xr.open_dataset(fileg,engine='cfgrib')

mh='05'
exp_name='ERA_5_ptvt'
exp='ERA_5_ClimRS_Sfc'
ctl='ERA_5_ptvt_1940_2025_%s_200hPa.grib'%(mh)
fileg=path+'/'+exp+'/'+ctl
#era5_may  = down.open_grads(fileg,exp_name)
era5_may  = xr.open_dataset(fileg,engine='cfgrib')


mean_april_ptvt = era5_april['pv'].mean(axis=0)
mean_may_ptvt   = era5_may['pv'].mean(axis=0)

date='2024-04-01T00:00'
april_ptvt=ma.time_select(date,era5_april['pv'])
anom_april=april_ptvt-mean_april_ptvt


date='2024-05-01T00:00'
may_ptvt  =ma.time_select(date,era5_may['pv'])
anom_may=may_ptvt-mean_may_ptvt


