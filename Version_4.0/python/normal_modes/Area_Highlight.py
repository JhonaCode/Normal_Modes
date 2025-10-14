####################33
from   types import SimpleNamespace
import os
####################33
import normal_modes.Rhomb_Resol as RB
def get_area_highlight(args):
    
    """
    * LonW : longitude west of the local area
    * LonE : longitude east of the local area
    * LatS : latitude sul of the local area
    * LonW : latitude norh of the local area
    * Center: longitude and latitude of the center of domain
    * ECArea: area for the energy cycle
    * Note that (LonE-LonW) must be equal 2 x (LatN-LatS)
    * to Get the Title and the Labels at the Correct Place
    * May be you will get a wider area than yo want
    * Change LonW, LonE, LatS and LatN to your own use:
    *
    * LonC, LatC: Longitude and Latitude to be highlighted.
    * If there is no one put LatC>90.0 and LonC>360.0.
    * Change LonC and LatC to your own use
    *
    """
    area=args['area']
    Mmax=args['Mmax']
    csst=args['csst']

    if (area == 'local'):

        if (csst=='RainRS' or csst=='ClimRS'):
            LonW=-110.0  
            LonE=-10.0
            LatS=-45.0 
            LatN=5.0
            LonC=-53.25 
            LatC=-29.4382
            Center='(53.3W,29.4S)'
            ECArea='63.8W-42.8W_39.8S-19.1S'

        if (csst=='RainSS' or csst=='ClimSS'):
            LonW=0.0 
            LonE=360.0
            LatS=-60.0  
            LatN=30.0
            LonC=-45.75 
            LatC=-23.5955
            Center='(45.8W,23.6S)'
            ECArea='55.5W-35.5W_33.75S-13.75S'

        if (csst!='RainRS' and csst!='RainSS' and csst!='ClimRS' and csst!='ClimSS'):
           #* Default
            LonW=-110.0 
            LonE=-10.0
            LatS=-45.0  
            LatN=5.0
            LonC=370.0  
            LatC=100.0
            Center='(60W,20S)'
            ECArea='110W-10W_45S-5N'
    else:
       #*This is to perform the Maximum calculation correctly
       #*for area = global
        LatS=-90.0
        LatN=90
        LonW=0.0
        LonE=360.0
        LonC=370.0
        LatC=100.0
        Center='(180W,0)'
        ECArea='0-360_90S-90N'
    
    fileout='Area_Highlight.txt'
    #'!echo "'LonW' 'LonE' 'LatS' 'LatN'" > 'fileout
    #'!echo "'LonC' 'LatC'" >> 'fileout
    #'!echo "'Center' 'ECArea'" >> 'fileout
    with open(fileout, "w") as f:

        # First line
        f.write(f"{LonW} {LonE} {LatS} {LatN} \n")
        # Second line
        f.write(f"{LonC} {LatC} \n")
        # Second line
        f.write(f"{Center} {ECArea} \n")

    print(f"✅ written to {fileout}")

    out=SimpleNamespace(
        LonW=LonW,  
        LonE=LonE, 
        LatS=LatS,  
        LatN=LatN,  
        LonC=LonC,   
        LatC=LatC,   
        Center=Center,
        ECArea=ECArea,
        )
    
    return out
