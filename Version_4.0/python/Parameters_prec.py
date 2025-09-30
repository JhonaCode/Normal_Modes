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
exp='ERA_5_PrecRS_Sfc'
ctl='ERA_5_PrecRS_Sfc.ctl'
fileg=path+'/'+exp+'/'+ctl
era5 = down.open_grads(fileg,exp_name)

#print(era5.variables)
#exit()

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
import xarray as xr
from glob import glob

# Directory where your files are
path = "/pesq/dados/bam/paulo.bonatti/Modal_Energetics_Data/GPCP_PrecRS_Sfc"

# Pattern for daily GPCP files
files = sorted(glob(os.path.join(path, "gpcp_v01r03_daily_d*.nc")))

valid_files = []
for f in files:
    size = os.path.getsize(f)
    # GPCP daily NetCDFs must be multiple of 259200 bytes
    if size % 259200 == 0:
        valid_files.append(f)
    else:
        print(f"⚠️ Skipping incomplete file: {os.path.basename(f)} (size {size})")

print(f"\n✅ Valid files: {len(valid_files)} / {len(files)}")

# Example: open with xarray
if valid_files:
    ds = xr.open_mfdataset(valid_files, combine="by_coords")
    print(ds)
"""
"""
import xarray as xr
from glob import glob

path = "/pesq/dados/bam/paulo.bonatti/Modal_Energetics_Data/GPCP_PrecRS_Sfc"
files = sorted(glob(f"{path}/gpcp_v01r03_daily_d*.nc"))

valid_files = []
bad_files = []

for f in files:
    try:
        ds = xr.open_dataset(f)   # try opening
        ds.close()
        valid_files.append(f)
    except Exception as e:
        print(f"⚠️ Bad file: {f} -> {e}")
        bad_files.append(f)

print(f"\n✅ Valid files: {len(valid_files)} / {len(files)}")
print(f"❌ Bad files: {len(bad_files)}")

"""


#print(prec.time)
#prec
#agcl
#print(prec.variables.values)
#print(prec.variables.values)

