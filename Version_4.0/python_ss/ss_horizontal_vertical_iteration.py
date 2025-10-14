import  os,sys
import importlib

# path to your target folder
folder_path = os.path.join('/home/jhonatan.aguirre/Modal_Energetics/Version_4.0/', "python")
sys.path.append(folder_path)


import normal_modes.totalhvint as th

args={
    "var" : "rbkv01",
    "caso": "ERA_5",
    "epoca": 2,
    "csst": "ClimSS",
    "area": "local",
    "perc": "Ener",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [-4.5,1.5,13],
    "fmt": '.2f',
}

#To load the appropiated file given the args. 
arg=th.totalhvint(args)

args={
    "var" : "kvrb01",
    "caso": "ERA_5",
    "epoca": 2,
    "csst": "ClimSS",
    "area": "local",
    #"perc": "Perc",
    "perc": "Ener",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [-2,2.5,10],
    "fmt": '.2f',
}

#To load the appropiated file given the args. 
arg=th.totalhvint(args)

args={
    "var" : "rbrb01",
    "caso": "ERA_5",
    "epoca": 2,
    "csst": "ClimSS",
    "area": "local",
    #"perc": "Perc",
    "perc": "Ener",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [0.5,7.0,14],
    "fmt": '.2f',
}
arg=th.totalhvint(args)
