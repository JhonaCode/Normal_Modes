import  os,sys
import importlib

# path to your target folder
folder_path = os.path.join('/home/jhonatan.aguirre/Modal_Energetics/Version_4.0/', "python")
sys.path.append(folder_path)

import normal_modes.epflux as tv

args={
    "caso": "ERA_5",
    "epoca": 37,
    #"csst": "ClimRS",
    "csst": "RainSS",
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

exit()

args={
    "caso": "BAMHY",
    "epoca": 10,
    #"csst": "ClimRS",
    "csst": "RainSS",
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
#arg=tv.anomrc(args)

