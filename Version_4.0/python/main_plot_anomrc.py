import normal_modes.anomrc as tv

args={
    "caso": "ERA_5",
    "epoca": 37,
    #"csst": "ClimRS",
    "csst": "RainRS",
    "lev":500,
    "bcolor": [-140.0,140,11],
    "lats":[-90,90,6], 
    "lons":[0,360,6], 
    "color": 'jet',    
    "scale":300, 
    "width":0.0020, 
    "magwind":20.0,
    "show" : True,
    "fmt":'.0f', 
    "units":'m/s', 
}

#To load the appropiated file given the args. 
#arg=tv.anomrc(args)

args={
    "caso": "BAMHY",
    "epoca": 10,
    #"csst": "ClimRS",
    "csst": "RainRS",
    "lev":500,
    "bcolor": [-140.0,140,11],
    "lats":[-90,90,6], 
    "lons":[0,360,6], 
    "color": 'jet',    
    "scale":300, 
    "width":0.0020, 
    "magwind":20.0,
    "show" : True,
    "fmt":'.0f', 
    "units":'m/s', 
}

#To load the appropiated file given the args. 
#arg=tv.anomrc(args)

args={
    "caso": "MONAN",
    "epoca": 7,
    #"csst": "ClimRS",
    "csst": "RainRS",
    "lev":500,
    "bcolor": [-140.0,140,11],
    "lats":[-90,90,6], 
    "lons":[0,360,6], 
    "color": 'jet',    
    "scale":300, 
    "width":0.0020, 
    "magwind":20.0,
    "show" : True,
    "fmt":'.0f', 
    "units":'m/s', 
}

#To load the appropiated file given the args. 
arg=tv.anomrc(args)
