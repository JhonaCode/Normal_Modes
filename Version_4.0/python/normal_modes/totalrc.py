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
VDout ='/pesq/dados/bam/paulo.bonatti/Modal_Energetics/Version_4.0/Hor_Ver_Recomposition/dataout'
VMout ='/pesq/dados/bam/paulo.bonatti/Modal_Energetics/Version_4.0/Vertical_Modes/dataout'
dirv40='/home/paulo.bonatti/Modal_Energetics/Version_4.0'
fig_out   =''

def totalrc(args=None):
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
        "  totalrc  [caso] [epoca] [csst] [lev] [magwind]\n\n"
        "Default:\n"
        "  caso=ERA_5 ;  epoca=37  ; csst=RainRS\n"
        "  lev =500   ;  magwind=6 \n"
        "Arguments meaning:\n"
        "  caso  : five letters identifying the case\n"
        "  epoca : number identifying the datei and datef\n"
        "  csst  : six letters identifying the case study\n"
        "     lv : pressure level\n"
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
        "lev"   : 500,
        "scale" : 100,
        "width" : 0.0025,
        "headlength" : 0.05,
        "magwind":6,
        "color" : 'ocean_r',
        "show"  : True,
        "bcolor": [],
        "lats": [],
        "lons": [],
        "fmt"   : '.1f',
        "units" : [],
    }

    """
    folders=fd.get_export_vars('../Config/Config_Dir')
    
    #get_in_file('../')
    # Now you can access the variables
    dirhome=folders["dirhome"]
    dirdata=folders["dirdata"]
    dirdinp=folders["dirdinp"]
    """

    # If nothing passed → just return defaults
    if not args:
        return defaults

    caso    =CD.trying(args,defaults,'caso')
    epoca   =CD.trying(args,defaults,'epoca')
    csst    =CD.trying(args,defaults,'csst')
    lev     =CD.trying(args,defaults,'lev')
    magwind =CD.trying(args,defaults,'magwind')
    color   =CD.trying(args,defaults,'color')
    bcolor  =CD.trying(args,defaults,'bcolor')
    headlength  =CD.trying(args,defaults,'headlength')
    width  =CD.trying(args,defaults,'width')
    scale  =CD.trying(args,defaults,'scale')
    lons    =CD.trying(args,defaults,'lons')
    lats    =CD.trying(args,defaults,'lats')
    show    =CD.trying(args,defaults,'show')
    fmt     =CD.trying(args,defaults,'fmt')
    units   =CD.trying(args,defaults,'units')

    # Print parsed values (like `say` in GrADS)
    print(f"caso={caso}, epoca={epoca}, csst={csst}")
    print(f"lev={lev}, magwind={magwind}")
    print(f"color={color}, bcolor={bcolor},  show={show}")

    # Placeholder for chkmdls()
    rec = chkmdls()
    if rec != 0:
        return

    # Spectral/vertical resolution
    Mmax = 160
    Kmax = 37
    print(f"Mmax = {Mmax}, Kmax = {Kmax}")

    ############################################################    
    #*Getting dates
    #'run ../../Config/Case_Dates.gs 'caso' 'epoca' 'csst
    arg_cs={'caso'  :caso,
            'epoca' :epoca,
            'csst'  :csst,
            'dirv40':dirv40
            }

    csd=CD.csdata(arg_cs)

    ca=0
    cb=1
    za, zb = csd.zmap[int(ca)]
    zc, zd = csd.zmap[int(cb)]
    ##########################################################
    rh =RB.get_Rhomb_Resol(args={'Mmax':Mmax,'resdir':1})

    trunc=rh.Rhomb+'L0'+str(Kmax)

    ############################################################    

    cx=csst[4:6] 

    if (cx== 'RS'):
      exta='S003_S003_H00_H04'
      extb='S001_S001_H00_H04'
    if (cx== 'SS'):
      exta='S004_S004_H00_H04'
      extb='S001_S001_H05_H10'
    

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

    filea='UVHS'+caso+csst+csd.datei+csd.datef+csd.prev+trunc+'_'+exta+'.ctl'
    fileb='UVHS'+caso+csst+csd.datei+csd.datef+csd.prev+trunc+'_'+extb+'.ctl'

    exp_name=''
    fileg=VDout+'/'+filea
    v1r = down.open_grads(fileg,exp_name)
    v1  = v1r.sel(lev=lev) 
    
    exp_name=''
    fileg=VDout+'/'+fileb
    v2r = down.open_grads(fileg,exp_name)
    v2  = v2r.sel(lev=lev) 

    if (cx=='RS'):
        htt=v1.hrb+v2.hkv+v2.hmx
        utt=v1.urb+v2.ukv+v2.umx
        vtt=v1.vrb+v2.vkv+v2.vmx

    if (cx=='SS'):
        htt=v1.hrb+v2.hkv
        utt=v1.urb+v2.ukv
        vtt=v1.vrb+v2.vkv

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

    ct= f"Contours: {bcolor[0]} to {bcolor[1]} by {dco:{fmt}} {units}"

    ha='9746.3'
    hb='641.4'
    hc='434.5'
    hd='125.1'
    za='00'
    zb='04'
    zc='05'
    zd='10'

    if (cx=='RS'):
        xla='Rb:S3 MX_KV:S1 C0'
        xlb='Class 0: H'+za+'='+ha+' to H'+zb+'='+hb
        fg ='RbS3_MxKvS1_C0'
        Center='(53.3W,29.4S)'
    if (cx=='SS'):
        xla='Rb:S4_C0 KV:S1_C1'
        xlb='RbS4C0: H'+za+'='+ha+'-H'+zb+'='+hb+' KvS1C1: H'+zc+'='+hc+'-H'+zc+'='+hc
        fg='RbS4C0_KvS1C1'
        Center='(45.8W,23.6S)'
    
    #cf=csst[0:4]
    #tcs = 'Monthly Mean: ' if cf == 'Clim' else tcs
    #tcs = 'Date: ' if cf == 'Rain' else tcs

    #######################################
    #date_format = '%H%d%Y%b'
    date_format = '%b%Y'

    # Works for int, numpy.int64, or numpy.datetime64
    date_py = pd.to_datetime(v1.time[0].values)
    datez = date_py.strftime(date_format).upper()

    if csst=='RainSS' or csst=='ClimSS':
        cssts='Sao Sebastiao'

    if csst=='RainRS' or csst=='ClimRS':
        cssts='Rio Grande do Sul'

    #tr ='Case Study:'+cssts+'-'+trunc
    tr =cssts+'-'+trunc #{Center}
    
    if (caso=='ERA_5'):
        titb='Analysis: '
    else:
        titb='3 Days Forecast: '

    titb  = f"Montly Mean {datez}"



    tita= f"{caso} {cssts} Wind and Geopotential Height \n{titb} for Level={lev} [hPa]" 
    xlabel= f"{ct} - {tr} \n {xla} {xlb}"

    figname=f"Wind_Geop_Height_Triplet_{fg}_Total_{caso}_{csst}_{datez}_{lev}_hPa"

    ma.cartopy_vector(utt,vtt,v1,data2=htt,scale=scale, width=width,lat=lats,lon=lons,color=color,bcolor=bcolor,figname=figname,plotname=tita,magwind=magwind,xtitle=xlabel ,cbar=False ,units=units, show=show,fmt=fmt,headlength=headlength,save=True)


    return

def chkmdls():
    """Dummy check (replace with real one)."""
    return 0

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
 
