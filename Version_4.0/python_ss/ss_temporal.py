import  os,sys
import importlib

# path to your target folder
folder_path = os.path.join('/home/jhonatan.aguirre/Modal_Energetics/Version_4.0/', "python")
sys.path.append(folder_path)

import normal_modes.temporal_plot_ss as tp

args={
    "caso": "ERA_5",
    "csst":'RainSS',
    "show" : True,
    "ylim": [0,350],
}

#To load the appropiated file given the args. 
fig=tp.temporal(args)

args={
    "caso": "BAMHY",
    "csst":'RainSS',
    "show" : True,
    "ylim": [0,350],
}

#To load the appropiated file given the args. 
fig=tp.temporal(args)
