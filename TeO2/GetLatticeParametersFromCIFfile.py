# This script is able to?
# 1. Access the original CIF file
# 2. Get the originial values for the lat param
# 3. Calculate the original volume
# 4. Calculate the volume reductions
# 5. Calculate the lat params for each reduced volume
# 6. Save everything in a .csv file called 'vol_vs_alats.csv'

import numpy as np
import os

home = os.getcwd()

for file in os.listdir(home):
    if os.path.splitext(file)[1] == '.cif':
        with open(os.path.join(home,file),'r') as cif:
            content = cif.readlines()
            for line in content:
                if '_cell_length_a' in line:
                    a = float(line.split('   ')[1])            
                if '_cell_length_b' in line:
                    b = float(line.split('   ')[1])
                if '_cell_length_c' in line:
                    c = float(line.split('   ')[1])
       
# calculate the volume
def vol(a):
    v = a*b*c
    return v

# Initial volume (i.e., volume calculated using the
# lattice parameter a frmo the CIF file
V0 = vol(a)

# percentage of reduction of volume
perc = [1.0, 0.95, 0.90, 0.85, 0.80]
vol_perc = [V0*i for i in perc]

# a function to calculate the lat par from a given volume
# for TeO2, a = b and c = 1.5345723 
def alat(vol):
    alat = (vol / 1.5345723)**(1/3)
    return alat

# lattice parameters (in angstrom)
alats = [alat(i) for i in vol_perc]

# calculate b and c from a
b = [i for i in alats]
c = [1.5345723*i for i in alats]  

# save the lat params in a csv file
with open('/home/user/Desktop/CompMatPhys/TeO2/vol_vs_alats.csv', 'w') as file:
    file.write('VolumeReduction(%),Volume(A^{3}),a(A),b(A),c(A) \n')
    for i in range(len(alats)):
        file.write('{},{},{},{},{}\n'.format(perc[i],vol_perc[i],alats[i],b[i],c[i]))

