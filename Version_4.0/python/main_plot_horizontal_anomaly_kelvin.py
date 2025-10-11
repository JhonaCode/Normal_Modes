import normal_modes.anomh as th

wave='kv'
cs=0

args={
    "wv"   : wave,
    "cs"   : cs,
    "caso": "ERA_5",
    "epoca": 37,
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [-0.2,0.3,21],
    "units":'[kJ/kg]'
}

#To load the appropiated file given the args. 
arg=th.arguments(args)


args={
    "wv"   : wave,
    "cs"   : cs,
    "caso": "BAMHY",
    "epoca": 10,
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [0.3,2.3,21],
    "units":'[kJ/kg]'
}
arg=th.arguments(args)

#To load the appropiated file given the args. 
#arg=th.arguments(args)
args={
    "wv"   : wave,
    "cs"   : cs,
    "caso": "MONAN",
    "epoca": 7,
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [0.2,1.5,21],
    "units":'[kJ/kg]'
}
arg=th.arguments(args)

cs=1

args={
    "wv"   : wave,
    "cs"   : cs,
    "caso": "ERA_5",
    "epoca": 37,
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [-2.5,0.3,21],
    "units":'[kJ/kg]'
}

#To load the appropiated file given the args. 
arg=th.arguments(args)


args={
    "wv"   : wave,
    "cs"   : cs,
    "caso": "BAMHY",
    "epoca": 10,
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor":[0.,4.0,21],
    "units":'[kJ/kg]'
}
arg=th.arguments(args)

#To load the appropiated file given the args. 
#arg=th.arguments(args)
args={
    "wv"   : wave,
    "cs"   : cs,
    "caso": "MONAN",
    "epoca": 7,
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [-5.5,0.5,21],
    "units":'[kJ/kg]'
}
arg=th.arguments(args)
