import normal_modes.totalvint as tv

args={
    "ca": 0,
    "cb": 1,
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
    "bcolor": [1.0,7.5,13],
}

#To load the appropiated file given the args. 
arg=tv.arguments(args)

