# Study of TeO2 using Density Functional Theory (DFT)

In this repository there is a series of Python scripts that can be used to automatize the process of using Quantum Espresso (QE) to run simulations of TeO2.

Underneath is a short description of what each script is able to do:

1. GetLatticeParameterFromCIFfiile: access the original .cif file (i.e., the .cif file downloaded from the materialsproject.org website) and get the lattice parameters
2. CreateDataDirectory: creates a directory called 'data' where all files will be stored
3. CreateCIFfilesForDifferentLatticeParams: based on the lattice parameters obtained from the original .cif file, this script creates a series of new .cif with other values for the lattice parameters, in such a way that the final volume of each unit cell is 0.95, 0.90, 0.85 and 0.8 the initial volume (this script is meant for the calculation of the lattice parameter that minimized the total energy)
4. ConvertCIFToQEIn: convert the .cif files into QE .in files
5. CompleteQEInpytFilesForTeO2Optimization: complete the QE .in files to make them fit to run the simulations
6. LatticeParameterOptimizationDataFrame: after finished the simulation of all QE .in, this script access each .out file, get the value of the energy and the volume of the unit cell and saves it in a .csv file
7. PlotEnergyVsLatticeParameter: Access the .csv file created in the step before and make a plot of the energy as a function of the unit cell volume (in angstron^3)

To optimize the process, there is a shell script (Execution.sh) that calls all the other scripts and executes the whole process in sequence.

In other words, the only script that you need to run is the Execution.sh.

When running the Execution.sh file, two new .sh scripts will be create, and within each of these files the complete set os Python scripts will be called.

** All the scripts were created using ABSOLUTE paths. Therefore, it's required to change it in some scripts in order to use them. **
