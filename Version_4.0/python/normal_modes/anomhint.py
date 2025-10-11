#####################3
import  argparse
import  subprocess
import  numpy as np
from    types import SimpleNamespace
#to get time
from    datetime import datetime
import  pandas as pd
import  xarray as xr
# Function with the definition of differents projetions
import  sources.cartopyplot   as ma 
import  grads.data_own   as down
#####################3
import normal_modes.get_folder     as fd
import normal_modes.Case_Dates     as CD
import normal_modes.Rhomb_Resol    as RB
import normal_modes.Area_Highlight as AH
import normal_modes.Cross_Section  as CS
import normal_modes.Get_Player     as GP

#####Tenmq uye trovar ir ler diteramente
VDout ='/pesq/dados/bam/paulo.bonatti/Modal_Energetics/Version_4.0/Horizontal_Decomposition/dataout'
VMout ='/pesq/dados/bam/paulo.bonatti/Modal_Energetics/Version_4.0/Vertical_Modes/dataout'
dirv40='/home/paulo.bonatti/Modal_Energetics/Version_4.0'
fig_out   =''

def arguments(args=None):
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
        " Plots the Total Energy of the Horizontal Modes the Classes 0 to 4\n\n"
        "Usage:\n"
        "  totalhint [wa] [wb] [cs] [caso] [epoca] [csst] [area] [perc] [xsec] [cnt]\n\n"
        "Default:\n"
        "  wa=rb; wb=kv ; cs=0 ; caso=ERA_5 ; epoca=37 ; csst=RainRS'\n"
        "  area=local ; perc=Perc ; xsec=no ; cnt=0\n\n"
        "Arguments meaning:\n"
        "  wa    : horizontal mode (rb, kv, mx, gw or ge)\n"
        "  wb    : horizontal mode (rb, kv, mx, gw or ge)\n"
        "  cs    : vertical mode (0, 1, 2, 3 or 4)\n"
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
        "wa"   : 'rb',
        "wb"   : 'kv',
        "cs"   : 0,
        "caso" : "ERA_5",
        "epoca": 37,
        "csst" : "RainRS",
        "area" : "local",
        "perc" : "Perc",
        "xsec" : "no",
        "cnt"  : 0,
        "color": 'ocean_r',
        "show" : True,
        "bcolor" : [],
        "fmt"  : '%.1f',
        "units"  : '',
    }

    # If nothing passed → just return defaults
    if not args:
        return defaults

    wa   =CD.trying(args,defaults,'wa')
    wb   =CD.trying(args,defaults,'wb')
    cs   =CD.trying(args,defaults,'cs')
    caso =CD.trying(args,defaults,'caso')
    epoca=CD.trying(args,defaults,'epoca')
    csst =CD.trying(args,defaults,'csst')
    area =CD.trying(args,defaults,'area')
    perc =CD.trying(args,defaults,'perc')
    xsec =CD.trying(args,defaults,'xsec')
    cnt  =CD.trying(args,defaults,'cnt')
    color=CD.trying(args,defaults,'color')
    bcolor=CD.trying(args,defaults,'bcolor')
    show =CD.trying(args,defaults,'show')
    fmt  =CD.trying(args,defaults,'fmt')
    units=CD.trying(args,defaults,'units')

    # Print parsed values (like `say` in GrADS)
    print('wa=',wa ,'wb=',wb, 'cs=',cs ,'caso=',caso, 'epoca=',epoca, 'csst=',csst, 'area=',area, 'perc=',perc, 'xsec=',xsec, 'cnt=',cnt)

    ##################################################

    # Placeholder for chkmdls()
    rec = chkmdls()
    if rec != 0:
        return

    # Spectral/vertical resolution
    Mmax = 160
    Kmax = 37
    print(f"Mmax = {Mmax}, Kmax = {Kmax}")

    ######################################################
    if (csst=='RainRS'):
        csstc='ClimRS'
    if (csst=='RainSS'):
        csstc='ClimSS'
    if (caso=='MONAN' or caso=='MONOP'):
        epocac=1
    else:
        epocac=2

    arg_cs={'caso':caso,
         'epoca':epoca,
         'csst':csst,
         'dirv40':dirv40
        }

    csd=CD.csdata(arg_cs)

    zca, zcb = csd.zmap[cs]

    arg_csc={'caso':caso,
         'epoca':epocac,
         'csst':csstc,
         'dirv40':dirv40
        }

    csdc=CD.csdata(arg_csc)

    zcac, zcbc = csdc.zmap[cs]
    ##################################################

    rh =RB.get_Rhomb_Resol(args={'Mmax':Mmax,'resdir':1})

    trunc=rh.Rhomb+'L0'+str(Kmax)

    args_ah={'area':area,
           'Mmax':Mmax,
           'csst':csst
           }


    #Get AREA HIGHLIGHT
    ah=AH.get_area_highlight(args_ah)
    print(ah)

    ##################################################
    xsec='yes'
    if (xsec=='yes'): 

        #Get Cross Section 
        crs=CS.get_cross_section(args={'csst':csst})
        print(crs)

    ##################################################
    filea='ENCL'+caso+csst+csd.datei+csd.datef+csd.prev+trunc+'.ctl'

    fileb='ENCLERA_5'+csstc+csdc.datei+csdc.datef+'P.icn.'+trunc+'.ctl'
    fileh='Vertical_Functions_'+csd.csvm+'.L0'+str(Kmax)+'.ctl'

    exp_name=''
    filea=VDout+'/'+filea
    v1 = down.open_grads(filea,exp_name)
    
    exp_name=''
    fileb=VDout+'/'+fileb
    v2 = down.open_grads(fileb,exp_name)

    exp_name=''
    fileh=VMout+'/'+fileh
    v3 = down.open_grads(fileh,exp_name)

    et1= getattr(v1,f"et{wa}{wb}{cs}")
    et2= getattr(v2,f"et{wa}{wb}{cs}")

    ett=(et1.isel(time=0).values-et2.isel(time=0).values)/1000.0

    # Create a new DataArray with the same coords as et1
    ett_da = xr.DataArray(
        ett,
        dims=('lat', 'lon'),
        coords={'lat': et1.lat, 'lon': et1.lon},
        attrs={'comment': 'Difference et1 - et2 [m2/s2]'}
    )

    ########################################

    #time
    now = datetime.now()
    dateg = now.strftime("%Y%m%d%H")   # like "202510011530"

    if bcolor:
        b1=bcolor[0]
        b2=bcolor[1]
        bn=bcolor[2]
    else: 
        b1=np.min(var[:])
        b2=np.max(var[:])
        bn=5

    levels= np.linspace(b1,b2,bn,endpoint=True)
    dco=levels[1]-levels[0]

    lats=[float(ah.LatS),float(ah.LatN),6]#float(ah.LatC)]
    lons=[float(ah.LonW),float(ah.LonE),6]#float(ah.LonC)]

    zmap=csd.zmap[cs]
    ha=GP.gethn(zmap[0],v3)
    hb=GP.gethn(zmap[1],v3)
    za=int(zmap[0])-1
    zb=int(zmap[1])-1

    wave_map = {
    'rb': 'Rossby',
    'kv': 'Kelvin',
    'mx': 'Mixed',
    'gw': 'GravW',
    'ge': 'GravE'
    }
    
    Wavea = wave_map.get(wa, 'Unknown')
    Waveb = wave_map.get(wb, 'Unknown')

    #######################################
    date_format = '%H%d%Y%b'

    # Works for int, numpy.int64, or numpy.datetime64
    date_py = pd.to_datetime(v1.time[0].values)
    datez = date_py.strftime(date_format).upper()

    tr ='Case Study:'+csst+ah.Center+'-'+trunc
    tit=datez+' Minus April Monthly Mean'

    if (caso=='ERA_5'):
        titb='Analysis: '+tit
    else:
        titb='3 Days Forecast: '+tit

    label=f"{caso} {Wavea}-{Waveb} Horizontal Energy Iteration\nClass {cs}: H{za}={ha} to H{zb}={hb}\n{titb}"

    name=f"energy_iter_c{cs}_{wa}_{wb}_anom_{area}_{caso}_{csst}_{datez}_{trunc}"

    tr='Case Study: '+csst+ah.Center+'-'+trunc  

    ct= f"Contours: {bcolor[0]} to {bcolor[1]} by {dco:.1f} {units}\n {tr}"

    ma.countour_plot(ett_da,lat=lats,lon=lons,
                    color=color,bcolor=bcolor,
                    units=units,figname=name,plotname=label ,xtitle=ct ,
                     show=show,fmt=fmt)

     
    out=SimpleNamespace(
        cs   =str(cs),
        caso =str(caso),
        epoca=str(epoca),
        csst =str(csst),
        area =str(area),
        perc =str(perc),
        xsec =str(xsec),
        cnt  =str(cnt),
        trunc=str(trunc),
        Kmax =str(Kmax),
        datei=str(csd.datei),
        datef=str(csd.datef),
        csvm =str(csd.csvm),
        prev =str(csd.prev),
        za    =str(za),
        zb    =str(zb),
        lats=lats,
        lons=lons,
        fileh=fileh,
        filea=filea,
        titb=titb,
        tit=tit
        )

    return out

def chkmdls():
    """Dummy check (replace with real one)."""
    return 0


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

