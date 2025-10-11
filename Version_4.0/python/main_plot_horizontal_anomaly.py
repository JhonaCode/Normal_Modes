import normal_modes.anomh as th

wave='rb'
cs=1
bcolor=[-4.0,6,11]

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
    "bcolor":  bcolor,#[-0.2,0.3,21],
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
    "bcolor": bcolor,
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
    "bcolor": bcolor,
    "units":'[kJ/kg]'
}
arg=th.arguments(args)
