import  os,sys
import importlib
# path to your target folder
folder_path = os.path.join('/home/jhonatan.aguirre/Modal_Energetics/Version_4.0/', "python")
sys.path.append(folder_path)

import normal_modes.totalv as tv

args={
    "cs": 0,
    "caso": "ERA_5",
    "epoca": 2,
    "csst": "ClimSS",
    "area": "local",
    #"perc": "Perc",
    "perc": "Ener",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [3.0,13,11],
}

#To load the appropiated file given the args. 
arg=tv.arguments(args)


args0={
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
    "bcolor": [3,33,11],
}

arg1=tv.arguments(args0)
