import normal_modes.totalh as th

args={
    "wv"   : "rb",
    "cs"   : 0,
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
    "bcolor": [2,8,6],
}

#To load the appropiated file given the args. 
#arg=th.arguments(args)


args0={
    "wv": "rb",
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
    "bcolor": [2,22,11],
}

#arg1=th.arguments(args0)

args0={
    "wv": "kv",
    "cs": 0,
    "caso": "ERA_5",
    "epoca": 2,
    "csst": "ClimRS",
    "area": "local",
    "perc": "Ener",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [0.5,5,9],
}

#arg1=th.arguments(args0)

args0={
    "wv": "kv",
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
    "bcolor": [4,32,11],
}

#arg1=th.arguments(args0)

args0={
    "wv": "mx",
    "cs": 0,
    "caso": "ERA_5",
    "epoca": 2,
    "csst": "ClimRS",
    "area": "local",
    "perc": "Ener",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [2E-3,4.5E-2,11],
    'fmt':".1E"
}

arg1=th.arguments(args0)

args0={
    "wv": "mx",
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
    "bcolor": [5E-5,7E-2,11],
    'fmt':".1E"
}

arg1=th.arguments(args0)


