import normal_modes.temporal_plot as tp

args={
    "caso": "ERA_5",
    "show" : False,
    "ylim": [0,350],
}

#To load the appropiated file given the args. 
fig=tp.temporal(args)

args={
    "caso": "BAMHY",
    "show" : False,
    "ylim": [0,350],
}

#To load the appropiated file given the args. 
fig=tp.temporal(args)

args={
    "caso": "MONAN",
    "show" : False,
    "ylim": [0,350],
}

#To load the appropiated file given the args. 
fig=tp.temporal(args)
