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
VDout ='/pesq/dados/bam/paulo.bonatti/Modal_Energetics/Version_4.0/Vertical_Decomposition/dataout'
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
        "Plots the Total Energy of the Vertical Modes the Classes 0 to 4\n\n"
        "Usage:\n"
        "  totalv [ca] [ca] [atm] [caso] [epoca] [csst] [area] [perc] [xsec] [cnt]\n\n"
        "Default:\n"
        "  ca=0 ; cb=0 ; atm=ht; epoca=37 ; csst=RainRS\n"
        "  area=local ; perc=Perc ; xsec=no ; cnt=0\n\n"
        "Arguments meaning:\n"
        "  ca : vertical mode (0, 1, 2, 3 or 4) \n"
        "  cb : vertical mode (0, 1, 2, 3 or 4) \n"
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
        "ca"    :   0,
        "cb"    :   1,
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

    ca      =CD.trying(args,defaults,'ca')
    cb      =CD.trying(args,defaults,'cb')
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


    # GrADS logic: if perc != 'Perc', force Ener
    if perc != "Perc":
        perc = "Ener"

    # Print parsed values (like `say` in GrADS)
    print(f"ca={ca}, cb={cb}, atm={atm}")
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
    #*Getting dates
    #'run ../../Config/Case_Dates.gs 'caso' 'epoca' 'csst
    arg_cs={'caso'  :caso,
            'epoca' :epoca,
            'csst'  :csst,
            'dirv40':dirv40
            }

    csd=CD.csdata(arg_cs)
    ############################################################    

    za, zb = csd.zmap[ca]
    zc, zd = csd.zmap[cb]

    print("za=",za)
    print("zb=",zb)
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

    print(ah)

    ############################################################    

    xsec='yes'
    if (xsec=='yes'): 

        #Get Cross Section 
        crs=CS.get_cross_section(args={'csst':csst})
        print(crs)



    ############################################################    
    #Get Pressure Layers

    pl=PL.PressLayer(args={'dirv40':dirv40,'op':1,'atm':atm})

    pfa=pl[atm]['pk1']
    pfb=pl[atm]['pk2']

    ############################################################    

    filea='ENCL'+caso+csst+csd.datei+csd.datef+csd.prev+trunc+'.ctl'
    fileh='Vertical_Functions_'+csd.csvm+'.L0'+str(Kmax)+'.ctl'

    exp_name='Energetic_Iteraction'
    fileg=VDout+'/'+filea
    vd = down.open_grads(fileg,exp_name)

    tosum = vd.sel(lev=slice(pfa, pfb)) 
    
    exp_name='Vertical_Modes'
    fileg=VMout+'/'+fileh
    vm = down.open_grads(fileg,exp_name)

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

    if (perc == 'Perc'):
        tita    =f"Vertical Energy Interaction Percentage C{ca}_C{cb}"
        fga     ='Perc_Int'
        units   ='[%]'
        ct= f"Contours: {bcolor[0]} to {bcolor[1]} by {dco:.1f} {units}"
        suma=0
        for i in range(0,5): 
            print(f'etc{i}')
            ett          =getattr(tosum,f'etc{i}')
            vertical_sum =ett.sum(dim="lev")
            suma         =suma+vertical_sum

        et      =getattr(tosum,f'etc{ca}{cb}')
        etca    =100*et.sum(dim="lev")/suma
        #etca    =100*tosum.etc1.sum(dim="lev")/suma
    else:
        tita=f"Vertical Energy Interaction C{ca}_C{cb}"
        fga='Ener_Int'
        units='[kJ/kg]'
        ct=f"Contours: {bcolor[0]} to {bcolor[1]} by {dco:.1f} {units}"
        et=getattr(tosum,f'etc{ca}{cb}')
        etca=et.sum(dim="lev")/1000.0

    ############################################################    

    #time
    #now = datetime.now()
    #dateg = now.strftime("%Y%m%d%H")   # like "202510011530"
    #print("dateg =", dateg)
    now = datetime.now()
    dateg = now.strftime("%Y%m%d%H")   # like "202510011530"

    #date_format = '%H%d%Y%b'
    date_format = '%b%Y'
    # Works for int, numpy.int64, or numpy.datetime64
    date_py = pd.to_datetime(vd.time[0].values)
    datez = date_py.strftime(date_format).upper()

    ############################################################    
    lats=[float(ah.LatS),float(ah.LatN),6]
    lons=[float(ah.LonW),float(ah.LonE),6]


    ############################################################    
    ha=GP.gethn(za,vm)
    hb=GP.gethn(zb,vm)
    hc=GP.gethn(zc,vm)
    hd=GP.gethn(zd,vm)
    na=za-1
    nb=zb-1
    nc=zc-1
    nd=zd-1

    #dateg=vm.time[0]#.values
    #dateg = pd.to_datetime(dateg.values).strftime("%Y%m%d%H")
    #print(dateg)
    ############################################################    

    tr ='Case Study:'+csst+ah.Center+'-'+trunc
    tit='Data for '+dateg

    if csst=='RainSS' or csst=='ClimSS':
        cssts='Sao Sebastiao'

    if csst=='RainRS' or csst=='ClimRS':
        cssts='Rio Grande do Sul'

    #tr ='Case Study:'+cssts+'-'+trunc
    tr =cssts+'-'+trunc
    
    if (caso=='ERA_5'):
        titb='Analysis: '
    else:
        titb='3 Days Forecast: '

    titb  = f"Montly Mean {datez}"


    tita=f"{caso} {tita} - Levels:{pfa:.1f}-{pfb:.1f} hPa \nClass {ca}:H{na}={ha} to H{nb}={hb} Class {cb}:H{nc}={hc} to H{nd}={hd} \n {titb}"
    label=f"{fga}_C{ca}_C{cb}_Total_{area}_{atm}_{caso}_{csst}_{datez}_{trunc}"
    xlabel=f"{ct} - {tr}"


    ma.countour_plot(etca,lat=lats,lon=lons,color=color,bcolor=bcolor,units=units,figname=label,xtitle=xlabel,plotname=tita  , show=show)

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
 
