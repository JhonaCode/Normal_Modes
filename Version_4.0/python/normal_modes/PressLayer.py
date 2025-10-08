"""
*Four Layers
* lt : Lower_Troposphere  <= po >  pb
* mt : Medium_Troposphere <= pb >  pm
* ut : Upper_Troposphere  <= pm >  pa
* st : Stratosphere_Above <= pa >= pt
*      pt : last level of the csvm
* You can change for your own use, but
* take care: to work po, pb, pm and pa
* must be levels of the case.

* Three Layers
* bt : Bottom_Troposphere <= po > pm
* ct : Center_Troposphere <= pb => pa
* ht : Higher_Troposphere  < pm => ph
* You can choose your own po, pb, pm, pa, ph, but take care:
* if pm is a level of the csvm it will be excluded
* if pm is not a level of the csvm you have to change
* dkh to change the initialization of kht1=kbt2+dkh:
* dkh=2 to exclude pm
* dkh=1 to include pm


* lt : Lower_Troposphere <= 1000 > 700 hPa
* mt : Medium_Troposphere <= 700 > 400 hPa
* ut : Upper_Troposphere  <= 400 > 200 hPa
* st : Stratosphere_Above <= 200 >= pt hPa
*      pt : last level of the csmv
* bt : Bottom_Troposphere <= 1000 > 500 hPa
* ct : Bottom_Troposphere <= 700 >= 300 hPa
* ht : Higher_Troposphere   < 500 > 100 hPa


"""

############################
import  normal_modes.Get_Player     as GP
import  normal_modes.Case_Dates     as CD

############################
import os
import  math 
from    types import SimpleNamespace

def PressLayer(args=None):

    """
    atm    : str, requested layer ('lt','mt','ut','st','bt','ct','ht')
    layers : dict, mapping layer -> (pfa, pfb)
    PrsLev : list of available pressure levels
    
    returns: (pfa, pfb, kfa, kfb)
    """

    defaults = {
        "dirv40": '../' ,
        "atm": 'mt',
        "op": 1,
    }   
    dirv40  =CD.trying(args,defaults,'dirv40')
    op      =CD.trying(args,defaults,'op')
    atm     =CD.trying(args,defaults,'atm')

    layers = {
    "lt",##: (pklt1, pklt2),
    "mt",##: (pkmt1, pkmt2),
    "ut",##: (pkut1, pkut2),
    "st",##: (pkst1, pkst2),
    "bt",##: (pkbt1, pkbt2),
    "ct",##: (pkct1, pkct2),
    "ht",##: (pkht1, pkht2),
    }
    
    if atm not in layers:
        print(" ")
        print(f" Wrong atm = {atm}")
        print(" atm must be: lt, mt, ut, st, bt, ct, ht")
        print(" ")
        return None

    if (op==1):
        dirg=dirv40+'/Config/'
        dirp=dirv40

    # --------------- Reference Case ----------------
    fref = os.path.join(dirg, 'Reference_Case')
    with open(fref, 'r') as f:
        lines = f.readlines()

    # Parse csvm and Kmax
    lrec = lines[0].strip()
    csvm = lrec[5:10]        # equivalent to substr(lrec,6,5)
    lrec = lines[1].strip()
    Kmax = int(lrec[5:7])    # equivalent to substr(lrec,6,2)

    if (Kmax < 100):
        FilePres=f"{dirp}/Pressure_Levels/PressureLevels_{csvm}.L0{Kmax}"
    else:
        FilePres=f"{dirp}/Pressure_Levels/PressureLevels_{csvm}.L{Kmax}"
    
    #* Read Pressure Levels
    PrsLev=GP.read_pressure_levels(FilePres,Kmax) 

    # Join with '%'
    #PrsLev = "%".join(PrsLev)

    po=1000
    pb=700
    pm=400
    pa=200
    ph=100
    dkh=2

    klt1=1
    klt2=klt1

    # Lower Troposphere
    rpklt, klt2, nlt = GP.get_layer("lt", po, pb, klt1, PrsLev, Kmax)
    
    # Medium Troposphere
    rpkmt, kmt2, nmt = GP.get_layer("mt", pb, pm, klt2 + 1, PrsLev, Kmax)
    
    # Upper Troposphere
    rpkut, kut2, nut = GP.get_layer("ut", pm, pa, kmt2 + 1, PrsLev, Kmax)
    
    # Stratosphere (top until pt = lowest pressure)
    pt = float(PrsLev[Kmax - 1])
    rpkst, kst2, nst = GP.get_layer("st", pa, pt, kut2 + 1, PrsLev, Kmax)

    # Adjust po if needed
    if PrsLev[0] > po:
        po = PrsLev[0]
    
    # Lower Troposphere
    # ---- Bottom Troposphere ----
    rpkbt, kbt2, nbt = GP.get_layer("bt", po, pm, 1, PrsLev, Kmax)
    
    # ---- Center Troposphere ----
    # Find where pk == pb
    kct1 = next((k+1 for k, pk in enumerate(PrsLev) if math.isclose(pk, pb, abs_tol=1e-5)), None)
    rpkct, kct2, nct = GP.get_layer("ct", pb, pa, kct1, PrsLev, Kmax, inclusive=True)
    
    # ---- Higher Troposphere ----
    kht1 = kbt2 + dkh
    rpkht, kht2, nht = GP.get_layer("ht", pm, ph, kht1, PrsLev, Kmax, inclusive=True)

    layers = {
    "lt": rpklt,
    "mt": rpkmt,
    "ut": rpkut,
    "st": rpkst,
    "bt": rpkbt,
    "ct": rpkct,
    "ht": rpkht,
    }

    #print(layers['lt']['pk1'])

    PresLay='Pressure_Layers.txt'
    ################
    """
    # Save them to file (overwrite first, append the rest)
    with open(f"{PresLay}", "w") as f:
        for name, values in layers.items():
           #f.write(f"{name} {values[0]} {values[1]} {values[2]}\n")
    """
    ################

    with open(f"{PresLay}", "w") as f:
        for name, vals in layers.items():
            line = f"{name} " + " ".join(f"{k}={v}" for k, v in vals.items())
            f.write(line + "\n")

    print(f"✅ {PresLay} written ")

    return layers 

"""
    def get_pressure_range(atm, layers, PrsLev):
    
        # get layer pressures
        pfa, pfb = layers[atm]

        # find their indices (like GrADS query dims, 1-based index)
        try:
            kfa = PrsLev.index(float(pfa)) + 1
        except ValueError:
            kfa = None
        
        try:
            kfb = PrsLev.index(float(pfb)) + 1
        except ValueError:
            kfb = None
        
        print(" ")
        print(f" atm = {atm}  pfa = {pfa}  pfb = {pfb}  kfa = {kfa}  kfb = {kfb}")
        return pfa, pfb, kfa, kfb
         
"""
