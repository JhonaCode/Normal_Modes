#import normal_modes.totalvint as tv

import  os,sys
import importlib

# path to your target folder
folder_path = os.path.join('/home/jhonatan.aguirre/Modal_Energetics/Version_4.0/', "python")
sys.path.append(folder_path)

import normal_modes.totalvint as tv


args={
    "ca": 0,
    "cb": 1,
    "caso": "ERA_5",
    "epoca": 2,
    "csst": "ClimSS",
    "area": "local",
    "perc": "Ener",
    #"perc": "Perc",
    "xsec": "no",
    "cnt": 0,
    #"color": 'RdBu_r',    
    "color": 'jet',    
    "show" : True,
    "bcolor": [0.5,7.0,16],
}

#To load the appropiated file given the args. 
arg=tv.arguments(args)

