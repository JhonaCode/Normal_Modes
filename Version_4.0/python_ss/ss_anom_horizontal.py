import  os,sys
import importlib

# path to your target folder
folder_path = os.path.join('/home/jhonatan.aguirre/Modal_Energetics/Version_4.0/', "python")
sys.path.append(folder_path)

import normal_modes.anomh as th

wave='rb'
cs=0
bcolor=[-4.0,14,18]

args={
    "wv"   : wave,
    "cs"   : cs,
    "caso": "ERA_5",
    "epoca": 37,
    "csst": "RainSS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor":  bcolor,#[-0.2,0.3,21],
    "units":'[kJ/kg]'
}

#To load the appropiated file given the args. 
arg=th.arguments(args)


args={
    "wv"   : wave,
    "cs"   : cs,
    "caso": "BAMHY",
    "epoca": 10,
    "csst": "RainSS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": bcolor,
    "units":'[kJ/kg]'
}
arg=th.arguments(args)

wave='rb'
cs=1
bcolor=[-8.0,14,18]

args={
    "wv"   : wave,
    "cs"   : cs,
    "caso": "ERA_5",
    "epoca": 37,
    "csst": "RainSS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor":  bcolor,#[-0.2,0.3,21],
    "units":'[kJ/kg]'
}

#To load the appropiated file given the args. 
arg=th.arguments(args)


args={
    "wv"   : wave,
    "cs"   : cs,
    "caso": "BAMHY",
    "epoca": 10,
    "csst": "RainSS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": bcolor,
    "units":'[kJ/kg]'
}
arg=th.arguments(args)
