import  os,sys
import importlib

# path to your target folder
folder_path = os.path.join('/home/jhonatan.aguirre/Modal_Energetics/Version_4.0/', "python")
sys.path.append(folder_path)


import normal_modes.totalhint as tv

args={
    "wa": 'rb',
    "wb": 'kv',
    "cs": 0,
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
    "bcolor": [-2.3,1.3,12],
    "fmt":'.1f', 
    "lats":[-60,30,6],
    "lons":[0,360,6],
}

#To load the appropiated file given the args. 
#arg=tv.arguments(args)


args={
    "wa": 'rb',
    "wb": 'kv',
    "cs": 1,
    "caso": "ERA_5",
    "epoca": 2,
    "csst": "ClimRS",
    "area": "local",
    "perc": "Ener",
    #"perc": "Perc",
    "xsec": "no",
    "cnt": 0,
    #"color": 'RdBu_r',    
    "color": 'jet',    
    "show" : True,
    "bcolor": [-10.0,4,9],
    "fmt":'.1f', 
    "lats":[-60,30,6],
    "lons":[0,360,6],
}

#To load the appropiated file given the args. 
arg=tv.arguments(args)
