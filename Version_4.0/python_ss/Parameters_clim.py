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
exp='ERA_5_ClimRS/'
ctl='ERA_5_ClimRS.ctl'
fileg=path+'/'+exp+'/'+ctl
era5_c = down.open_grads(fileg,exp_name)

exp_name='ERA_5_rain'
exp='ERA_5_RainRS/'
ctl='ERA_5_RainRS.ctl'
fileg=path+'/'+exp+'/'+ctl
era5_t = down.open_grads(fileg,exp_name)

date='2024-04-01T15:00'
april_u   =ma.time_select(date,era5_c['uvel'])
april_v   =ma.time_select(date,era5_c['vvel'])
april_zgeo=ma.time_select(date,era5_c['zgeo'])

anom_u   =era5_t['uvel']-april_u.values
anom_v   =era5_t['vvel']-april_v.values
anom_zgeo=era5_t['zgeo']-april_zgeo.values



#############################################
#############################################

dirdat='BAMHY_RainRS/'
filctl='BAMHY_RainRS.ctl'

exp_name='BAMHY_rain'
exp='BAMHY_RainRS/'
ctl='BAMHY_RainRS.ctl'
fileg=path+'/'+exp+'/'+ctl
bamt_t = down.open_grads(fileg,exp_name)

#linear interpolation
april_u_interp = april_u.interp(lat=bamt_t['uvel'].lat, lon=bamt_t['uvel'].lon,lev=bamt_t['uvel'].lev)
april_v_interp = april_v.interp(lat=bamt_t['vvel'].lat, lon=bamt_t['vvel'].lon,lev=bamt_t['vvel'].lev)

april_zgeo_interp = april_zgeo.interp(lat=bamt_t['zgeo'].lat, lon=bamt_t['zgeo'].lon,lev=bamt_t['zgeo'].lev)

#reindex to the nearest
#april_u_interp = april_u.reindex(lat=bamt_t.lat, lon=bamt_t.lon, lev=bamt_t.lev, method="nearest")

anom_u_bam=bamt_t['uvel']-april_u_interp.values
anom_v_bam=bamt_t['vvel']-april_v_interp.values
anom_zgeo_bam=bamt_t['zgeo']-april_zgeo_interp.values

###############################################
###############################################

dirdat='MONAN_RainRS/'
filctl='MONAN_RainRS.ctl'

exp_name='MONAN_rain'
exp='MONAN_RainRS/'
ctl='MONAN_RainRS.ctl'
fileg=path+'/'+exp+'/'+ctl
monan_t = down.open_grads(fileg,exp_name)

#linear interpolation
april_u_interp_monan = april_u.interp(lat=monan_t['uvel'].lat, lon=monan_t['uvel'].lon,lev=monan_t['uvel'].lev)
april_v_interp_monan = april_v.interp(lat=monan_t['vvel'].lat, lon=monan_t['vvel'].lon,lev=monan_t['vvel'].lev)
april_zgeo_interp_monan = april_zgeo.interp(lat=monan_t['zgeo'].lat, lon=monan_t['zgeo'].lon,lev=monan_t['zgeo'].lev)


anom_u_monan=monan_t['uvel']-april_u_interp_monan.values
anom_v_monan=monan_t['vvel']-april_v_interp_monan.values
anom_zgeo_monan=monan_t['zgeo']-april_zgeo_interp_monan.values


"""
exp_name='GPCP'
exp='GPCP_PrecRS_Sfc'
ctl='GPCP_PrecRS_Sfc.ctl'

#wrong ctl ???
#fileg=path+'/'+exp+'/'+ctl
#gpcp = down.open_grads(fileg,exp_name)

fileg = path+'/'+exp
gpcp  = down.open_netcdfs(fileg,exp_name)
#print(gpcp)

exp_name='BAMHY'
exp='BAMHY_PrecRS_Sfc/'
ctl='BAMHY_PrecRS_Sfc.ctl'
fileg=path+'/'+exp+'/'+ctl
bam = down.open_grads(fileg,exp_name)

exp_name='MONAN'
exp='MONAN_PrecRS_Sfc/'
ctl='MONAN_PrecRS_Sfc.ctl'
fileg=path+'/'+exp+'/'+ctl
monan = down.open_grads(fileg,exp_name)
"""
