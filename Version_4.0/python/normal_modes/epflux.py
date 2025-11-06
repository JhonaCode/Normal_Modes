#####################3
import  argparse
import  subprocess
from    types import SimpleNamespace
import  numpy as np
import  pandas as pd
#to get time
from    datetime import datetime
# Function with the definition of differents projetions
import  sources.cartopyplot   as ma 
import  grads.data_own   as down
#####################3
import normal_modes.get_folder     as fd
import normal_modes.Case_Dates     as CD
import normal_modes.Rhomb_Resol    as RB
import normal_modes.Area_Highlight as AH
import normal_modes.Cross_Section  as CS
import normal_modes.PressLayer     as PL
import normal_modes.Get_Player     as GP

#####Tenmq uye trovar ir ler diteramente
scripts='/home/jhonatan.aguirre/Modal_Energetics/Version_4.1/Eliassen_Palm_Flux/gs/dgs'
VDout ='/pesq/dados/bam/paulo.bonatti/Modal_Energetics/Version_4.0/Eliassen_Palm_Flux/dataout/'
VMout ='/pesq/dados/bam/paulo.bonatti/Modal_Energetics/Version_4.0/Vertical_Modes/dataout'
dirv40='/home/paulo.bonatti/Modal_Energetics/Version_4.0'
fig_out   =''

