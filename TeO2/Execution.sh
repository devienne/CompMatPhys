#!/bin/sh
# reminder: from now on, what follows the character # is a comment

# Create and complete the QE .in files
#echo 'Create and complete QE input files in progess..'
#python3 CreateBashScriptToCreateEverything.py
#bash ScriptToCreateEverything.sh 
#echo 'CIF and QE .in files created successfully'
#echo '#'
# Create the script to execute everything
#echo 'create execution script in progress...'
#python3 CreateBashScriptToExecuteCompleteQEInputFiles.py
#echo 'Execution script created successfully'
#echo '#'
# Execute
#echo 'Execution...'
#bash ScriptToExecuteCompleteQEInputFiles.sh
#echo 'Execution finished, vai tomar no cu caralho.'
#echo '#'

# Plot
echo 'Plot the energy vs volume fitted with the Murnaghan eq os states'
python3 LatticeParameterOptimizationDataFrame.py
python3 PlotEnergyVsLatticeParameter.py


