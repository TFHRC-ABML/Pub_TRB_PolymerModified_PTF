# Title: Analysis of Double-Edge Notched Tension (DENT) test Parameters
# 
# Description: This script includes a function to calculate the Crack Tip Opening Displacement (CTOD) using the DENT 
#   test results.
# 
# Example input:
#   inps  = [{'FractureEnergy': array([1.0219, 2.528 , 4.5478]), 'MaxLoad': 28.7, 
#             'Ligament': array([0.005, 0.01 , 0.015]), 'Area': array([5.0e-05, 1.0e-04, 1.5e-04])}, 
#            {'FractureEnergy': array([0.9851, 2.4823, 4.6736]), 'MaxLoad': 29.8, 
#             'Ligament': array([0.005, 0.01 , 0.015]), 'Area': array([5.0e-05, 1.0e-04, 1.5e-04])}]
#
# Author: Farhad Abdollahi (farhad.abdollahi.ctr@dot.gov)
# Date: 07/03/2025
# ======================================================================================================================

# Importing the required libraries.
import os
import itertools
import numpy as np


def Calc_DENT(inps):
    """
    This function calculates the CTOD values using the DENT test results. 

    :param inps: a list of dictionaries of the DENT test results.
    :return: A dictionary of the results. 
    """
    # Define different combinations. 
    NumReps = len(inps)
    combinations = list(itertools.product(
        [i for i in range(NumReps)], 
        [i for i in range(NumReps)], 
        [i for i in range(NumReps)]))
    # Calculate the CTOD for each combinations.
    CTOD = np.zeros(len(combinations))
    for j, comb in enumerate(combinations):
        Ligament = np.array([inps[comb[i]]['Ligament'][i] for i in range(3)])
        Area     = np.array([inps[comb[i]]['Area'][i] for i in range(3)])
        Failure  = np.array([inps[comb[i]]['FractureEnergy'][i] for i in range(3)])
        Wt       = Failure / Area
        Coeff = np.polyfit(Ligament, Wt, 1)
        Intercept = Coeff[1]
        CTOD[j] = (Intercept / (float(inps[comb[0]]['MaxLoad']) / float(inps[comb[0]]['Area'][0]))) * 1000
    # Return the results. 
    return CTOD
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================


if __name__ == '__main__':
    pass

