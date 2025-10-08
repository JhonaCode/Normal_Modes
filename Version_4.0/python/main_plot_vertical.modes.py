import normal_modes.totalv as tv

args={
    "cs": 0,
    "caso": "ERA_5",
    "epoca": 2,
    "csst": "ClimRS",
    "area": "local",
    #"perc": "Perc",
    "perc": "Ener",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [4.5,10,11],
}

#To load the appropiated file given the args. 
arg=tv.arguments(args)


args0={
    "cs": 1,
    "caso": "ERA_5",
    "epoca": 2,
    "csst": "ClimRS",
    "area": "local",
    "perc": "Ener",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [3,33,11],
}

arg1=tv.arguments(args0)



