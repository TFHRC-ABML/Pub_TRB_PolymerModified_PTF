# Title: Analysis of Low Temperature Rheological Parameters
# 
# Description: This script includes a function to calculate the low temperature performance grade (LTPG) and ΔΤc values 
#   using the bending beam rheometer (BBR) test results. 
# 
# Example input:
#   inps = {'Temp1': array([-12, -12, -12]), 'mval1': array([0.31 , 0.31 , 0.307]), 'Sval1': array([235, 228, 206]), 
#           'Temp2': array([-18, -18, -18]), 'mval2': array([0.26 , 0.254, 0.256]), 'Sval2': array([419, 385, 456])}
#
# Author: Farhad Abdollahi (farhad.abdollahi.ctr@dot.gov)
# Date: 07/02/2025
# ======================================================================================================================

# Importing the required libraries.
import os
import itertools
import numpy as np


def Calc_LTPG_DeltaTc(inps):
    """
    This function calculates the LTPG and ΔΤc values using the BBR test results at two different temperatures. 

    :param inps: a dictionary of the BBR test results, including the first and second temperatures and their 
    corresponding, m-values, and S-values.
    :return: A dictionary of the results. 
    """
    # First check the input temperatures to pass the 1°C telorance. 
    DeltaTemp1 = inps['Temp1'].max() - inps['Temp1'].min()
    DeltaTemp2 = inps['Temp2'].max() - inps['Temp2'].min()
    if DeltaTemp1 > 1.0:
        raise Exception(f'The testing temperature (first set) should have tolerance of less than 1°C, ' + 
                        f'while it is now {DeltaTemp1}°C! Please check the input data. ')
    if DeltaTemp2 > 1.0:
        raise Exception(f'The testing temperature (second set) should have tolerance of less than 1°C, ' + 
                        f'while it is now {DeltaTemp2}°C! Please check the input data. ')
    # Get the average testing temperatures.
    t1, t2 = inps['Temp1'].mean(), inps['Temp2'].mean()
    # Calculate the LTPG using different combinations based on S-values. 
    Combinations = list(itertools.product(range(len(inps['Sval1'])), range(len(inps['Sval2']))))
    LTPG_S = np.zeros(len(Combinations))
    for i, comb in enumerate(Combinations):
        Slope     = (inps['Sval2'][comb[1]] - inps['Sval1'][comb[0]]) / (t2 - t1)
        Intercept = inps['Sval1'][comb[0]] - Slope * t1
        LTPG_S[i] = (300 - Intercept) / Slope
    # Calculate the LTPG using different combinations based on m-values. 
    Combinations = list(itertools.product(range(len(inps['mval1'])), range(len(inps['mval2']))))
    LTPG_m = np.zeros(len(Combinations))
    for i, comb in enumerate(Combinations):
        Slope     = (inps['mval2'][comb[1]] - inps['mval1'][comb[0]]) / (t2 - t1)
        Intercept = inps['mval1'][comb[0]] - Slope * t1
        LTPG_m[i] = (0.300 - Intercept) / Slope
    # Calculate the LTPG. 
    if LTPG_m.mean() > LTPG_S.mean():
        LTPG = LTPG_m.copy() - 10
    else:
        LTPG = LTPG_S.copy() - 10
    # Calculate the Delta Tc. 
    DeltaTc_avg = LTPG_S.mean() - LTPG_m.mean()
    DeltaTc_std = np.sqrt(LTPG_S.std() ** 2 + LTPG_m.std() ** 2)
    # Return the results. 
    return {'LTPG_S': LTPG_S, 'LTPG_m': LTPG_m, 'LTPG': LTPG, 'LTPG_avg': LTPG.mean(), 'LTPG_std': LTPG.std(), 
            'DeltaTc_avg': DeltaTc_avg, 'DeltaTc_std': DeltaTc_std}
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================


if __name__ == '__main__':
    pass

