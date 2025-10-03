import os
import subprocess

def get_export_vars(path): 

    # Path to your env file
    env_file = path
    
    # Run bash, source the file, then print all variables
    command = f"bash -c 'source {env_file} && env'"
    
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")

    for line in proc.stdout:
        key, _, value = line.decode().partition("=")
        os.environ[key] = value.strip()
    
    proc.communicate()
    
    # Now you can access the variables
    #dirhome=os.environ["dirhome"])
    #dirdata=os.environ["dirdata"])
    #dirdinp=os.environ["dirdinp"])

    return os.environ 


def get_in_file(filepath):

    # read the file into a list of lines
    with open("filepath", "r") as f:
        lines = f.readlines()
    
    # strip newline characters
    lines = [line.strip() for line in lines]
    
    # now pick specific lines and first words
    # (Python is 0-indexed, GrADS sublin() is 1-indexed)
    diri   = lines[1].split()[0]   # line 2, first word
    dirh   = lines[1].split()[0]   # also line 2, first word (same as diri!)
    dirfig = lines[1].split()[0]   # same again
    

    return fileg 


