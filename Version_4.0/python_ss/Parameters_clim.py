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

exp_name='ERA_5_clima'
exp='ERA_5_ClimSS/'
ctl='ERA_5_ClimSS.ctl'
fileg=path+'/'+exp+'/'+ctl
era5_c = down.open_grads(fileg,exp_name)

exp_name='ERA_5_rain'
exp='ERA_5_RainSS/'
ctl='ERA_5_RainSS.ctl'
fileg=path+'/'+exp+'/'+ctl
era5_t = down.open_grads(fileg,exp_name)

date='2023-02-01T15:00'
feb_u   =ma.time_select(date,era5_c['uvel'])
feb_v   =ma.time_select(date,era5_c['vvel'])
feb_zgeo=ma.time_select(date,era5_c['zgeo'])

anom_u   =era5_t['uvel']-feb_u.values
anom_v   =era5_t['vvel']-feb_v.values
anom_zgeo=era5_t['zgeo']-feb_zgeo.values



#############################################
#############################################

dirdat='BAMHY_RainSS/'
filctl='BAMHY_RainSS.ctl'

exp_name='BAMHY_rain'
exp='BAMHY_RainSS/'
ctl='BAMHY_RainSS.ctl'
fileg=path+'/'+exp+'/'+ctl
bamt_t = down.open_grads(fileg,exp_name)

#linear interpolation
feb_u_interp = feb_u.interp(lat=bamt_t['uvel'].lat, lon=bamt_t['uvel'].lon,lev=bamt_t['uvel'].lev)
feb_v_interp = feb_v.interp(lat=bamt_t['vvel'].lat, lon=bamt_t['vvel'].lon,lev=bamt_t['vvel'].lev)

feb_zgeo_interp = feb_zgeo.interp(lat=bamt_t['zgeo'].lat, lon=bamt_t['zgeo'].lon,lev=bamt_t['zgeo'].lev)

#reindex to the nearest
#april_u_interp = april_u.reindex(lat=bamt_t.lat, lon=bamt_t.lon, lev=bamt_t.lev, method="nearest")

anom_u_bam=bamt_t['uvel']-feb_u_interp.values
anom_v_bam=bamt_t['vvel']-feb_v_interp.values
anom_zgeo_bam=bamt_t['zgeo']-feb_zgeo_interp.values

###############################################

