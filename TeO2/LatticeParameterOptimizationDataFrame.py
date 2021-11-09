# This script is able to:
# 1. Open the QE .out files
# 2. Get the energy and volume
# 3. Save the energy and volume values in a CSV file

import os
import numpy as np 

home = '/home/user/Desktop/CompMatPhys/TeO2/data'

# ge the subdirs within 'data directory'
dirs = [i for i in os.listdir(home)]

# empty lists to store the data
vols_A, vols_UA, Es, Lat_UA, Lat_A = [], [], [], [], []

for d in dirs:
    new_path = os.path.join(home,d)
    for file in os.listdir(new_path):
        if os.path.splitext(file)[1] == '.out':        
            parts = os.path.splitext(file)[0].split('_')            
            # lat param in angstrom
            if parts[1] == 'complete':
                pass
            else:
                lat_p_angs = float(parts[1])
            Lat_A.append(lat_p_angs)
            vol_ang3 = 1.5345723*lat_p_angs**3
            vols_A.append(vol_ang3)            
            # lat param in                 
            lat_p_ua = 1.889*lat_p_angs
            Lat_UA.append(lat_p_ua)
            vol_ua3 = 1.5345723*lat_p_ua**3
            vols_UA.append(vol_ua3)            
            # Energy
            filepath = os.path.join(new_path,file)
            with open(filepath, 'r') as data:
                content = data.readlines()
            for line in content:
                if '! ' in line:
                    parts = line.split(' ')
                    E = float(parts[-2])
                    Es.append(E)  
            #print(lat_p_angs, vol_ang3, E)


csv_file = ['Lat. Par. (ua), Lat. Par (A), Vol (ua3), Vol (A3), Energy (Ry)']

with open('/home/user/Desktop/CompMatPhys/TeO2/LatticeParameterOptimization.csv', 'w') as out:
    out.write('Lat.Par.(ua),Lat.Par(A),Vol(ua3),Vol(A3),Energy(Ry)\n')
    for i in range(len(Es)):
        out.write('{},{},{},{},{} \n'.format(Lat_UA[i], Lat_A[i], vols_UA[i], vols_A[i], Es[i]))
