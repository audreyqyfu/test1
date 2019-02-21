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

def pearson_cor (x, y):
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
    if (len(x) > 2) and (x.std() > 0) and (y.std() > 0):
        corr = pearsonr(x, y)[0]
    else:
        corr = np.nan
    
    return corr
