##############3
from types import SimpleNamespace
#################
import normal_modes.Rhomb_Resol as RB

import os

def get_cross_section(args):
    
    csst=args['csst']

    #*Change LonA, LonB, LatA and LatB to your own use:
                       
    if (csst=='RainRS'):
    #* Rain over Rio Grande do Sul: April-May 2024
        LonA=-65.0
        LonB=-25.0                                           
        LatA= 0.0  
        LatB=-35.0

    if (csst=='RainSS'):              
    #* Rain over Sao Sebastiao: February 2023
        LonA=-65.0+360 
        LonB=-25.0+360
        LatA= 0.0   
        LatB=-35.0

    if (csst!='RainRS' and csst!='RainSS'):
    #* Defaut defined the same
        LonA=-65.0 
        LonB=-25.0
        LatA= 0.0  
        LatB=-35.0
              
    #filecrssct='Cross_Section.dgs'      
    #'!echo "'LonA' 'LonB' 'LatA' 'LatB'" > 'filecrssct
    
    fileout='Cross_Section.txt'
    with open(fileout, "w") as f:

        # First line
        f.write(f"{LonA} {LonB} {LatA} {LatB} \n")

    print(f"✅ written to {fileout}")

    out=SimpleNamespace(
        LonA=LonA,  
        LonB=LonB, 
        LatA=LatB,  
        LatB=LatB,  
        )
    
    return out
