#####################3
import  argparse
import  subprocess
from    types import SimpleNamespace
#to get time
from    datetime import datetime
# Function with the definition of differents projetions
import   sources.cartopyplot   as ma 
import  grads.data_own   as down
#####################3
import normal_modes.get_folder     as fd
import normal_modes.Case_Dates     as CD
import normal_modes.Rhomb_Resol    as RB
import normal_modes.Area_Highlight as AH
import normal_modes.Cross_Section  as CS

#####Tenmq uye trovar ir ler diteramente
VDout ='/pesq/dados/bam/paulo.bonatti/Modal_Energetics/Version_4.0/Vertical_Decomposition/dataout'
VMout ='/pesq/dados/bam/paulo.bonatti/Modal_Energetics/Version_4.0/Vertical_Modes/dataout'
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
        "Plots the Total Energy of the Vertical Modes the Classes 0 to 4\n\n"
        "Usage:\n"
        "  totalv [cs] [caso] [epoca] [csst] [area] [perc] [xsec] [cnt]\n\n"
        "Default:\n"
        "  cs=0 ; caso=ERA_5 ; epoca=37 ; csst=RainRS\n"
        "  area=local ; perc=Perc ; xsec=no ; cnt=0\n\n"
        "Arguments meaning:\n"
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


    # GrADS logic: if perc != 'Perc', force Ener
    if perc != "Perc":
        perc = "Ener"

    # Print parsed values (like `say` in GrADS)
    print(cs, caso, epoca, csst, area, perc, xsec, cnt)

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
         'csst':csst
        }

    csd=CD.csdata(arg_cs)

    if cs == 0:
        csd.zca, csd.zcb = csd.z0a, csd.z0b
    elif cs == 1:
        csd.zca, csd.zcb = csd.z1a, csd.z1b
    elif cs == 2:
        csd.zca, csd.zcb = csd.z2a, csd.z2b
    elif cs == 3:
        csd.zca, csd.zcb = csd.z3a, csd.z3b
    elif cs == 4:
        csd.zca, csd.zcb = csd.z4a, csd.z4b
    else:
        raise ValueError(f"Invalid cs index: {cs}")


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
    
    filea='ENEC'+caso+csst+csd.datei+csd.datef+csd.prev+trunc+'.ctl'
    fileh='Vertical_Functions_'+caso+'.L0'+str(Kmax)+'.ctl'

    lats=[float(ah.LatS),float(ah.LatN),6]#float(ah.LatC)]
    lons=[float(ah.LonW),float(ah.LonE),6]#float(ah.LonC)]

    exp_name='Vertical_Decomposition'
    fileg=VDout+'/'+filea
    vd = down.open_grads(fileg,exp_name)
    
    exp_name='Vertical_Modes'
    fileg=VMout+'/'+fileh
    vm = down.open_grads(fileg,exp_name)

    ha=gethn(csd.zca,vm)
    hb=gethn(csd.zcb,vm)
    za=int(csd.zca)-1
    zb=int(csd.zcb)-1
  
    var=getattr(vd,f"etn{cs}")

    if perc=="Perc":

        fga   ='Ener_Perc'
        var   = var/vd.ett*100
        tita  ='Vertical Energy Percentage'
        label =f"{caso} {tita}\n {titb} \n Class {cs}: H{za}={ha} to H {zb}={hb}"
        name  =f"{fga}_Class_{cs}_Total_{area}_{caso}_{csst}_{dateg}_{trunc}"
        
        ma.cartopy_plot(var,lat=lats,lon=lons,color=color,bcolor=bcolor,units='[%]',figname=name,plotname=label  , show=show)
        
    else:
        fga   ='Ener'
        var   = var/1000
        tita  ='Vertical Energy'
        label =f"{caso} {tita}\n {titb} \n Class {cs}: H{za}={ha} to H {zb}={hb}"
        name  =f"{fga}_Class_{cs}_Total_{area}_{caso}_{csst}_{dateg}_{trunc}"
        
        ma.cartopy_plot(var,lat=lats,lon=lons,color=color,bcolor=bcolor,units='[kJ/kg]',figname=name,plotname=label  , show=show)

     
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
        #zca  =str(csd.zca),
        #zcb  =str(csd.zcb),
        za    =str(za),
        zb    =str(zb),
        #Center=str(ah.Center),
        #LonW  =str(ah.LonW),
        #LonE  =str(ah.LonE),
        #LatN  =str(ah.LatN),
        #LatS  =str(ah.LatS),
        lats=lats,
        lons=lons,
        fileh=fileh,
        filea=filea,
        titb=titb,
        tit=tit
        )

    #return {
    #    "cs": cs,
    #    "caso": caso,
    #    "epoca": epoca,
    #    "csst": csst,
    #    "area": area,
    #    "perc": perc,
    #    "xsec": xsec,
    #    "cnt": cnt,
    #}
    return out

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

