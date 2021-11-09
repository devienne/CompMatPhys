# This script is able to:


import os

home = os.getcwd()

for file in os.listdir(home):
    if os.path.splitext(file)[1] == '.cif':
        filename = os.path.splitext(file)[0]
        #print(filename)
        dirpath = os.path.join(home,filename + '_SFC')
        if os.path.isdir(dirpath):
            pass
        else:
            os.mkdir(dirpath)
