# This script is able to:
# 1. 

import os
import numpy as np

# home directory
home = '/home/user/Desktop/CompMatPhys/TeO2/data'

# get the dirs within home
dirs = [i for i in os.listdir(home)]

# define the initial parameters
ecutwfc = str(50)
ecutrho = str(330)
kpoints = ['  3 3 3 0 0 0 \n']

# function to complete the QE .in files
def complete_QE(filename, ecutwfc, ecutrho):
    '''
    This function completes the quantum espresso input files
    
    '''
    if os.path.splitext(filename)[1] != '.in':
        pass
    else:
        #if 'TeO2.in' in filename:
        with open(filename,'r') as file:
            filename = os.path.splitext(filename)[0]
            contents = file.readlines()    
        contents.insert(8, "&CONTROL \n")
        contents.insert(9, "  calculation='scf', \n")
        contents.insert(10, "  outdir='.', \n")
        contents.insert(11, "  prefix='{}', \n".format(filename))
        contents.insert(12, "  pseudo_dir='/home/user/Desktop/QE/PSEUDOS_TeO2', \n")
        contents.insert(13, "  verbosity='low', \n")
        contents.insert(14, "  tprnfor=.true., \n")
        contents.insert(15, "  tstress=.true., \n")
        contents.insert(16, "/ \n")
        contents.insert(23, "  ecutwfc={}, \n".format(ecutwfc))
        contents.insert(24, "  ecutrho={}, \n".format(ecutrho))
        contents.insert(25, "  input_dft='pbe', \n")
        contents.insert(26, "  occupations='smearing', \n")
        contents.insert(27, "  smearing='mv', \n")
        contents.insert(28, "  degauss=0.005d0, \n")
        contents.insert(29, "/ \n")
        contents.insert(30, "&ELECTRONS \n")
        contents.insert(31, "  conv_thr=1d-08, \n")
        contents.insert(32, "  mixing_beta=0.7d0, \n")
        contents.insert(33, "/ \n")
        contents.insert(len(contents) + 1, "K_POINTS {automatic} \n")
        contents.insert(len(contents) + 1, "{}".format(kpoints[0]))  

        for i in range(len(contents)):
            if 'Te_PSEUDO' in contents[i]:                
                pseudo_name = 'Te.pbe-n-kjpaw_psl.1.0.0.UPF'
                x = contents[i].index('Te_PSEUDO')
                new_line = contents[i][:x] + pseudo_name + '\n'
                contents[i] = new_line            

            if 'O_PSEUDO' in contents[i][-10:-1]:        
                pseudo_name = 'O.pbe-n-kjpaw_psl.1.0.0.UPF'
                new_line = contents[i][:-10] + pseudo_name + '\n'
                contents[i] = new_line

        with open("{}_complete.in".format(filename), "w") as f:
            contents = "".join(contents)
            f.write(contents)

# execute
for d in dirs:
    new_path = os.path.join(home,d)
    os.chdir(new_path)
    for file in os.listdir(new_path):
        if os.path.splitext(file)[1] == '.in' and '_complete' not in file:
            complete_QE(file, ecutwfc, ecutrho)

