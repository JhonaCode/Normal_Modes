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
import matplotlib.pyplot as plt

#####Tenmq uye trovar ir ler diteramente
VDout ='/pesq/dados/bam/paulo.bonatti/Modal_Energetics/Version_4.0/Horizontal_Decomposition/dataout'
VMout ='/pesq/dados/bam/paulo.bonatti/Modal_Energetics/Version_4.0/Vertical_Modes/dataout'
dirv40='/home/paulo.bonatti/Modal_Energetics/Version_4.0'
fig_out   =''

def temporal(args=None):
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
        " Plots the variation in time of a ressonat triplet for case study RainRS \n\n"
        "Usage:\n"
        "temporal [caso] \n\n"
        "Default:\n"
        "Arguments meaning:\n"
        "  caso  : five letters identifying the case\n"
    ),
    formatter_class=argparse.RawTextHelpFormatter  # preserve line breaks
    )
    helped = parser.parse_args()

    # Default values
    defaults = {
        "caso" : "ERA_5",
        "csst" : "RainSS",
        "show" : True,
        "ylim" : [],
        "color": ['red','green','red'],
        "fmt"  : '%.1f',
    }

    if not args:
        return defaults

    caso  =CD.trying(args,defaults,'caso')
    csst  =CD.trying(args,defaults,'csst')
    color =CD.trying(args,defaults,'color')
    show  =CD.trying(args,defaults,'show')
    fmt   =CD.trying(args,defaults,'fmt')
    ylim  =CD.trying(args,defaults,'ylim')

    RSC='(45.8W,23.6S)'
    
    # C0_rb_C0_kv_C0_mx:
    zrb1=0
    zrb2=5
    zkv1=5
    zkv2=10
    zmx1=5
    zmx2=10

    filei='ENEC'+caso+csst+'2023'+'.ctl'

    exp_name='Temporal Triplex'
    fileg=VDout+'/'+filei
    vd = down.open_grads(fileg,exp_name)

    #print(fileg)
    #exit()
    #print(vd)
    #exit()

    if (caso=='ERA_5'):
        tit='Analysis: '
    else:
        tit='3 Days Forecast: '

    timei='00Z05FEB2023'
    timef='00Z20FEB2023'

    tim  =timei[5::]
    vrgm =450

    #lat e lon não são, são os modoss e começa do zero!
    point1  = vd.etrbasy.isel(lon=4, lat=2)
    #point1  = vd.etrbasy.sel(lon=vd.lon[5].values, lat=vd.lat[3].values)

    smrbx   = point1.isel(lev=slice(zrb1, zrb2 ))
    smrb    = smrbx.sum(dim='lev')

    point2  = vd.etgesym.isel(lon=1, lat=0)
    smkv    = point2.isel(lev=slice(zkv1, zkv2)).sum(dim='lev')
    
    total   = smrb+smkv

    title   = f"Modal Energy Class 0: {caso}-{csst} {RSC} \n {tit} From {timei} to {timef}"

    xtitle= 'Time [Days]'
    ytitle= r'Energy [m$^{2}$s$^{-2}$]'

    label   = ['Kv+Rb','Rb Asy s=4 l=4',r'Kv s=1 l=-1',r'$Mx s=1 l=-1',]

    
    figname='Energy_Triplet_Mixed_Kelvin_Rossby_'+caso+'_'+csst+'_'+tim


    fig,ax=ma.temporal_plot( 
                            data=[total,smrb,smkv],
                            #data=[smrb],
                            vmulti=[1,1,1,1],
                            color=['blue','black','red','green'],
                            label=label,ylim=ylim, dates=[timei,timef],
                            title=title,xtitle=xtitle,ytitle=ytitle,                            figname=figname,save=True,
                            show=show)

    return fig,ax 

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

