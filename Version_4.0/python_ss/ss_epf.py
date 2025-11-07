import  os,sys
import importlib

# path to your target folder
folder_path = os.path.join('/home/jhonatan.aguirre/Modal_Energetics/Version_4.0/', "python")
sys.path.append(folder_path)

import normal_modes.epflux as tv

args={
    "caso": "ERA_5",
    "epoca": 2,
    "csst": "ClimSS",
    "bcolor": [-8.0,10,10],
    "lats":  [-85,-25,5],
    "color": 'jet',    
    "scale":5, 
    "width":0.0050, 
    "magwind":10.0,
    "show" : True,
    "fmt":'.0f', 
    "units":'m/s', 
}

arg=tv.epf(args)

#exit()

lats=  [-70,-10,5]
#To load the appropiated file given the args. 

args={
    "caso": "ERA_5",
    "epoca": 37,
    #"csst": "ClimRS",
    "csst": "RainSS",
    "bcolor": [-8.0,10,10],
    "lats":  lats, 
    "color": 'jet',    
    "scale":5, 
    "width":0.0050, 
    "magwind":10.0,
    "show" : True,
    "fmt":'.0f', 
    "units":'m/s', 
}

#To load the appropiated file given the args. 
arg=tv.epf(args)

args={
    "caso": "ERA_5",
    "epoca": 53,
    #"csst": "ClimRS",
    "csst": "RainSS",
    "lats":  lats, 
    "bcolor": [-8.0,10,10],
    "color": 'jet',    
    "scale":5, 
    "width":0.0050, 
    "magwind":10.0,
    "show" : True,
    "fmt":'.0f', 
    "units":'m/s', 
}

#To load the appropiated file given the args. 
arg=tv.epf(args)


args={
    "caso": "BAMHY",
    "epoca": 10,
    #"csst": "ClimRS",
    "csst": "RainSS",
    "bcolor": [-8.0,10,10],
    "lats":  lats, 
    "color": 'jet',    
    "scale":5, 
    "width":0.0050, 
    "magwind":10.0,
    "show" : True,
    "fmt":'.0f', 
    "units":'m/s', 
}

#To load the appropiated file given the args. 
arg=tv.epf(args)

args={
    "caso": "BAMHY",
    "epoca": 14,
    #"csst": "ClimRS",
    "csst": "RainSS",
    "lats":  lats, 
    "bcolor": [-8.0,10,10],
    "color": 'jet',    
    "scale":5, 
    "width":0.0050, 
    "magwind":10.0,
    "show" : True,
    "fmt":'.0f', 
    "units":'m/s', 
}

#To load the appropiated file given the args. 
arg=tv.epf(args)
