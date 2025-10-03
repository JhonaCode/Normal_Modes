import os
from types import SimpleNamespace

dirv40='/home/paulo.bonatti/Modal_Energetics/Version_4.0'

def trying(args,default,arg):

    try:
        var  =args[arg]       
    except:
        var =default[arg]

    return var 


def csdata(args=None):

    defaults = {
        "caso": "ERA_5",
        "epoca": 37,
        "csst": "RainRS",
        "op": 3,
    }   

    caso =trying(args,defaults,'caso')
    epoca=trying(args,defaults,'epoca')
    csst =trying(args,defaults,'csst')
    op   =trying(args,defaults,'op')


    if (op==3):
      dirg=dirv40+'/Config/'
    
    print( 'caso=',caso,'epoca=',epoca,'csst=',csst,'dirg=',dirg,'op =',op )

    
    #* Getting dirdinp to input the data
    #filedir=dirg+'Config_Dir'
    #dirdinp = find_variable_in_file(filedir,'dirdinp', nro=7, max_lines=5)
    #diri=dirdinp+'/' 
    #print(diri)

     # --------------- Check caso -------------------
    res = chkcase(caso, dirg)
    if res == 'no':
        print("Error: wrong caso")
        return

    # --------------- Check csst -------------------
    res = chkcsst(csst, caso, dirg)
    excsst, excscs = res[0], res[1]
    if excsst == 'no':
        print("Error: wrong csst")
        return
    if excscs == 'no':
        print("Error: caso not available for csst")
        return

    # --------------- Reference Case ----------------
    fref = os.path.join(dirg, 'Reference_Case')
    with open(fref, 'r') as f:
        lines = f.readlines()

    # Parse csvm and Kmax
    lrec = lines[1].strip()
    csvm = lrec[5:10]   # equivalent to substr(lrec,6,5)
    Kmax = lrec[5:7]    # equivalent to substr(lrec,6,2)



    #number of dates 
    ne = check_epoca(dirg, caso, csst,epoca)

    #Fixed Vertical Modes Classes (0, 1, 2, 3, and 4) Distribution:
    #Same as Reference Case csvm for All Cases
    z0a=1 
    z0b=5
    z1a=6
    z1b=11
    z2a=12
    z2b=19
    z3a=20 
    z3b=29
    z4a=30 
    z4b=37

    # --------------- Dates Caso ----------------
    fref = os.path.join(dirg, 'Dates_'+caso+'_'+csst+'.dgs')
    with open(fref, 'r') as f:
        lines = f.readlines()

    epoch = datei = datef = lonc = latc = None

    for ne, line in enumerate(lines[1:], start=1):  # skip header, start count at 1
        parts = line.strip().split()
    
        if len(parts) < 5:
            continue  # skip malformed lines
    
        epoch, datei, datef, lonc, latc = parts[0:5]
    
        if epoch == str(epoca):   # compare epoch with given epoca
            break

    if (datei==datef):
      prev='P.icn.'
    else:
      prev='P.fct.'

    outfile="./Case_Dates.txt"
    with open(outfile, "w") as f:

        # First line
        f.write(f"{Kmax} {datei} {datef} {prev} {csvm} {caso} {lonc} {latc}\n")
        # Second line
        f.write(f"{z0a} {z0b} {z1a} {z1b} {z2a} {z2b} {z3a} {z3b} {z4a} {z4b}\n")

    print(f"✅ Case_Dates.dgs written to {outfile}")

    out=SimpleNamespace(
         Kmax  =Kmax,
         datei =datei, 
         datef =datef,
         prev  = prev,
         csvm  = csvm,
         caso  = caso,
         lonc  = lonc,
         latc  = latc,
         z0a   =  z0a,
         z0b   =  z0b,
         z1a   =  z1a,
         z1b   =  z1b,
         z2a   =  z2a,
         z2b   =  z2b,
         z3a   =  z3a,
         z3b   =  z3b,
         z4a   =  z4a,
         z4b   =  z4b,
        )

    return out 
    

def chkcase(caso, dirg):
    """
    Check if the given case exists in the Cases_List file.

    Args:
        caso (str): The case to check.
        dirg (str): Directory containing 'Cases_List'.

    Returns:
        str: 'yes' if the case exists, 'no' otherwise.
    """

    fcase = os.path.join(dirg, "Cases_List")

    # Read the file
    with open(fcase, 'r') as f:
        lines = f.readlines()
        #print(lines)


    # Get the second line
    if len(lines) < 2:
        raise ValueError(f"File {fcase} has less than 2 lines.")

    lrec = lines[0].rstrip()  # remove newline

    # Get number of cases (substr(lrec,8,2) in KornShell)
    ncases_str = lrec[7:9]  # Python is 0-indexed

    try:
        ncases = int(ncases_str)
    except ValueError:
        raise ValueError(f"Cannot parse number of cases from '{ncases_str}'")

    lrec = lines[1].rstrip()  # remove newline

    # Get the list of cases (substr(lrec,9,nstr-9))
    lcases = lrec[8:].strip()  # everything after the 8th character

    # Split into individual cases (assuming space-separated)
    cases_list = lcases.split()

    # Check if caso is in the list
    if caso in cases_list:
        excs = 'yes'
        print(f"\n Correct Case: {caso}")
    else:
        excs = 'no'
        print(f"\n Error: Wrong Case: {caso}")
        print(f" Must be: {' '.join(cases_list)}")

    return excs

def chkcsst(csst, caso, dirg):
    """
    Check if the given case study (csst) exists inside the CsSt_List file.
    Equivalent of the GrADS function chkcsst.
    """
    import os

    fcsst = os.path.join(dirg, "CsSt_List")

    try:
        with open(fcsst, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File {fcsst} not found")
        return "no no"

    # First relevant line -> number of case studies
    lrec = lines[0].strip().split()
    ncsst = int(lrec[0])  # first word = number of cssts

    # Second relevant line -> list of case studies
    lcsst = lines[1].strip().split()

    excsst = "no"
    for csstx in lcsst:
        if csst == csstx:
            excsst = "yes"
            break

    if excsst == "no":
        print()
        print(f" Error: Wrong Case Study: {csst}")
        print(" Must be :", " ".join(lcsst))
        print()
        return "no no"
    else:
        print()
        print(f" Correct Case Study: {csst}")
        return "yes"


def check_epoca(dirg, caso, csst, epoca):

    fileg = os.path.join(dirg, f"Dates_{caso}_{csst}.dgs")

    try:
        with open(fileg, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File {fileg} not found")
        return "no no"

    # second line in file
    if len(lines) < 2:
        print(f"\n Error: file {fileg} does not contain enough lines\n")
        return None


    lrec = lines[0].strip().split()
    nd = int(lrec[0])   # first word is nd

    if epoca < 1 or epoca > nd:
        print()
        print(f" Wrong epoca = {epoca}")
        print(f" Must be >= 1 and <= {nd}")
        print()
        return None

    return nd


if __name__== "__main__":

    csdata()
