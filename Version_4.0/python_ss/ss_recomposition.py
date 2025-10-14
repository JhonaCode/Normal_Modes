import  os,sys
import importlib

# path to your target folder
folder_path = os.path.join('/home/jhonatan.aguirre/Modal_Energetics/Version_4.0/', "python")
sys.path.append(folder_path)

import normal_modes.totalrc as tv

args={
    "caso": "ERA_5",
    "epoca": 2,
    #"csst": "ClimRS",
    "csst": "ClimSS",
    "lev":500,
    "bcolor": [-60.0,60,11],
    "lats":[-90,90,6], 
    "lons":[0,360,6], 
    "color": 'jet',    
    "scale":100, 
    "width":0.0020, 
    "magwind":8.0,
    "show" : True,
    "fmt":'.0f', 
    "units":'m/s', 
}

#To load the appropiated file given the args. 
arg=tv.totalrc(args)

