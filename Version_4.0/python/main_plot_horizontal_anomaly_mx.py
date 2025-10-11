import normal_modes.anomh as th

#wave='rb'
#wave='kv'
#bcolor=[-1,1,21]
wave='mx'

args={
    "wv"   : wave,
    "cs"   : 0,
    "caso": "ERA_5",
    "epoca": 37,
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor":  [-0.0,0.18,11],
    "units":'[kJ/kg]',
    "fmt":'.1E'
}

#To load the appropiated file given the args. 
#arg=th.arguments(args)


args={
    "wv"   : wave,
    "cs"   : 0,
    "caso": "BAMHY",
    "epoca": 10,
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [-0.02,0.12,11],
    "units":'[kJ/kg]',
    "fmt":'.1E'
}
#arg=th.arguments(args)

#To load the appropiated file given the args. 
#arg=th.arguments(args)
args={
    "wv"   : wave,
    "cs"   : 0,
    "caso": "MONAN",
    "epoca": 7,
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "cnt": 0,
    "color": 'jet',    
    "show" : True,
    "bcolor": [-0.02,0.16,11],
    "units":'[kJ/kg]',
    "fmt":'.1E'
}
#arg=th.arguments(args)

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
    "bcolor":  [-0.015,0.035,11],
    "units":'[kJ/kg]',
    "fmt":'.1E'
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
    "bcolor": [-0.02,0.06,11],
    "units":'[kJ/kg]',
    "fmt":'.1E'
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
    "bcolor": [-0.02,0.05,11],
    "units":'[kJ/kg]',
    "fmt":'.1E'
}
arg=th.arguments(args)
