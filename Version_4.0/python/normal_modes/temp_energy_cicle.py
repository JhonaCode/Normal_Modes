#####################3
import  argparse
import  subprocess
import  numpy as np
from    types import SimpleNamespace
#to get time
from    datetime import datetime
import  pandas as pd
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
VDout ='/pesq/dados/bam/paulo.bonatti/Modal_Energetics/Version_4.0/Regional_Energy_Cycle/dataout'
dirv40='/home/paulo.bonatti/Modal_Energetics/Version_4.0'


def temporal_plot(args=None):
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
        "temporal {caso: ,csst: }\n\n"
        "Default:\n"
        "Arguments meaning:\n"
        "  caso  : five letters identifying the case\n"
    ),
    formatter_class=argparse.RawTextHelpFormatter  # preserve line breaks
    )
    helped = parser.parse_args()

    # Default values
    defaults = {
        "caso"   : ["ERA_5"],
        "csst"   : "RainSS",
        "var"    : 'Aem',
        "dates"  : None,
        "label"  : ['',''],
        "xtitle" : [],
        "ytitle" : [],
        "title"  : [],
        "figname": [],
        "show"   : True,
        "ylim"   : [],
        "color"  : ['red','green','red'],
        "fmt"    : '%.1f',
        "vmulti" : [1,1],
        "color"  : ['blue','red'],
        "save"   : True,
    }

    if not args:
        return defaults

    caso   =CD.trying(args,defaults,'caso')
    csst   =CD.trying(args,defaults,'csst')
    var    =CD.trying(args,defaults,'var')
    dates  =CD.trying(args,defaults,'dates')
    label  =CD.trying(args,defaults,'label')
    xtitle =CD.trying(args,defaults,'xtitle')
    ytitle =CD.trying(args,defaults,'ytitle')
    title  =CD.trying(args,defaults,'title')
    figname=CD.trying(args,defaults,'figname')
    color  =CD.trying(args,defaults,'color')
    show   =CD.trying(args,defaults,'show')
    fmt    =CD.trying(args,defaults,'fmt')
    ylim   =CD.trying(args,defaults,'ylim')
    vmulti =CD.trying(args,defaults,'vmulti')
    color  =CD.trying(args,defaults,'color')
    save   =CD.trying(args,defaults,'save')

    # Spectral/vertical resolution
    Mmax = 160
    Kmax = 37
    print(f"Mmax = {Mmax}, Kmax = {Kmax}")


    ########################################
    epoca=1
    arg_cs={'caso':caso[0],
         'epoca':epoca,
         'csst':csst,
         'dirv40':dirv40
        }

    csd1=CD.csdata(arg_cs)

    if len(caso)>1:

        epoca=1
        arg_cs={'caso':caso[1],
             'epoca':epoca,
             'csst':csst,
             'dirv40':dirv40
            }

        csd2=CD.csdata(arg_cs)

    ######################################

    datei=csd1.datei
    datef=csd1.datef

    date_format = '%Y%m%d%H'
    # Works for int, numpy.int64, or numpy.datetime64
    date_py =  datetime.strptime(datef,date_format)
    date2_format = '%b%Y'
    date2   =  date_py.strftime(date2_format).upper()

    filei=f"{caso[0]}_{csst}_Reg_Ener_{date2}.ctl"

    exp_name=''
    fileg=VDout+'/'+filei
    v1 = down.open_grads(fileg,exp_name)

    toplot1=getattr(v1,var)

    if len(caso)>1:

        filei=f"{caso[1]}_{csst}_Reg_Ener_{date2}.ctl"

        exp_name=''
        fileg=VDout+'/'+filei
        v2 = down.open_grads(fileg,exp_name)

        toplot2=getattr(v2,var)

    #print(toplot.time)
    #print(v2.variables)
    #exit()

    if dates==None:

        if (csst=='RainRS'):
            ta='00Z23APR2024'
            tb='00Z04MAY2024'
        else:
            ta='00Z05FEB2023'
            tb='00Z21FEB2023'

        dates=[ta,tb]


    try:
        figname=figname+'_'+caso[0]+'_'+caso[1]+'_'+csst
        data=[toplot1,toplot2]
        label=[caso[0],caso[1]]
    except:
        figname=figname+'_'+caso[0]+'_'+csst
        data=[toplot1]

    fig,ax=ma.temporal_plot(data=data,
                            vmulti=vmulti,
                            color=color,
                            title=title,
                            label=label,
                            ylim=ylim,
                            dates=dates,
                            xtitle=xtitle,ytitle=ytitle,     
                            figname=figname,save=save,
                            show=show)



    return fig,ax 
