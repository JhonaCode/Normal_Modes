#####################3
import  argparse
import  subprocess
import  numpy as np
from    types import SimpleNamespace
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
        "  totalv  [wv] [cs] [caso] [epoca] [csst] [area] [perc] [xsec] [cnt]\n\n"
        "Default:\n"
        "  wv=rb; cs=0 ; caso=ERA_5 ; epoca=37 ; csst=RainRS \n"
        "  area=local ; perc=Perc ; xsec=no ; cnt=0\n\n"
        "Arguments meaning:\n"
        "  wv    : horizontal mode (rb, kv, mx, gw or ge)\n"
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
        "wv"   : 'rb',
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
    }

    """
    folders=fd.get_export_vars('../Config/Config_Dir')
    
    #get_in_file('../')
    # Now you can access the variables
    dirhome=folders["dirhome"]
    dirdata=folders["dirdata"]
    dirdinp=folders["digfggdinp"]
    """

    # If nothing passed → just return defaults
    if not args:
        return defaults

    wv   =CD.trying(args,defaults,'wv')
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


    # GrADS logic: if perc != 'Perc', force Ener
    if perc != "Perc":
        perc = "Ener"

    # Print parsed values (like `say` in GrADS)
    # Print parsed values (like `say` in GrADS)
    print('wv=',wv , 'cs=',cs ,'caso='caso, 'epoca=',epoca, 'csst=',csst, 'area=',area, 'perc=',perc, 'xsec=',xsec, 'cnt=',cnt)

    # Placeholder for chkmdls()
    rec = chkmdls()
    if rec != 0:
        return

    # Spectral/vertical resolution
    Mmax = 160
    Kmax = 37
    print(f"Mmax = {Mmax}, Kmax = {Kmax}")

    
    #*Getting dates
    #'run ../../Config/Case_Dates.gs 'caso' 'epoca' 'csst
    arg_cs={'caso':caso,
         'epoca':epoca,
         'csst':csst,
         'dirv40':dirv40
        }

    csd=CD.csdata(arg_cs)

    zca, zcb = csd.zmap[cs]
    ######################################

    rh =RB.get_Rhomb_Resol(args={'Mmax':Mmax,'resdir':1})

    trunc=rh.Rhomb+'L0'+str(Kmax)

    args_ah={'area':area,
           'Mmax':Mmax,
           'csst':csst
           }


    #Get AREA HIGHLIGHT
    ah=AH.get_area_highlight(args_ah)
    print(ah)

    xsec='yes'
    if (xsec=='yes'): 

        #Get Cross Section 
        crs=CS.get_cross_section(args={'csst':csst})
        print(crs)

    #time
    now = datetime.now()
    dateg = now.strftime("%Y%m%d%H")   # like "202510011530"
    #print("dateg =", dateg)
    ################

    tr ='Case Study:'+csst+ah.Center+'-'+trunc
    tit='Data for '+dateg
    
    if (caso=='ERA_5'):
        titb='Analysis: '#+tit
    else:
        titb='3 Days Forecast: '#+tit
    
    
    filea='ENCL'+caso+csst+csd.datei+csd.datef+csd.prev+trunc+'.ctl'
    fileh='Vertical_Functions_'+caso+'.L0'+str(Kmax)+'.ctl'

    lats=[float(ah.LatS),float(ah.LatN),6]#float(ah.LatC)]
    lons=[float(ah.LonW),float(ah.LonE),6]#float(ah.LonC)]

    exp_name='Horizontal_Decomposition'
    fileg=VDout+'/'+filea
    vd = down.open_grads(fileg,exp_name)

    #print(vd.variables)
    #exit()

    
    exp_name='Horizontal_Modes'
    fileg=VMout+'/'+fileh
    vm = down.open_grads(fileg,exp_name)

    #print(vm.variables)


    zmap=csd.zmap[cs]

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

    ha=GP.gethn(zmap[0],vm)
    hb=GP.gethn(zmap[1],vm)
    za=int(zmap[0])-1
    zb=int(zmap[1])-1

    wave_map = {
    'rb': 'Rossby',
    'kv': 'Kelvin',
    'mx': 'Mixed',
    'gw': 'GravW',
    'ge': 'GravE'
    }
    
    Wave = wave_map.get(wv, 'Unknown')

    var= getattr(vd,f"et{wv}{wv}{cs}")

    if perc=="Perc":

        fga   ='Ener_Perc'
        tita  =Wave+' Horizontal Energy Percentage'
        label =f"{caso} {tita}\n Class {cs}: H{za}={ha} to H{zb}={hb}"
        name  =f"{fga}_Class_{cs}_{Wave}_Total_{area}_{caso}_{csst}_{dateg}_{trunc}"
    
        ett=0
        for i in range(0,5):

            ets=getattr(vd,f"etnsum{i}")
            ett=ets+ett

        var=100*var/ett

        units='[%]'

        ct= f"Contours: {bcolor[0]} to {bcolor[1]} by {dco:.1f} {units}"
        
        ma.countour_plot(var,lat=lats,lon=lons,color=color,bcolor=bcolor,units=units,figname=name,plotname=label ,xtitle=ct , show=show)
        
    else:
        fga   ='Energy'
        etw   = var/1000
        tita  =Wave+' Horizontal Energy '
        label =f"{caso} {tita} \n Class {cs}: H{za}={ha} to H {zb}={hb}"
        name  =f"{fga}_Class_{cs}_{Wave}_Total_{area}_{caso}_{csst}_{dateg}_{trunc}"

        units='[kJ/kg]'

        ct= f"Contours: {bcolor[0]} to {bcolor[1]} by {dco:{fmt}} {units}"
        
        ma.countour_plot(var/1000.0,lat=lats,lon=lons,color=color,bcolor=bcolor,units=units,figname=name,plotname=label ,xtitle=ct , show=show,fmt=fmt)
        
     
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

