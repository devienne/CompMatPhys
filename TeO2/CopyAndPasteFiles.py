# This script is able to:

import os
import shutil as st

home = os.getcwd()

dirnames = []

for file in os.listdir(home):    
    if os.path.isdir(file) == True and '_SFC' in file:
        dirnames.append(file)
        #print(file)

#print(dirnames)
        
for file in os.listdir(home):
    if os.path.isdir(file) == False:
        if os.path.splitext(file)[1] == '.in' or os.path.splitext(file)[1] == '.out' or os.path.splitext(file)[1] == '.xml' or os.path.splitext(file)[1] == '.cif' :
            filename = os.path.splitext(file)[0]
            for dirname in dirnames:
                if filename in dirname:
                    IN = file
                    OUT = os.path.join(home,dirname)
                    st.move(IN,OUT)
                    #print('y')


#st.move(origin,end)
