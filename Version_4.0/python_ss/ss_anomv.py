import  os,sys
import importlib

# path to your target folder
folder_path = os.path.join('/home/jhonatan.aguirre/Modal_Energetics/Version_4.0/', "python")
sys.path.append(folder_path)

import normal_modes.anomv as th 
args={
    "cs"    : 0,
    "caso"  : "ERA_5",
    "epoca" : 37,
    "csst"  : "RainSS",
    "cnt"   : 0,
    "color" : 'jet',    
    "show"  : True,
    "bcolor": [-4,16,17],
    "units" : '[kJ/kg]',
    "lats"  :[-90,0,6],
    "lons"  :[0,360,6],
}

#To load the appropiated file given the args. 
arg=th.arguments(args)


args={
    "cs"    : 0,
    "caso"  : "BAMHY",
    "epoca" : 10,
    "csst"  : "RainSS",
    "cnt"   : 0,
    "color" : 'jet',    
    "show"  : True,
    "bcolor": [-4,16,17],
    "units" : '[kJ/kg]',
    "lats"  :[-90,0,6],
    "lons"  :[0,360,6],
}
arg=th.arguments(args)


args={
    "cs"    : 1,
    "caso"  : "ERA_5",
    "epoca" : 37,
    "csst"  : "RainSS",
    "cnt"   : 0,
    "color" : 'jet',    
    "show"  : True,
    "bcolor": [-4,16,17],
    "units" : '[kJ/kg]',
    "lats"  :[-90,0,6],
    "lons"  :[0,360,6],
}

#To load the appropiated file given the args. 
arg=th.arguments(args)

args={
    "cs"    : 1,
    "caso"  : "BAMHY",
    "epoca" : 10,
    "csst"  : "RainSS",
    "cnt"   : 0,
    "color" : 'jet',    
    "show"  : True,
    "bcolor": [-4,16,17],
    "units" : '[kJ/kg]',
    "lats"  :[-90,0,6],
    "lons"  :[0,360,6],
}
arg=th.arguments(args)

