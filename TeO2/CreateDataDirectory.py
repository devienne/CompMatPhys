# This script is able to:


import os

home = os.getcwd()

data_dir = os.path.join(home,'data')

if os.path.isdir(data_dir):
    pass
else:
    os.mkdir(data_dir)

                
                








