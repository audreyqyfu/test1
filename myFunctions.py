import math
import numpy as np
from scipy.stats.stats import pearsonr

def nz_corr(x, y, digits=4):
    '''This function calculates Pearson correlation between two vectors,
        excluding zeros in either vector

        Parameters
        ------------
        x: numpy array
        y: numpy array
        
        Return
        -----------
        Pearson correlation or nan
        '''
    nas = np.logical_or(x == 0, y == 0)
    result = pearson_cor(x[~nas], y[~nas])
    if not math.isnan(result):
        result = round(result, digits)
    return result

def pearson_cor (x, y, digits=6):
    '''This function calculates Pearson correlation between vector x and y.
        It returns nan if x or y has 2 data points or less, or if either of them does not vary
        
        Parameters
        ------------
        x: numpy array
        y: numpy array
        
        Return
        -----------
        Pearson correlation or nan
        '''
    print("x:\n")
    print(x.head())
    print("\ny:\n")
    print(y)
    print("x.std: {}".format(x.std()))
    print("y.std: {}".format(y.std()))
    print("y.mean: {}".format(y.mean()))

    if (len(x) > 2) and (round(x.std(), digits) > 0) and (round(y.std(), digits) > 0):
        print("defined")
        corr = pearsonr(x, y)[0]
    else:
        print("undefined")
        corr = np.nan
    
    return corr
