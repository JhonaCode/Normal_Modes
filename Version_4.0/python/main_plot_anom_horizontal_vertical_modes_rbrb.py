import normal_modes.anomhvint as th

args={
    "var" : "rbrb01",
    "caso": "ERA_5",
    "epoca": 37,
    "atm": 'ht',
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [-1.0,4.0,13],
    "fmt": '.2f',
    "units": '[kJ;kg]',
}

#To load the appropiated file given the args. 
arg=th.anomhvint(args)

args={
    "var" : "rbrb01",
    "caso": "BAMHY",
    "epoca": 10,
    "atm": 'ht',
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [-1.0,4.0,13],
    "fmt": '.2f',
    "units": '[kJ;kg]',
}

#To load the appropiated file given the args. 
arg=th.anomhvint(args)

args={
    "var" : "rbrb01",
    "caso": "MONAN",
    "epoca": 7,
    "atm": 'ht',
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [-1.0,4.0,13],
    "fmt": '.2f',
    "units": '[kJ;kg]',
}

#To load the appropiated file given the args. 
arg=th.anomhvint(args)
