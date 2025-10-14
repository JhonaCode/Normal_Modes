import  os,sys
import importlib

# path to your target folder
folder_path = os.path.join('/home/jhonatan.aguirre/Modal_Energetics/Version_4.0/', "python")
sys.path.append(folder_path)

import normal_modes.anomrc as tv

args={
    "caso": "ERA_5",
    "epoca": 37,
    #"csst": "ClimRS",
    "csst": "RainSS",
    "lev":500,
    "bcolor": [-140.0,160,15],
    "lats":[-90,90,6], 
    "lons":[0,360,6], 
    "color": 'jet',    
    "scale":300, 
    "width":0.0020, 
    "magwind":20.0,
    "show" : True,
    "fmt":'.0f', 
    "units":'m/s', 
}

#To load the appropiated file given the args. 
arg=tv.anomrc(args)

args={
    "caso": "BAMHY",
    "epoca": 10,
    #"csst": "ClimRS",
    "csst": "RainSS",
    "lev":500,
    "bcolor": [-140.0,160,15],
    "lats":[-90,90,6], 
    "lons":[0,360,6], 
    "color": 'jet',    
    "scale":300, 
    "width":0.0020, 
    "magwind":20.0,
    "show" : True,
    "fmt":'.0f', 
    "units":'m/s', 
}

#To load the appropiated file given the args. 
arg=tv.anomrc(args)

#########################
args={
    "caso": "ERA_5",
    "epoca": 21,
    #"csst": "ClimRS",
    "csst": "RainSS",
    "lev":500,
    "bcolor": [-160.0,160,15],
    "lats":[-90,90,6], 
    "lons":[0,360,6], 
    "color": 'jet',    
    "scale":300, 
    "width":0.0020, 
    "magwind":20.0,
    "show" : True,
    "fmt":'.0f', 
    "units":'m/s', 
}

#To load the appropiated file given the args. 
arg=tv.anomrc(args)

args={
    "caso": "BAMHY",
    "epoca": 6,
    #"csst": "ClimRS",
    "csst": "RainSS",
    "lev":500,
    "bcolor": [-160.0,160,11],
    "lats":[-90,90,6], 
    "lons":[0,360,6], 
    "color": 'jet',    
    "scale":300, 
    "width":0.0020, 
    "magwind":20.0,
    "show" : True,
    "fmt":'.0f', 
    "units":'m/s', 
}

#To load the appropiated file given the args. 
arg=tv.anomrc(args)

#########################
args={
    "caso": "ERA_5",
    "epoca": 53,
    #"csst": "ClimRS",
    "csst": "RainSS",
    "lev":500,
    "bcolor": [-80.0,80,11],
    "lats":[-90,90,6], 
    "lons":[0,360,6], 
    "color": 'jet',    
    "scale":300, 
    "width":0.0020, 
    "magwind":20.0,
    "show" : True,
    "fmt":'.0f', 
    "units":'m/s', 
}

#To load the appropiated file given the args. 
arg=tv.anomrc(args)

args={
    "caso": "BAMHY",
    "epoca": 14,
    #"csst": "ClimRS",
    "csst": "RainSS",
    "lev":500,
    "bcolor": [-80.0,80,11],
    "lats":[-90,90,6], 
    "lons":[0,360,6], 
    "color": 'jet',    
    "scale":300, 
    "width":0.0020, 
    "magwind":20.0,
    "show" : True,
    "fmt":'.0f', 
    "units":'m/s', 
}

#To load the appropiated file given the args. 
arg=tv.anomrc(args)

