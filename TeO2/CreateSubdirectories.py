# This script is able to:



import os

home = os.getcwd()

# get the lattice parameters from the csv file
for file in os.listdir(home):
    if 'vol_vs_alats' in file:
        with open(os.path.join(home,file), 'r') as cif:
            content = cif.readlines()
            for line in content[1:]:
                line = line.split(',')
                A = float(line[2])
                name = 'TeO2_{}'.format("%.6f" % A)
                new_dir = os.path.join(home,'data',name)
                try:
                    os.mkdir(new_dir)
                except:
                    pass
