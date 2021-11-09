# This script is able to:
# 1. 

import os

home = '/home/user/Desktop/CompMatPhys/TeO2'

# define the function that generate the CIF files
def generate_cif_files(alats, be, ce):
    for i in range(len(be)):
        path = os.path.join(home,'data','TeO2_{}'.format("%.6f" % alats[i]))
        filename = os.path.join(path,'TeO2_{}.cif'.format("%.6f" % alats[i]))        
        with open(filename,'w') as file:
            file.write('data_TeO2 \n')
            file.write("_symmetry_space_group_name_H-M   'P 1' \n")
            a = alats[i]
            file.write('_cell_length_a   {} \n'.format("%.6f" % a))
            b = be[i]
            file.write('_cell_length_b   {} \n'.format("%.6f" % b))
            c = ce[i]
            file.write('_cell_length_c   {} \n'.format("%.6f" % c))
            file.write('_cell_angle_alpha   90 \n')
            file.write('_cell_angle_beta   90 \n')
            file.write('_cell_angle_gamma   90 \n')            
            file.write('_symmetry_Int_Tables_number   1 \n')
            file.write('_chemical_formula_structural   TeO2 \n')
            file.write("_chemical_formula_sum   'Te4 O8' \n")
            file.write('_cell_volume   188.09425793 \n')
            file.write('_cell_formula_units_Z   4 \n')
            file.write('loop_ \n')
            file.write('_symmetry_equiv_pos_site_id \n')
            file.write('_symmetry_equiv_pos_as_xyz \n')
            file.write(" 1 'x,y,z' \n")
            file.write('loop_ \n')
            file.write('_atom_site_type_symbol \n')
            file.write('_atom_site_label \n')            
            file.write('_atom_site_symmetry_multiplicity \n')
            file.write('_atom_site_fract_x \n')
            file.write('_atom_site_fract_y \n')
            file.write('_atom_site_fract_z \n')
            file.write('_atom_site_occupancy \n')
            file.write('Te0  Te  1  0.96868500  0.96868500  0.50000000  1 \n')
            file.write('Te1  Te  1  0.53131500  0.46868500  0.75000000  1 \n')            
            file.write('Te2  Te  1  0.46868500  0.53131500  0.25000000  1 \n')            
            file.write('Te3  Te  1  0.03131500  0.03131500  0.00000000  1 \n')            
            file.write('O4  O  1  0.74545000  0.85462400  0.30940300  1 \n')            
            file.write('O5  O  1  0.25455000  0.14537600  0.80940300  1 \n')            
            file.write('O6  O  1  0.85462400  0.74545000  0.69059700  1 \n')
            file.write('O7  O  1  0.35462400  0.75455000  0.05940300  1 \n')
            file.write('O8  O  1  0.14537600  0.25455000  0.19059700  1 \n')
            file.write('O9  O  1  0.24545000  0.64537600  0.44059700  1 \n')
            file.write('O10  O  1  0.75455000  0.35462400  0.94059700  1 \n')
            file.write('O11  O  1  0.64537600  0.24545000  0.55940300  1 \n')
                                                                                          
# empty lists to store the values for the lat params
A, B, C = [],[],[] 
            
# get the lattice parameters from the csv file
for file in os.listdir(home):
    if 'vol_vs_alats' in file:
        with open(os.path.join(home,file), 'r') as cif:
            content = cif.readlines()
            for line in content[1:]:
                line = line.split(',')
                A.append(float(line[2]))
                B.append(float(line[3]))
                C.append(float(line[4]))

# create the new CIF files
for i in range(len(A)):
    generate_cif_files(A,B,C)

            
            
            