def epf(args=None):
    """
    Parameters
    ----------
    args : list[str] or None
          List of arguments (like sys.argv[1:]).
          If None, defaults are used.

    Returns
    -------
    dict
        Dictionary with keys: cs, caso, epoca, csst, area, perc, xsec, cnt
    """

     # Convert None to empty list
    if args is None:
        args = []

    parser = argparse.ArgumentParser(
        description=(
        "Plots the Total Energy of the Vertical Modes the Classes 0 to 4\n\n"
        "Usage:\n"
        "  epf { caso:, epoca:, csst:, magwind}\n\n"
        "Default:\n"
        "  caso=ERA_5 ;  epoca=37  ; csst=RainRS\n"
        "  lev =500   ;  magwind=6 \n"
        "Arguments meaning:\n"
        "  caso  : five letters identifying the case\n"
        "  epoca : number identifying the datei and datef\n"
        "  csst  : six letters identifying the case study\n"
        "magwind : reference value for wind magnitude \n"
    ),
    formatter_class=argparse.RawTextHelpFormatter  # preserve line breaks
    )
    helped = parser.parse_args()

    # Default values
    defaults = {
        "caso"  : "ERA_5",
        "epoca" : 37,
        "csst"  : "RainRS",
        "scale" : 100,
        "width" : 0.0025,
        "headlength" : 0.05,
        "magwind":6,
        "color" : 'ocean_r',
        "show"  : True,
        "bcolor": [],
        "lats": [],
        "fmt"   : '.1f',
        "units" : [],
    }


    # If nothing passed → just return defaults
    if not args:
        return defaults

    caso        = CD.trying(args,defaults,'caso')
    epoca       = CD.trying(args,defaults,'epoca')
    csst        = CD.trying(args,defaults,'csst')
    magwind     = CD.trying(args,defaults,'magwind')
    color       = CD.trying(args,defaults,'color')
    bcolor      = CD.trying(args,defaults,'bcolor')
    headlength  = CD.trying(args,defaults,'headlength')
    width       = CD.trying(args,defaults,'width')
    scale       = CD.trying(args,defaults,'scale')
    lats        = CD.trying(args,defaults,'lats')
    show        = CD.trying(args,defaults,'show')
    fmt         = CD.trying(args,defaults,'fmt')
    units       = CD.trying(args,defaults,'units')


    # Print parsed values (like `say` in GrADS)
    print(f"caso={caso}, epoca={epoca}, csst={csst}")
    print(f"magwind={magwind}")
    print(f"color={color}, bcolor={bcolor},  show={show}")

    # Spectral/vertical resolution
    Mmax = 160
    Kmax = 37
    print(f"Mmax = {Mmax}, Kmax = {Kmax}")

    ############################################################    

    if (csst=='RainRS'): 
         csstc='ClimRS'

    if (csst=='RainSS'): 
         csstc='ClimSS' 

    if (caso=='MONAN' or caso=='MONOP'):
        epocac=1
    else:
        epocac=2

    ############################################################    
    #*Getting dates
    #'run ../../Config/Case_Dates.gs 'caso' 'epoca' 'csst
    arg_cs={'caso'  :caso,
            'epoca' :epoca,
            'csst'  :csst,
            'dirv40':dirv40
            }

    csd =CD.csdata(arg_cs)

    ca=0
    cb=1

    za, zb = csd.zmap[int(ca)]
    zc, zd = csd.zmap[int(cb)]


    ############################################################    

    #time
    now = datetime.now()
    dateg = now.strftime("%Y%m%d")   # like "202510011530"

    ############################################################    

    date_format = '%Y%m%d%H'
    dateit=datetime.strptime(csd.datei, date_format)
    dateft=datetime.strptime(csd.datef, date_format)
    date_format = '%H%d%Y%b'
    dateiz=datetime.strftime(dateit, date_format)
    datefz=datetime.strftime(dateft, date_format)
    date_format = '%HZ%d%b%Y'

    ############################################################

    cx=csst[4:6] 

    if (cx== 'SS'):
        Loc='(45.5W,23.75S)' 
    if (cx== 'RS'):
        Loc='(53.5W,29.5S)'
    
    ############################################################    

    trunc='RB0159L0'+str(Kmax) 

    filea='EPF_'+caso+csst+csd.datei+csd.datef+csd.prev+trunc+'.ctl'

    exp_name=''
    fileg=VDout+'/'+filea
    v1 = down.open_grads(fileg,exp_name)


    fref=scripts+'/'+'EPF_'+csd.caso+csst+csd.datei+csd.datef+'.dgs' 
    with open(fref, 'r') as f:
        lines = f.readlines()


    #file norm 
    lrec   = lines[0].split()
    epfypx = lrec[0]  
    epfppx = lrec[1]
    dveppx = lrec[2]


    
    ylevs = np.array([1000, 950, 900, 850, 800, 750, 700, 650, 600, 550,
                  500, 450, 400, 350, 300, 250, 200, 150, 100, 70, 30, 1])

    ylevs= [1000,1,21]

    contourn = v1.dvep#.sel(lev=ylevs)

    #######################################
    #date_format = '%H%d%Y%b'
    date_format = '%b%Y'

    # Works for int, numpy.int64, or numpy.datetime64
    date_py = pd.to_datetime(v1.time[0].values)
    datez = date_py.strftime(date_format).upper()

    date2_format = '%HZ%d%b%Y'
    date2_py = pd.to_datetime(v1.time[0].values)
    date2z = date_py.strftime(date2_format).upper()

    if csst=='RainSS' or csst=='ClimSS':
        cssts='Sao Sebastiao'

    if csst=='RainRS' or csst=='ClimRS':
        cssts='Rio Grande do Sul'

    #tr ='Case Study:'+cssts+'-'+trunc
    tr =cssts+'-'+trunc #{Center}
    

    if bcolor:
        b1=bcolor[0]
        b2=bcolor[1]
        bn=bcolor[2]
    else: 
        b1=np.min(var[:])
        b2=np.max(var[:])
        bn=5


    levels= np.linspace(b1,b2,bn,endpoint=True)
    #levels= np.arange(b1,b2,bn)
    dco=levels[1]-levels[0]

    units='[hpa]'
    nabla=r"$\mathbf{\nabla \cdot F}$"
    ct= f"{nabla}: contours {bcolor[0]} to {bcolor[1]} by {dco:{fmt}} {units}"
    
    cf=csst[0:4]

    tita= f"EP Flux for {date2z} \n {caso} : {csst} {Loc} - QG"
    xlabel= f" Latitude \n {ct}"
    ylabel= f" Pressure [hpa]"
    figname=f"EPF_{caso}_{csst}_{csd.datei}_{csd.datef}"


    #text=r"f$_\psi$: epfypx [m$^3$s$^{-2}$]$f_p$: epfppx [Pa m$^{2}$s$^{-2}$] $\mathbf{\nabla \cdot f}$: dveppx [m$^2s$^{-2}$]"

    text = '\n'.join((
    r"$F_\psi$: %s [m$^3$s$^{-2}$]"%(epfypx),
    r"$F_p$: %s [Pa m$^{2}$s$^{-2}$]"%(epfppx), 
    r"$\mathbf{\nabla \cdot F}$: %s [m$^2$s$^{-2}$]"%(dveppx)
    ))


    ma.cartopy_vector_1d('epfy','epfp',v1,contourn,scale=scale, width=width,lat=lats,lev=ylevs,color=color,bcolor=bcolor,figname=figname,plotname=tita,magwind=magwind,xtitle=xlabel,ytitle=ylabel ,cbar=False ,units=units, show=show,fmt=fmt,headlength=headlength,save=False,text=text)


    return

def chkmdls():
    """Dummy check (replace with real one)."""
    return  

def gethn(zz, ds):
    """
    Python equivalent of the GrADS gethn function.
    
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



# Example usage
if __name__ == "__main__":

    arg={
        "cs": 0,
        "caso": "ERA_5",
        "epoca": 37,
        "csst": "RainRS",
        "area": "local",
        "perc": "Perc",
        "xsec": "no",
        "cnt": 0,
    }
    # If nothing passed
    print(arguments(arg))
 
