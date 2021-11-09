import subprocess as sb
import os

home = '/home/user/Desktop/CompMatPhys/TeO2/data'


# get the dirs within home
dirs = [i for i in os.listdir(home)]

# access each subdir and convert the cif files into QE .in files
for d in dirs:
    new_path = os.path.join(home,d)
    os.chdir(new_path)
    for file in os.listdir(new_path):
        if os.path.splitext(file)[1] == '.cif':
            print(file)
            name = os.path.splitext(file)[0] + '.in'
            cmd = 'cif2cell {} -p quantum-espresso -o {} '.format(file, name)
            sb.Popen(cmd, shell = True)            
