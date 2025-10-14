import  os,sys
import importlib

# path to your target folder
folder_path = os.path.join('/home/jhonatan.aguirre/Modal_Energetics/Version_4.0/', "python")
sys.path.append(folder_path)

import normal_modes.totalh as th

args={
    "wv"   : "rb",
    "cs"   : 0,
    "caso": "ERA_5",
    "epoca": 2,
    "csst": "ClimSS",
    "area": "local",
    "perc": "Ener",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [2,13,16],
}

#To load the appropiated file given the args. 
#arg=th.arguments(args)



args0={
    "wv": "rb",
    "cs": 1,
    "caso": "ERA_5",
    "epoca": 2,
    "csst": "ClimSS",
    "area": "local",
    "perc": "Ener",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [2,22,11],
}

#arg1=th.arguments(args0)

args0={
    "wv": "kv",
    "cs": 0,
    "caso": "ERA_5",
    "epoca": 2,
    "csst": "ClimSS",
    "area": "local",
    "perc": "Ener",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [0.5,6.5,15],
    'lats':[-45,45,6],
    'lons':[0,360,6],
}

arg1=th.arguments(args0)

args0={
    "wv": "kv",
    "cs": 1,
    "caso": "ERA_5",
    "epoca": 2,
    "csst": "ClimSS",
    "area": "local",
    "perc": "Ener",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [0,32,11],
    'lats':[-45,45,6],
    'lons':[0,360,6],
}

arg1=th.arguments(args0)
