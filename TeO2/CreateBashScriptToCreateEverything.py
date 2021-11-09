# This script is able to?
# 1 - get the lattice param from the originial CIF file
# 2 - Create diff Cif files with diff lat param
# 3 - Convert the CIF files into QE input files

import os
#import subprocess as sb

home = os.getcwd()

with open('ScriptToCreateEverything.sh', 'w') as file:
    file.write('#!/bin/sh \n')
    file.write(' \n')
    # create the "data" directory
    file.write('# create the "data" directory \n')
    file.write(' python3 CreateDataDirectory.py \n')
    file.write(' \n')  
    file.write('# get the lattice parameter from the CIF file \n')
    # Get lattice parameters from the original CIF file
    file.write('python3 GetLatticeParametersFromCIFfile.py \n')
    file.write(' \n')
    # Create subdirectories for each lat param
    file.write(' # Create subdirectories for each lat param \n')
    file.write('python3 CreateSubdirectories.py \n')
    file.write(' \n')   
    # Create diff CIF files for each reduced volume
    file.write('# from the initial CIF file \n')
    file.write('# create a series of CIF files varying the \n')
    file.write('# lattice parameter \n')    
    file.write('python3 CreateCIFfilesForDifferentLatticeParams.py \n')
    file.write(' \n')
    # Convert them into QE input files
    file.write('# Convert all CIF files into QE input files \n')   
    file.write('python3 ConvertCIFToQEIn.py \n')
    file.write(' \n')
    # Complete the QE input files
    file.write('# Now we need to complete the QE input files \n')  
    file.write('python3 CompleteQEInputFilesForTeO2Optimization.py \n')
    file.write(' \n')

# Execute the just created bash script
#sb.Popen('bash ScriptToCreateEverything.sh ', shell = True)
    
