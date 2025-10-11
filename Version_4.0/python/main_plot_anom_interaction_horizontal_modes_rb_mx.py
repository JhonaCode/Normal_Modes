import normal_modes.anomhint as tv

args={
    "wa": 'rb',
    "wb": 'mx',
    "cs": 0,
    "caso": "ERA_5",
    "epoca": 37,
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "color": 'jet',    
    "show" : True,
    "bcolor": [-0.25,0.2,13],
    "fmt":'.1f', 
    "units":'[kJ/kg]' 
}

#To load the appropiated file given the args. 
#arg=tv.arguments(args)

args={
    "wa": 'rb',
    "wb": 'mx',
    "cs": 0,
    "caso": "BAMHY",
    "epoca": 10,
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "color": 'jet',    
    "show" : True,
    "bcolor": [-0.25,0.1,21],
    "fmt":'.1f', 
    "units":'[kJ/kg]' 
}

#To load the appropiated file given the args. 
#arg=tv.arguments(args)

args={
    "wa": 'rb',
    "wb": 'mx',
    "cs": 0,
    "caso": "MONAN",
    "epoca": 7,
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "color": 'jet',    
    "show" : True,
    "bcolor": [-0.3,0.15,21],
    "fmt":'.1f', 
    "units":'[kJ/kg]' 
}

#To load the appropiated file given the args. 
#arg=tv.arguments(args)

args={
    "wa": 'rb',
    "wb": 'mx',
    "cs": 1,
    "caso": "ERA_5",
    "epoca": 37,
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "color": 'jet',    
    "show" : True,
    "bcolor": [-0.08,0.06,13],
    "fmt":'.1E', 
    "units":'[kJ/kg]' 
}

#To load the appropiated file given the args. 
arg=tv.arguments(args)

args={
    "wa": 'rb',
    "wb": 'mx',
    "cs": 1,
    "caso": "BAMHY",
    "epoca": 10,
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "color": 'jet',    
    "show" : True,
    "bcolor": [-0.1,0.08,13],
    "fmt":'.1E', 
    "units":'[kJ/kg]' 
}

#To load the appropiated file given the args. 
arg=tv.arguments(args)

args={
    "wa": 'rb',
    "wb": 'mx',
    "cs": 1,
    "caso": "MONAN",
    "epoca": 7,
    "csst": "RainRS",
    "area": "local",
    "xsec": "no",
    "color": 'jet',    
    "show" : True,
    "bcolor": [-0.06,0.1,13],
    "fmt":'.1E', 
    "units":'[kJ/kg]' 
}

#To load the appropiated file given the args. 
arg=tv.arguments(args)

