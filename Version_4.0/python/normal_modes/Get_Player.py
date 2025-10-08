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
"""
import math

def read_pressure_levels(FilePres, Kmax):
    """Read pressure levels from file ."""
    nRec = Kmax / 10
    print(nRec)
    if int(nRec) != nRec:
        nRec = int(nRec) + 1
    else:
        nRec = int(nRec)

    PrsLev = []
    with open(FilePres, "r") as f:
        for _ in range(nRec):
            rec = f.readline().strip()
            if not rec:
                break
            lrec = rec.split()
            for re in lrec: 
                PrsLev.append(float(re))
    return PrsLev


def format_pk(pk):
    """Return integer if pk is whole number, else float."""
    return int(pk) if int(pk) == pk else pk


def get_layer(name, pmax, pmin, start_idx, PrsLev, Kmax, inclusive=False):
    """
    Extracts a pressure layer from PrsLev.
    If inclusive=True, pmin is included (>=).
    """
    end_idx = start_idx
    nlev = 0
    for k in range(start_idx, Kmax + 1):
        pk = float(PrsLev[k - 1])
        if (pmax >= pk > pmin) or (inclusive and pmax >= pk >= pmin):
            nlev += 1
            end_idx = k
        else:
            break

    pk1 = format_pk(PrsLev[start_idx - 1])
    pk2 = format_pk(PrsLev[end_idx - 1])

    #rpk = f"{name} {pk1} {pk2} {name.upper()} <={pmax}>{pmin}hPa {start_idx}_{end_idx}:{nlev}_Levels"

    rpk = { 
            #f"name"     :name, 
            f"pk1"      :pk1,  
            f"pk2"      :pk2, 
            f"pmax"     :pmax,
            f"pmin"     :pmin, 
            f"start_idx":start_idx,
            f"end_idx"  :end_idx,
            f"nlev"     :nlev,

    }

    return rpk, end_idx, nlev

def gethn(zz, ds):
    """
    
    Parameters
    ----------
    zz : int
        Vertical level index (z coordinate).
    ds : xarray.Dataset
        Dataset that has variable 'dn' with dimensions (time, z, y, x).
    
    Returns
    -------
    str
        Formatted number as a string.
    """
    # Extract value at x=1, y=1, z=zz, t=1
    # (GrADS indices are 1-based; Python is 0-based)

    zz=int(zz)-1

    hh = float(ds['dn'].isel(time=0,lat=0,lon=zz).values)


    # Choose format string based on magnitude
    if hh >= 1000:
        fmt = "{:6.1f}"
    elif 100 <= hh < 1000:
        fmt = "{:6.2f}"
    elif 10 <= hh < 100:
        fmt = "{:6.3f}"
    elif 1 <= hh < 10:
        fmt = "{:6.4f}"
    else:
        fmt = "{:6.4f}"

    # Format and return
    hn = fmt.format(hh)

    return hn


