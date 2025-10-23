import  os,sys
import importlib

# path to your target folder
folder_path = os.path.join('/home/jhonatan.aguirre/Modal_Energetics/Version_4.0/', "python")
sys.path.append(folder_path)


import normal_modes.temp_energy_cicle as te


args={
    "caso": ["ERA_5","BAMHY"],
    "csst": "RainSS",
    "var" : 'Azm',
    "title" :' A) Zonal A. Potential Energy',
    "xtitle": 'Time [Days]',
    "ytitle": r'AZ [Jm$\mathbf{^{-2}}$]$\mathbf{\times10^5}$',
    "figname": 'zonal_A_potential_energy',
    "save": True
}

te.temporal_plot(args)


args={
    "caso": ["ERA_5","BAMHY"],
    "csst": "RainSS",
    "var" : 'Aem',
    "title" :' B) Eddie A. Potential Energy',
    "xtitle": 'Time [Days]',
    "ytitle": r'AE [Jm$\mathbf{^{-2}}$]$\mathbf{\times10^5}$',
    "figname": 'eddy_A_potential_energy',
    "save": True
}

te.temporal_plot(args)

args={
    "caso": ["ERA_5","BAMHY"],
    "csst": "RainSS",
    "var" : 'Kzm',
    "title" :' C) Zonal Kinetic Energy',
    "xtitle": 'Time [Days]',
    "ytitle": r'KZ [Jm$\mathbf{^{-2}}$]$\mathbf{\times10^5}$',
    "figname": 'zonal_kinetic_energy',
    "save": True
}

te.temporal_plot(args)

args={
    "caso": ["ERA_5","BAMHY"],
    "csst": "RainSS",
    "var" : 'Kem',
    "title" :'D) Eddie Kinetic Energy',
    "xtitle": 'Time [Days]',
    "ytitle": r'KE [Jm$\mathbf{^{-2}}$]$\mathbf{\times10^5}$',
    "figname": 'eddy_kinetic_energy',
    "save": True
}

te.temporal_plot(args)

args={
    "caso": ["ERA_5","BAMHY"],
    "csst": "RainSS",
    "var" : 'Cam',
    "title" :' E)  Convertion AZ into AE',
    "xtitle": 'Time [Days]',
    "ytitle": r'CA [Jm$\mathbf{^{-2}}$]$\mathbf{\times10^5}$',
    "figname": 'convection_az_ae',
    "save": True
}

te.temporal_plot(args)

args={
    "caso": ["ERA_5","BAMHY"],
    "csst": "RainSS",
    "var" : 'Cem',
    "title" :' F) Convertion AE into KE',
    "xtitle": 'Time [Days]',
    "ytitle": r'CE [Jm$\mathbf{^{-2}}$]$\mathbf{\times10^5}$',
    "figname": 'convection_ae_ke',
    "save": True
}

te.temporal_plot(args)


args={
    "caso": ["ERA_5","BAMHY"],
    "csst": "RainSS",
    "var" : 'Gem',
    "title" :' G) Generation of AE', 
    "xtitle": 'Time [Days]',
    "ytitle": r'GE [Jm$\mathbf{^{-2}}$]$\mathbf{\times10^5}$',
    "figname": 'generation_ae',
    "save": True
}

te.temporal_plot(args)

args={
    "caso": ["ERA_5","BAMHY"],
    "csst": "RainSS",
    "var" : 'Ckm',
    "title" :' H) Convertion KE into KZ',
    "xtitle": 'Time [Days]',
    "ytitle": r'CK [Jm$\mathbf{^{-2}}$]$\mathbf{\times10^5}$',
    "figname": 'convection_ke_kz',
    "save": True
}

te.temporal_plot(args)
