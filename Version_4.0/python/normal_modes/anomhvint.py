#####################3
import  argparse
import  subprocess
from    types import SimpleNamespace
import  numpy as np
import  pandas as pd
import  xarray as xr
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
VDout ='/pesq/dados/bam/paulo.bonatti/Modal_Energetics/Version_4.0/Interaction_Horizontal_Vertical/dataout'
VMout ='/pesq/dados/bam/paulo.bonatti/Modal_Energetics/Version_4.0/Vertical_Modes/dataout'
dirv40='/home/paulo.bonatti/Modal_Energetics/Version_4.0'
fig_out   =''

def anomhvint(args=None):
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
        "  totalv [var] [atm] [caso] [epoca] [csst] [area] [perc] [xsec] [cnt]\n\n"
        "Default:\n"
        "  var=rbkv01 ;  atm=ht; epoca=37 ; csst=RainRS\n"
        "  area=local ; perc=Perc ; xsec=no ; cnt=0\n\n"
        "Arguments meaning:\n"
        "var : (wawbcaca) define the field to be plotted waves a and b, classes a and b"
        "  atm : ht for high troposphere or ct for medium troposphere'\n"
        "        or bt for botton troposphere'\n"
        "  caso  : five letters identifying the case\n"
        "  epoca : number identifying the datei and datef\n"
        "  csst  : six letters identifying the case study\n"
        "  area  : local for fixed area or global for full domain\n"
        "  perc  : Ener to plot energy or Perc to plot percentage\n"
        "  xsec  : yes to mark cross-section points, no otherwise\n"
        "  cnt   : lines interval\n"
    ),
    formatter_class=argparse.RawTextHelpFormatter  # preserve line breaks
    )
    helped = parser.parse_args()

    # Default values
    defaults = {
        "var"   : "rbkv01",
        "caso"  : "ERA_5",
        "atm"   : "ht",
        "epoca" : 37,
        "csst"  : "RainRS",
        "ht"    : "ht",
        "area"  : "local",
        "perc"  : "Perc",
        "xsec"  : "no",
        "cnt"   : 0,
        "color" : 'ocean_r',
        "show"  : True,
        "bcolor" : [],
        "fmt"  : '.1f',
        "units": ''
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


    var     =CD.trying(args,defaults,'var')
    atm     =CD.trying(args,defaults,'atm')
    caso    =CD.trying(args,defaults,'caso')
    epoca   =CD.trying(args,defaults,'epoca')
    csst    =CD.trying(args,defaults,'csst')
    area    =CD.trying(args,defaults,'area')
    perc    =CD.trying(args,defaults,'perc')
    xsec    =CD.trying(args,defaults,'xsec')
    cnt     =CD.trying(args,defaults,'cnt')
    color   =CD.trying(args,defaults,'color')
    bcolor  =CD.trying(args,defaults,'bcolor')
    show    =CD.trying(args,defaults,'show')
    fmt     =CD.trying(args,defaults,'fmt')
    units   =CD.trying(args,defaults,'units')

    #obtained from the variable
    wa=var[0:2]
    wb=var[2:4]
    ca=var[4]
    cb=var[5]

    # Print parsed values (like `say` in GrADS)
    print(f"var={var}, atm={atm}")
    print(f"caso={caso}, epoca={epoca}, csst={csst}")
    print(f"area={area}, perc={perc}, xsec={xsec}, cnt={cnt}")
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
    if (csst=='RainRS'):
        csstc='ClimRS'
    if (csst=='RainSS'):
        csstc='ClimSS'
    if (caso=='MONAN' or caso=='MONOP'):
        epocac=1
    else:
        epocac=2

    arg_cs={'caso'  :caso,
            'epoca' :epoca,
            'csst'  :csst,
            'dirv40':dirv40
            }

    csd=CD.csdata(arg_cs)

    za, zb = csd.zmap[int(ca)]
    zc, zd = csd.zmap[int(cb)]

    arg_csc={'caso':caso,
         'epoca':epocac,
         'csst':csstc,
         'dirv40':dirv40
        }

    csdc=CD.csdata(arg_csc)

    zac, zbc = csdc.zmap[int(ca)]
    zcc, zdc = csdc.zmap[int(cb)]

    ############################################################    

    rh =RB.get_Rhomb_Resol(args={'Mmax':Mmax,'resdir':1})

    trunc=rh.Rhomb+'L0'+str(Kmax)

    ############################################################    

    args_ah={'area':area,
           'Mmax':Mmax,
           'csst':csst
           }

    #Get AREA HIGHLIGHT
    ah=AH.get_area_highlight(args_ah)

    ############################################################    

    xsec='yes'
    if (xsec=='yes'): 

        #Get Cross Section 
        crs=CS.get_cross_section(args={'csst':csst})
        print(crs)

    ############################################################    

    #time
    #now = datetime.now()
    #dateg = now.strftime("%Y%m%d%H")   # like "202510011530"
    #print("dateg =", dateg)
    now = datetime.now()
    dateg = now.strftime("%Y%m%d%H")   # like "202510011530"

    ############################################################    
    #Get Pressure Layers

    pl=PL.PressLayer(args={'dirv40':dirv40,'op':1,'atm':atm})

    pfa=pl[atm]['pk1']
    pfb=pl[atm]['pk2']

    wave_map = {
    'rb': 'Rossby',
    'kv': 'Kelvin',
    'mx': 'Mixed',
    'gw': 'GravW',
    'ge': 'GravE'
    }
    
    Wave1 = wave_map.get(wa, 'Unknown')
    Wave2 = wave_map.get(wb, 'Unknown')

    cas=wa+'_C'+ca+'_'+wb+'_C'+cb
    CAS=Wave1+'_C'+ca+'_'+Wave2+'_C'+cb
    print('cas=',cas)

    date_format = '%Y%m%d%H'

    dateit=datetime.strptime(csd.datei, date_format)
    dateft=datetime.strptime(csd.datef, date_format)
    date_format = '%H%d%Y%b'
    dateiz=datetime.strftime(dateit, date_format)
    datefz=datetime.strftime(dateft, date_format)
    date_format = '%HZ%d%b%Y'


    ############################################################    

    filea='INHV'+caso+csst+csd.datei+csd.datef+csd.prev+trunc+'.ctl'
    fileb='INHVERA_5'+csstc+csdc.datei+csdc.datef+'P.icn.'+trunc+'.ctl'
    fileh='Vertical_Functions_'+csd.csvm+'.L0'+str(Kmax)+'.ctl'


    exp_name=''
    filea=VDout+'/'+filea
    v1 = down.open_grads(filea,exp_name)
    tosum1 = v1.sel(lev=slice(pfa, pfb)) 
    
    exp_name=''
    fileb=VDout+'/'+fileb
    v2 = down.open_grads(fileb,exp_name)
    tosum2 = v2.sel(lev=slice(pfa, pfb)) 

    exp_name=''
    fileh=VMout+'/'+fileh
    v3 = down.open_grads(fileh,exp_name)

    Wavea = wave_map.get(wa, 'Unknown')
    Waveb = wave_map.get(wb, 'Unknown')


    et1= getattr(tosum1,f"e{wa}{wb}{ca}{cb}").sum(dim="lev")
    et2= getattr(tosum2,f"e{wa}{wb}{ca}{cb}").sum(dim="lev")

    ett=(et1.isel(time=0).values-et2.isel(time=0).values)/1000.0

    # Create a new DataArray with the same coords as et1
    ett_da = xr.DataArray(
        ett,
        dims=('lat', 'lon'),
        coords={'lat': et1.lat, 'lon': et1.lon},
        attrs={'comment': 'Difference et1 - et2 [m2/s2]'}
    )


###################################################################

    ####################
    lats=[float(ah.LatS),float(ah.LatN),6]#float(ah.LatC)]
    lons=[float(ah.LonW),float(ah.LonE),6]#float(ah.LonC)]

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

    ha=GP.gethn(za,v3)
    hb=GP.gethn(zb,v3)
    hc=GP.gethn(zc,v3)
    hd=GP.gethn(zd,v3)
    na=za-1
    nb=zb-1
    nc=zc-1
    nd=zd-1

    #######################################
    date_format = '%b%Y'

    # Works for int, numpy.int64, or numpy.datetime64
    date_py = pd.to_datetime(v1.time[0].values)
    datez = date_py.strftime(date_format).upper()

    date2_format = '%HZ%d%b%Y'

    date2_py = pd.to_datetime(v2.time[0].values)
    date2z = date_py.strftime(date2_format).upper()

    if csst=='RainSS' or csst=='ClimSS':
        cssts='Sao Sebastiao'

    if csst=='RainRS' or csst=='ClimRS':
        cssts='Rio Grande do Sul'

    #tr =csssts+csst+ah.Center+'-'+trunc
    tr =cssts+'-'+trunc
    #tr='Case Study : '+csst+ah.Center+'-'+trunc  
    #tit=datez+' Minus April Monthly Mean'
    tit  = f" {date2z} minus Monthly Mean {datez} "

    if (caso=='ERA_5'):
        titb='Analysis: '+tit
    else:
        titb='3 Days Forecast: '+tit

    levl=f"Levels:{pfa:.1f}-{pfb:.1f} hPa" 

    label=f"{caso} Hor-Ver Energy Iter. {CAS}, {levl}\nClass{ca}: H{za}={ha} to H{zb}={hb}-Class{cb}: H{zc}={hc} to H{zd}={hd}\n{titb}"

    name=f"energy_iter_{cas}_anom_c{ca}_c{cb}_{atm}_{caso}_{csst}_{date2z}_{trunc}"

    #tr='Case Study: '+csst+ah.Center+'-'+trunc  

    ct= f"Contours: {bcolor[0]} to {bcolor[1]} by {dco:.1f} {units} - {tr} "

    ma.countour_plot(ett_da,lat=lats,lon=lons,
                    color=color,bcolor=bcolor,
                    units=units,figname=name,plotname=label ,xtitle=ct ,
                     show=show,fmt=fmt)


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
 
