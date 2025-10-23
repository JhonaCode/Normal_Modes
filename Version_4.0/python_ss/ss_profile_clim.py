import  os,sys
import importlib

# path to your target folder
folder_path = os.path.join('/home/jhonatan.aguirre/Modal_Energetics/Version_4.0/', "python")
sys.path.append(folder_path)

import normal_modes.profile as th 

epoca = [2]
args={
    "caso"  : ["ERA_5"],
    "epoca" : epoca,
    "csst"  : "ClimSS",
    "var"   : "Qr",  
    "vmulti": [1],  
    "title" :  "Barotropic",
    "ytitle" : "Pressure [hPa]",
    "latp"  : -23.75,
    "color" : ["blue"],    
    #"date"  : "2023-02-01T15:00",
    "show"  : True,
    "save"  :True,
}

#To load the appropiated file given the args. 
arg=th.arguments(args)


args={
    "caso"  : ["ERA_5"],
    "epoca" : epoca,
    "csst"  : "ClimSS",
    "var"   : "Qc",  
    "vmulti": [1,1],  
    "title" :  "Baroclinic",
    "latp"  : -23.75,
    "color" : ['blue'],    
    #"date"  : "2023-02-01T15:00",
    "show"  : True,
    "save"  :True,
}

#To load the appropiated file given the args. 
arg=th.arguments(args)


args={
    "caso"  : ["ERA_5"],
    "epoca" : epoca,
    "csst"  : "ClimSS",
    "var"   : "Qy",  
    "vmulti": [1,1],  
    "title" :  "Baroclinic+Barotropic",
    "latp"  : -23.75,
    "color" : ['blue'],    
    #"date"  : "2023-02-01T15:00",
    "show"  : True,
    "save"  :True,
}

#To load the appropiated file given the args. 
arg=th.arguments(args)
