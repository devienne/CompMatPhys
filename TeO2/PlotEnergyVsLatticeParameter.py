# This script is able to:
# 1. Open the csv file containing the energy of each reduced volume value
# 2. Fit this data with the Murnaghan equation of State
# 3. Plot (and save)  the result

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import leastsq

df = pd.read_csv('/home/user/Desktop/CompMatPhys/FeAl/LatticeParameterOptimization.csv')
df.sort_values('Lat.Par(A)')

###  Fit with the Murnaghan equation
xdata = df['Vol(A3)'].tolist()
ydata = df['Energy(Ry)'].tolist()

# transform the lists into numpy arrays
xdata = np.array(xdata)
ydata = np.array(ydata)

# Murnaghan equation of state:
def Murnaghan(parameters, vol):
    E0, B0, BP, V0 = parameters
    
    E = E0 + (B0*vol/BP)*(((V0/vol)**BP)/(BP-1) + 1)- V0*B0/(BP - 1) 
    
    return E

# function to calculate the best fit params
def best_fit(pars, y, x):
    # we want to minimize this function
    err = y - Murnaghan(pars, x)
    return err

# initial guess of params
x0 = [-730.0, 0.54, 2.0, 16.5] # initial guess of parameters

# calculate the best fir params
plsq = leastsq(best_fit, x0, args=(ydata, xdata))

# Plot
x = np.linspace(min(xdata), max(xdata), 50)
y = Murnaghan(plsq[0], x)

fig, ax = plt.subplots()
ax.plot(x, y, 'k-', label = 'EoS')
ax.plot(xdata, ydata, 'ro', label = 'DFT')
ax.set_xlabel('Unit-cell volume $(A³)$', fontsize = 12,labelpad=5)
ax.set_ylabel('Energy (Ry)', color='k', fontsize = 12,labelpad=5)
plt.legend()
plt.savefig('/home/user/Desktop/CompMatPhys/FeAl/DFT_vs_Murnaghan-EoS.png', bbox_inches='tight',dpi = 300)
plt.show()

with open('/home/user/Desktop/CompMatPhys/FeAl/LatticeParameterForMinimumVolume.csv', 'w') as file:
    file.write('Volume(A3),Energy(Ry) \n')
    Emin = np.amin(y) 
    Emin_ind = np.where(y == np.amin(y))[0][0]
    Vmin = x[Emin_ind]
    file.write('{},{} \n'.format(Vmin, Emin))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
