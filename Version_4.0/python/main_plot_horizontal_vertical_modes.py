import normal_modes.totalhvint as th

args={
    "var" : "rbkv01",
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
    "bcolor": [-6,0.5,18],
    #"bcolor": [-6,0.5,0.25],
    "fmt": '.2f',
}

#To load the appropiated file given the args. 
arg=th.totalhvint(args)

args={
    "var" : "kvrb01",
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
    "bcolor": [-2,3,18],
    "fmt": '.2f',
}

#To load the appropiated file given the args. 
arg=th.totalhvint(args)

args={
    "var" : "rbrb01",
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
    "bcolor": [0.5,6.5,15],
    "fmt": '.2f',
}
arg=th.totalhvint(args)
