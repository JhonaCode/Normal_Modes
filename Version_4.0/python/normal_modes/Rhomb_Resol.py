import argparse
import subprocess
import os
from  types import SimpleNamespace

def get_Rhomb_Resol(args=None):
    """
    Parameters
    ----------
    args : 

    Returns
    -------
    """

     # Convert None to empty list
    if args is None:
        args = []

    parser = argparse.ArgumentParser(
        description=(
        "\n\n" 
        " Rhomb_Resol [Mmax] \n\n "
        "\n\n" 
        " default: Mmax=126'"  
        "\n\n" 

    ),
    formatter_class=argparse.RawTextHelpFormatter  # preserve line breaks
    )

    helped = parser.parse_args()

    Mmax, resdir = check_mmax(args)

    print(f"Mmax = {Mmax}, resdir = {resdir}")

    Mmx = Mmax - 1

    # Build Rhomb name depending on value
    if Mmx < 100:
        Rhomb = f"RB00{Mmx}"
    else:
        Rhomb = f"RB0{Mmx}"

    # Choose directory based on resdir
    if resdir == 1:
        fileRhomb = f"../Get_Rhomb_Res_GLats/dataout/{Rhomb}"
    else:
        fileRhomb = f"../../Get_Rhomb_Res_GLats/dataout/{Rhomb}"

    # Read file (assuming it's plain text with values separated by spaces)
    with open(fileRhomb, "r") as f:
        lines = f.readlines()


    # The "sublin(rec,2)" means second line (index 1 in Python)
    lrec = lines[0].strip().split()
    Imax, Jmax = int(lrec[0]), int(lrec[1])

    # Save result into file
    fileout = "Rhomb_Resol.txt"
    with open(fileout, "w") as fout:
        fout.write(f"{Rhomb} {Imax} {Jmax}\n")

    out=SimpleNamespace(
        Rhomb=Rhomb,
        Imax=Imax,
        Jmax=Jmax,
        )

    return out 


def check_mmax(args=None):
    """
    Check Mmax against allowed values and return resdir.

    * This procedure is hardwired for odd rhomboidal quadratica grid truncation
* Mmax : rhomb+1, rhomb is the zonal wave truncation (rhomb odd number)
* Mmax must be an even number and MOD(Mmax,2)=0
* Imax : number of longitude (at least 3*Mmax, for quadratic grid truncation)
*        Imax must be in the form : 2**n1 x 3**n2 x 5**n3, due to FFT
*        where n1=1,2,3,... ; n2=0,1,2,3,... ; n3=0,1,2,3,...
*        Imax should be a number in that format just above 3*Mmax
* Jmax : number of gaussian latitudes (at least 5*Mmax/2, or 5*Imax/6)
* Jmaxh=Jmax/2 must be a even number of latitudes by hemisphere and
*       Jmaxh/2 must be even due some coding logics, then MOD(Jmax,4)=0
* There is some selected cases for Mmax = 32, 64, 126, 132, 198, 264, 296 and 328.
* You can add your own Mmax, but take care with:
* MOD(Mmax,2)=0 ; MOD(Jmax,4)=0 ; Imax at least 3*Mmax and Jmax at leat 5*Imax/6
* Jmax should be the a number just above 5*Imax/6 such that MOD(Jmax,4)=0
* Calculate Imax first and then calculate Jmax
* These calculation is done at ${dirhome}/Get_Rhomb_Res

    """

    Mmax=args['Mmax']
    residir=args['resdir']

    # Default if empty
    if not Mmax:
        Mmax = 126

    # Allowed values
    allowed_mmax = [12, 160]

    # Check if Mmax is valid
    if int(Mmax) not in allowed_mmax:
        print("")
        print(f"Wrong Mmax: {Mmax}")
        print(f"Values Available: {' '.join(map(str, allowed_mmax))}")
        print("")
        return None  # equivalent to 'return' in GrADS function

    # resdir comes from args[1] (like subwrd(args,2)), default = 2
    resdir = None
    if args and len(args) >= 2:
        try:
            resdir = int(args['resdir'])
        except ValueError:
            resdir = args['resdir']  # keep as string if not numeric
    if not resdir:
        resdir = 2

    return Mmax, resdir
