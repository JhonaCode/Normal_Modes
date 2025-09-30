
The reference directory is 
    dirhome=${sdirhome}/Modal_Energetics/Version_4.0
    dirdata=${sdirdata}/Modal_Energetics/Version_4.0
    where sdirhome is in general /home/user/
The directory ${dirhome} is defined in the directory ./Config
Read the CFG_ksh_Readme.txt inside this directory and edit 
./Config/Config_Dir to define your own ${dirhome} and ${dirdata}
Note that the directory ${sdirhome} must be the one you install
the directory Modal_Energetics/. If not, you must to move
the directory Modal_Energetics/* to your ${sdirhome}
All changes you need to do are at the files inside ./Config
See the *_Readme.txt inside directory ./Config
Note: Inside ./Config/Config_Dir there also three numeric 
      variables nchdird, nchsdr1 and nchsdr2: it reffers to
      the length of parts of ${dirdata}. Suppose that
      dirata=/disk/data/user/Modal_Energetics/Version_4.0
      Then 
      nchdird=16, that is the length of /disk/data/user/
      nchsdr1=17, that is the length of Modal_Energetics/
      nchsdr2=11, that is the length of Version_4.0
      This is necessary to the korn shell script 
      ./Make_Dir_Data inside ./Config make the data outuput
      subdirectories at the correct place you choose.
      
      The directory dirdinp is the main directory where your 
      data is located.

In the following items there is a guide to compute the
modal energetics, Eliassen-Palm Flux and Regional Energy Cyle.

After read these clues go to ./Config and see the *_Readme.txt
and make the changes you want for your own use.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Change the grads local in Config/Case_Data.gs:
****dirv40='/home/paulo.bonatti/Modal_Energetics/Version_4.0'
dirv40='/home/jhonatan.aguirre/Modal_Energetics/Version_4.0'

1 - The directory ./Pressure_Levels has the files with the
    pressure levels data for the reference case cvsm. The 
    name of the file is:
    PressureLevels_csvm.Lkkk
    where csvm is a identifier for the case (ERA_5) with five letters,
    defined at i${dirhome}/Config/Reference_Case and kkk is a
    three digit number of levels (Kmax), e.g. if Kmax=37, kkk=037
    These data contains mean surface pressure and pressure levels
    from surface to top.
    ERA_5 is selected as the reference case.

2 - Before run any script, go to the subdirectories source and
    do make to generate the executable binary file for all of them.
    Take care, if you run any script without argumentsi pr -h, 
    they will be run for the default case.

3 - The first program to run is to generate the vertical modes
    for each case you will analyse, to perform the vertical
    decomposition. To do that use go to directory ./Vertical_Modes/source
    and do make and then cd ../run and run
    ./Run_VModes
    Run_VModes has no arguments and uses the reference case to
    generated the vertical modes.
    Run ./Run_VModes -h for extra tips.

4 - If you want to classify the vertical modes into classes,
    and get predefined vertical pressure layers go to directory
    ./Get_Cls_Prs_Lay/source and do make and then cd ../run and run
    ./Run_GClsPrs
    and the result will be at ./Get_Cls_Prs_Lay/txt
    Run_VModes has no arguments and uses the reference case to
    get pressure layers and vertical modes distribution by classes.
    Run ./Run_GClsPrs -h for extra tips.

5 - Now it is necessary to generate the horizontal resolution.
    Go to the directory ./Get_Rhomb_Res_GLats/run and run
    ./Run_GRhoResGL Mmax 0
    where Mmax is the number of zonal waves (Rhomb+1)
    See GRG_Readme.txt inside the directory ./Get_Rhomb_Res_GLats
    or do ./Run_GRhoResGL -h for further details.
    Mmax must be 160, but if you want plot the Hough Functions,
    ++
    you must run ./Run_GRhoResGL 32 0, because the GrADS scripts
    ++
    you must run ./Run_GRhoResGL 31 0, because the GrADS scripts
    to do that plot use the this resolution for the quasi-Mercator
    grid. There is a korn shell script (Run_GRhoResGL_All) to do
    all the necessary files.

5 - The next step is to genetared the horizontal modes 
    (Hough functions), to perform the horizontal decomposition.
    To do that go to directory Hough_Functions/run and run
    ./Run_Hough nhn Mmax
    at the directory Hough_Functions, for nhn = 1, to Kmax
    Mmax refers to the selected quadratic Rhomboidal grid,
    it is Rhomb+1 and represents the number of zonal waves
    including the zonal mean (+1).
    ./Run_Hough uses the reference case to generate the Hough 
    Functions.
    Run ./Run_Hough -h for description of the arguments.
    There is a script ./Run_Hough_All that generates all
    the Hough Functions files.

6 - You can generate the files of dates used for all the
    processes (Dates_caso_csst.dgs) at the directory Get_Dates. 
    Go to Get_Dates/run and run
    ./Run_Dates caso csst datei datef dh Nmax
    Run ./Run_Dates -h for description of the arguments.

7 - Then, to generate the inital condition for modal energy
    analysis has 3 steps:
    a) go to ./Data_Pressure and open GrADS with the comand
       grads. Then run the GrADS script:
       Get_Data caso epoca csst
       This will generate the initial data as 5 netcdf files 
       (zonal wind, meridional wind, temperature, specific
       humidity and geopotential height)
       Run GetData -h inside grads command for description 
       of the arguments.
    b) go to directory ./Get_Netcdf/source inside ./Data_Pressure
       and do make, then cd ../run and run:
       ./Run_Netcdf caso epoca csst DelFileInp
       A single binary file with the variables zonal wind, 
       meridional wind, temperature, specific humidity and
       geopotential height will be generated.
       Run ./Run_Netcdf -h for description of the arguments.
    c) go to directory ./Get_ENER_UVZ/source inside ./Data_Pressure 
       and do make, then cd ../run and run:
       ./Run_GEUVZ CasoInp KmaxInp epoca csst DelFileInp MmaxOut GrdInp CasoClm 
       Then a quadratic gaussian Rhomboidal grid RB(MmaxOut-1) in a
       GrADS sequential format data file with  zonal wind, meridional wind
       and geopotential height will be generated to be read by the program 
       that performs the vertical decomposition.
       Run ./Run_GEUVZ -h for description of the arguments.
       The layout of the initial data for is a file in REAL(KIND=4)
       with sequential records and in a selected horizontal Rhomboidal grid,
       with Kmax pressure levels from the reference case (the first 1000 hPa):
       zonal wind (m/s) for each layer as record (Kmax records)
       meridional wind (m/s) for each layer as record (Kmax records)
       geopotential height (m) for each layer as record (Kmax records)
       You can geneterate the initial data with this layout using
       another procedure than GrADS.
       Vertical interpolation to the reference case is done in this 
       procedure, then all cases has the same vertical modes as the
       reference case and the same vertical distribution by vertical classes.

8 - You can do now the Eliassen-Palm Flux because you only need the 
    initial files to do that, for the desided date.
    Go to the directory Eliassen_Palm_Flux/run and run
    ./Run_EPF caso epoca csst norm
    Run ./Run_EPF -h for description of the arguments.

9 - You can also do now the Regional Energy Cycle but in that case you need
    at least 3 consecutive dates with the same time interval as initial files.
    It is included in this procedure the calculation of the Rayleigh necessary
    condition for barotropic and baroclinic instabilities.
    Go to the directory Regional_Energy_Cycle/run and run
    ./Run_RegEner caso] csst Flux EnTu PTop
    Run ./Run_Reg_Ener -h for description of the arguments.

10 - Now the modal decomposition will begin. Go to the directory
     ./Vertical_Decomposition/run and run
     ./Run_VDecomp caso epoca csst
     to perform the vertical modal decomposition.
     Run ./Run_VDecomp -h for description of the arguments.

11 - To perform the horizontal modal decomposition go to the
     directory ./Horizontal_Decomposition/run and run
     ./Run_HDecomp caso epoca csst
     Run ./Run_HDecomp -h for description of the arguments.

12 - To perform the calculation of the interaction among
     horizontal and vertical modes go to the directory
     ./Interaction_Horizontal_Vertical/run and run
     ./Run_IntHV caso epoca csst
     Run ./Run_IntHV -h for description of the arguments.

13 - To perform the horizontal modal recomposition for a
     range of zonal wave numbers and a range of vertical
     modes go to the directory ./Hor_Ver_Recomposition/run 
     and run
     ./Run_HVRec caso epoca csst Si Sf Ni Nf HorOut VerOut
     Run ./Run_HVRec -h for description of the arguments.

14 - Finally you can plot figures using GrADS scripts
     (name.gs)
     at the directories
     ./Vertical_Modes/gs
     ./Hough_Functions/gs
     ./Vertical_Decomposition/gs
     ./Horizontal_Decomposition/gs
     ./Interaction_Horizontal_Vertical/gs
     ./Hor_Ver_Recomposition/gs
     ./Obs_gs
     and see the scripts inside these directories because
     they have instruction how to run them.
     We can design your own GrADS scripts.
     To see the usage of the available GrADS script type
     name.gs -h
     inside GrADS application (grads) and it will be 
     displayed the arguments and their default values.
     Before run the GrADS scripts it is necessary to run
     the korn shell script ./Create_gs_dir_cfg inside 
     ./Config to create a file (dir.cfg) with the data 
     input directories and directory for the figures.

15 - As pointed out at the beginning before run the ksh scripts 
     it is necessary to compile the sources which are in FORTRAN 90. 
     Then, go to the subdirectory source and execute the make.
     There are two options for compilers (See FTN.Comp_Readme.txt
     at the directory ./Config)
     a) The compiler GNU gfortran
        it is necessary to do 
        module load gnu9
        module load openmpi4/4.1.1
        at egeon. 
     b) The compiler intel ifort
        it is necessary to do
        module unload gnu9
        module unload openmpi4/4.1.1
        module load intel/2022.1.0
        module load mpi/2021.5.1
        at egeon.
        If you want to change the FORTRAN compiler,
        you need to to that changing the file FTN_Compiler
        at ./Config
        and load de corresponding module (if necessary).
        It is necessary to load the module nco-5.0.1-gcc-11.2.0-u37c3hb
        at egeon to treat the netcdf files generate by GrADS script 
        GetData.gs that uses the application ncks from nco.

     c) To use grads that opens netcdf files used at egeon:
        module load opengrads/2.2.1
        export GASCRP=/home/ioper/bin/opengrads-2.2.1.oga.1/Contents/Resources/Scripts
        export GADDIR=/home/ioper/bin/opengrads-2.2.1.oga.1/Contents/Resources/SupportData

     d) The commands module (a, b and c) and export (c) must be
        included at the file .bashrc at your ${HOME}.

     e) At the directory ./pdf there is a pdf file describing all the theory 
        envolved in this system of energetics analysis, the Eliassen-Palm Flux, 
        the regional energy cycle and the Rayleigh necessary condition (in portuguese):
        Normal_Modes_Decomposition_Energetics_Interaction_EPF_REG_Qy_Theory.pdf

     f) Take care, if you run these korn shell scripts without arguments,
        it will be runned for the default case
