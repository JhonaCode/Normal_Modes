import  os,sys
import importlib

# path to your target folder
folder_path = os.path.join('/home/jhonatan.aguirre/Modal_Energetics/Version_4.0/', "python")
sys.path.append(folder_path)

import normal_modes.anomhint as tv

args={
    "wa": 'rb',
    "wb": 'kv',
    "cs": 0,
    "caso": "ERA_5",
    "epoca": 37,
    "csst": "RainSS",
    "area": "local",
    "xsec": "no",
    "color": 'jet',    
    "show" : True,
    "bcolor": [-1.0,1.1,11],
    "fmt":'.1f', 
    "units":'[kJ/kg]' 
}

#To load the appropiated file given the args. 
arg=tv.arguments(args)

args={
    "wa": 'rb',
    "wb": 'kv',
    "cs": 0,
    "caso": "BAMHY",
    "epoca": 10,
    "csst": "RainSS",
    "area": "local",
    "xsec": "no",
    "color": 'jet',    
    "show" : True,
    "bcolor": [-1.0,1.0,11],
    "fmt":'.1f', 
    "units":'[kJ/kg]' 
}

#To load the appropiated file given the args. 
arg=tv.arguments(args)

args={
    "wa": 'rb',
    "wb": 'kv',
    "cs": 1,
    "caso": "ERA_5",
    "epoca": 37,
    "csst": "RainSS",
    "area": "local",
    "xsec": "no",
    "color": 'jet',    
    "show" : True,
    "bcolor": [-2.5,2.0,15],
    "fmt":'.1f', 
    "units":'[kJ/kg]' 
}

#To load the appropiated file given the args. 
arg=tv.arguments(args)

args={
    "wa": 'rb',
    "wb": 'kv',
    "cs": 1,
    "caso": "BAMHY",
    "epoca": 10,
    "csst": "RainSS",
    "area": "local",
    "xsec": "no",
    "color": 'jet',    
    "show" : True,
    "bcolor": [-2.5,2.0,15],
    "fmt":'.1f', 
    "units":'[kJ/kg]' 
}

#To load the appropiated file given the args. 
arg=tv.arguments(args)


