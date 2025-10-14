import  os,sys
import importlib

# path to your target folder
folder_path = os.path.join('/home/jhonatan.aguirre/Modal_Energetics/Version_4.0/', "python")
sys.path.append(folder_path)


import normal_modes.anomhvint as th

args={
    "var" : "rbkv01",
    "caso": "ERA_5",
    "epoca": 37,
    "atm": 'ht',
    "csst": "RainSS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [-2.5,3,16],
    "fmt": '.2f',
    "units": '[kJ/kg]',
}

#To load the appropiated file given the args. 
#arg=th.anomhvint(args)


args={
    "var" : "rbkv01",
    "caso": "BAMHY",
    "epoca": 10,
    "atm": 'ht',
    "csst": "RainSS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [-2.5,3,16],
    "fmt": '.2f',
    "units": '[kJ/kg]',
}

#To load the appropiated file given the args. 
arg=th.anomhvint(args)

var='kvrb01'
bcolor= [-1.0,1,16]

args={
    "var" : var,
    "caso": "ERA_5",
    "epoca": 37,
    "atm": 'ht',
    "csst": "RainSS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": bcolor,
    "fmt": '.2f',
    "units": '[kJ/kg]',
}

#To load the appropiated file given the args. 
arg=th.anomhvint(args)


args={
    "var" : var,
    "caso": "BAMHY",
    "epoca": 10,
    "atm": 'ht',
    "csst": "RainSS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": bcolor,
    "fmt": '.2f',
    "units": '[kJ/kg]',
}

#To load the appropiated file given the args. 
arg=th.anomhvint(args)

var='rbrb01'
bcolor= [-3.0,5,16]

args={
    "var" : var,
    "caso": "ERA_5",
    "epoca": 37,
    "atm": 'ht',
    "csst": "RainSS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": bcolor,
    "fmt": '.2f',
    "units": '[kJ/kg]',
}

#To load the appropiated file given the args. 
arg=th.anomhvint(args)


args={
    "var" : var,
    "caso": "BAMHY",
    "epoca": 10,
    "atm": 'ht',
    "csst": "RainSS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": bcolor,
    "fmt": '.2f',
    "units": '[kJ/kg]',
}

#To load the appropiated file given the args. 
arg=th.anomhvint(args)
