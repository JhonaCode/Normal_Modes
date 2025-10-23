#####################3
import  argparse
import  subprocess
import  numpy as np
import  pandas as pd
import  xarray as xr
import  matplotlib.pyplot as plt
from    types import SimpleNamespace

#to get time
from    datetime import datetime
import datetime as dt
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
        "  profile  { [caso:,caso:],\n epoca:,\n csst:,\n area:, \n  latp:}\n\n"
        "Default:\n"
        "  caso=ERA_5 ; epoca=37 ; csst=RainRS \n"
        "  area=local ; perc=Perc ; xsec=no ; cnt=0\n\n"
        "Arguments meaning:\n"
        "  caso  : five letters identifying the case\n"
        "  epoca : number identifying the datei and datef\n"
        "  csst  : six letters identifying the case study\n"
        "  latp  :  latitude of the vertical profile\n"
    ),
    formatter_class=argparse.RawTextHelpFormatter  # preserve line breaks
    )
    helped = parser.parse_args()

    # Default values
    defaults = {
        "caso" : ["ERA_5"],
        "epoca": [37],
        "csst" : "RainRS",
        "title": "",
        "ytitle":[],
        "var"  : "Qr",
        "varmulti"  : [1],
        "date" : [],
        "color": ['blue'],
        "show" : True,
        "vmulti": 1,
        "latp" : -27,
        "ylim" : [],
        "fmt"  : '.1f',
        "units": '',
        "save": False,
    }


    # If nothing passed → just return defaults
    if not args:
        return defaults

    caso  =CD.trying(args,defaults,'caso')
    epoca =CD.trying(args,defaults,'epoca')
    csst  =CD.trying(args,defaults,'csst')
    title =CD.trying(args,defaults,'title')
    ytitle=CD.trying(args,defaults,'ytitle')
    latp  =CD.trying(args,defaults,'latp')
    color =CD.trying(args,defaults,'color')
    ylim  =CD.trying(args,defaults,'ylim')
    show  =CD.trying(args,defaults,'show')
    fmt   =CD.trying(args,defaults,'fmt')
    units =CD.trying(args,defaults,'units')
    vmulti=CD.trying(args,defaults,'vmulti')
    var   =CD.trying(args,defaults,'var')
    vmulti=CD.trying(args,defaults,'vmulti')
    date  =CD.trying(args,defaults,'date')
    save  =CD.trying(args,defaults,'save')


    print('caso=',caso, 'epoca=',epoca, 'csst=',csst)

    # Placeholder for chkmdls()
    rec = chkmdls()
    if rec != 0:
        return

    # Spectral/vertical resolution
    Mmax = 160
    Kmax = 37
    print(f"Mmax = {Mmax}, Kmax = {Kmax}")
    
    ########################################

    csd_array=[]
    datetp=[]

    clm=csst[0:4]

    for i in range(0,len(caso)):

        arg_cs={'caso':caso[i],
             'epoca':epoca[i],
             'csst':csst,
             'dirv40':dirv40
            }

        cs_l=CD.csdata(arg_cs)
        csd_array.append(cs_l)
        
        date1_format = '%Y-%m-%dT%H:00'
        date2_format = '%Y%m%d%H'
        date3_format = '%b%Y'

        if date==[]:

            datei= csd_array[i].datei
            datef= csd_array[i].datef

            date_py =  datetime.strptime(datef,date2_format)
            
            if clm == 'Clim': 
                date_py=date_py - dt.timedelta(days=30) 

            date2   =  date_py.strftime(date3_format).upper()
            dateii  =  date_py.strftime(date1_format).upper()
            datetp.append(dateii)

                             
        else:
            date_py =  datetime.strptime(date ,date1_format)

            if clm == 'Clim': 
                date_py=date_py - dt.timedelta(days=30) 

            date2   =  date_py.strftime(date3_format).upper()
            datetp.append(date)
    ########################################


        
    latpf=np.abs(latp)

    #filei=f"{caso[0]}_{csst}_Qy_{date2}.ctl"
    #exp_name=''
    ##fileg=VDout+'/'+filei
    #print(VDout)
    #fileg=filei
    #vtp1 = down.open_grads(fileg,exp_name)
    #v1   =getattr(vtp1,var)
    #print(datetp)
    #exit()

    toplot=[]
    datetp=[]
    fn=''
    for i in range(0,len(caso)):

        filei=f"{caso[i]}_{csst}_Qy_{date2}.ctl"

        exp_name=''
        #fileg=VDout+'/'+filei
        fileg=filei
        vtp=down.open_grads(fileg,exp_name)
        toplot.append(getattr(vtp,var))

        if clm == 'Clim': 
            date2   =  (toplot[i].time[0].values).astype('datetime64[ms]').astype(dt.datetime)
            datetp.append(date2.strftime(date1_format))

        fn=fn+"_"+caso[i]

    figname=f"Profile_{var}{fn}_{csst}_{datetp[0]}_lat_{latpf}S"

    title=title
    xtitle=r'$\dfrac{\alpha}{\Omega}\left(\dfrac{\partial q}{\partial \phi }\right)$'
    #ytitle='Pressure [hPa]'
    ytitle=ytitle

    fig,ax=ma.profile_plot(data=toplot,
                            vmulti=vmulti,
                            color=color,
                            title=title,
                            label=caso,
                            lat=latp,
                            ylim=ylim,
                            date_str=datetp,
                            xtitle=xtitle,ytitle=ytitle,
                            figname=figname,
                            save=save,
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

