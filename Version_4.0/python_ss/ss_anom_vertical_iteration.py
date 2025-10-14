import  os,sys
import importlib
# path to your target folder
folder_path = os.path.join('/home/jhonatan.aguirre/Modal_Energetics/Version_4.0/', "python")
sys.path.append(folder_path)


import normal_modes.anomvint as tv

args={
    "ca": 0,
    "cb": 1,
    "atm": 'ht',
    "caso": "ERA_5",
    "epoca": 37,
    "csst": "RainSS",
    "area": "local",
    "perc": "Ener",
    #"perc": "Perc",
    "xsec": "no",
    "cnt": 0,
    #"color": 'RdBu_r',    
    "color": 'jet',    
    "show" : True,
    "bcolor": [-2.5,4.0,13],
    "units": '[kJ/kg]',
}

#To load the appropiated file given the args. 
arg=tv.arguments(args)

args={
    "ca": 0,
    "cb": 1,
    "atm": 'ht',
    "caso": "BAMHY",
    "epoca": 10,
    "csst": "RainSS",
    "area": "local",
    "perc": "Ener",
    #"perc": "Perc",
    "xsec": "no",
    "cnt": 0,
    #"color": 'RdBu_r',    
    "color": 'jet',    
    "show" : True,
    "bcolor": [-2.5,4.0,13],
    "units": '[kJ/kg]',
}

#To load the appropiated file given the args. 
arg=tv.arguments(args)
