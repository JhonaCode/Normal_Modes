import normal_modes.totalv as tv

args={
    "cs": 0,
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
    "bcolor": [3.0,13,17],
}

#To load the appropiated file given the args. 
arg=tv.arguments(args)


args0={
    "cs": 1,
    "caso": "ERA_5",
    "epoca": 2,
    "csst": "ClimSS",
    "area": "local",
    "perc": "Ener",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [3,33,17],
}

arg1=tv.arguments(args0)



