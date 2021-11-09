# This script is able to:
# 1. Create the bash script to execute the completed QE .in files

import os

# home directory
home = os.getcwd()

# get the subdirs within home 'data' directory
dirs = [i for i in os.listdir(os.path.join(home,'data'))]

with open('ScriptToExecuteCompleteQEInputFiles.sh', 'w') as file:
    file.write('#!/bin/sh \n')
    file.write(' \n')
    for d in dirs:
        new_path = os.path.join(home, 'data', d)    
        for f in os.listdir(new_path):
            fname = os.path.splitext(f)[0] 
            if '_complete' in fname:
                fullpath = os.path.join(new_path, fname)
                file.write('echo running {} \n'.format(f))
                file.write('cd {} \n'.format(new_path))
                file.write('mpirun -np 3 pw.x -in {}.in > {}.out \n'.format(fname, fname))
                file.write(' \n')
        

    
