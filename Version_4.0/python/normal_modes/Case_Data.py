dirv40='/home/paulo.bonatti/Modal_Energetics/Version_4.0'

def csdata(args=None):
 
    if args==None:
        args=[]

    caso=int(args[0]) if len(args) > 0 and args[1] != "" else "ERA_5"
    csst=int(args[1]) if len(args) > 0 and args[3] != "" else "RainRS"
    op  =int(args[2]) if len(args) > 0 and args[2] != "" else 1

    if (op==1):
      dirg='../../Config/'
    if (op==2):
      dirg=dirv40+'/Config/'
    
    print( 'caso=',caso,'csst=',csst,'dirg=',dirg,'op =',op)
    
    #* Getting dirdinp to input the data
    filedir=dirg+'Config_Dir'

    dirdinp = find_variable_in_file(filedir,'dirdinp', nro=7, max_lines=5)

    diri=dirdinp+'/' 

    #rename the variables
    ps='pslc'
    pr='psnm'
    uv='uvel'
    vv='vvel'
    zg='zgeo'
    om='omeg'
    tp='temp'
    sh='umes'

    dirin=diri+caso+'_'+csst+'/'
    filein=caso+'_'+csst+'.ctl'
    sdf='no'
    
    if (caso == 'MONAN'):
      Idim=1440
      Jdim=721
      ko=1
      km=22
      lono=0.0
      dlon=0.25
      lato=-90.0
      dlat=0.25
      title='MONAN Pre Operational r1.3.1-rc: '+csst
    
    if (caso == 'MONOP'):
      Idim=1440
      Jdim=721
      ko=1
      km=18
      lono=0.0
      dlon=0.25
      lato=-90.0
      dlat=0.25
      title='MONAN Pre Operational r1.4.1-rc: '+csst
    
    if (caso=='BAMHY'):
      Idim=2000
      Jdim=1000
      ko=1
      km=32
      lono=0.0
      dlon=0.18
      lato=-89.91
      dlat=0.18
      title='BAMHY Hybrid Operational: '+csst
    
    if (caso == 'ERA_5'):
      Idim=1440
      Jdim=721
      ko=1
      km=37
      lono=0.0
      dlon=0.25
      lato=-90.0
      dlat=0.25
      title='ECMWF ERA 5 Reanalysis: '+csst

      if (csst=='ClimRS' or csst=='ClimSS'):
        title='ECMWF ERA 5 Climatology: '+csst

    # Path to your file
    filecsdata = './Case_Data.dgs'
    
    # Lines to write
    lines = [
        f"'{Idim}' '{Jdim}' '{ko}' '{km}' '{lono}' '{dlon}' '{lato}' '{dlat}' '{ps}' '{pr}' '{uv}' '{vv}' '{zg}' '{om}' '{tp}' '{sh}' '{sdf}'",
        f"'{dirin}'",
        f"'{filein}'",
        f"'{title}'"
    ]
    
    # Write lines to the file
    with open(filecsdata, 'w') as f:
        for line in lines:
            f.write(line + '\n')
        
    return

def find_variable_in_file(filepath, var_name, nro=7, max_lines=5):
    """
    Search for a variable name in the first `nro` characters of each line after '',
    checking up to `max_lines` lines in the file.

    Args:
        filepath (str): Path to the file to search.
        var_name (str): Variable name to find (e.g., 'dirdinp').
        nro (int): Number of characters to consider from each line.
        max_lines (int): Maximum number of lines to check from the top.

    Returns:
        str or None: The full line containing the variable, or None if not found.
    """
    with open(filepath, 'r') as f:
        for i, line in enumerate(f):
            if i >= max_lines:
                break
            snippet = line[:]
            words = snippet.split()
            if len(words) >= 2 and words[1][0:nro] == var_name:
                return f'{words[1][nro+1::]}'#line.strip()
    return None 

# Example usage
if __name__ == "__main__":
    # Simulating: totalv 2 MYCAS 40 MyCase global Ener yes 5
    csdata()





