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
    "bcolor": [-1.8,1.2,13],
    "fmt": '.2f',
    "units": '[kJ;kg]',
}

#To load the appropiated file given the args. 
arg=th.anomhvint(args)

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
    "bcolor": [-1.0,1.2,13],
    "fmt": '.2f',
    "units": '[kJ;kg]',
}

