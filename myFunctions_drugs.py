import math
import numpy as np
from scipy.stats.stats import pearsonr

def pearson_cor (x, y):
    '''This function calculates Pearson correlation between vector x and y when NAs are present
                
        Parameters
        ------------
        x: numpy array
        y: numpy array
        
        Return
        -----------
        Pearson correlation or nan
        '''
    # find NAs
    # mark the pair (x,y)
    # as long as one of the two values is NA
    nonas = np.logical_and(~np.isnan(x), ~np.isnan(y))
    print (np.isnan(x))
    print (np.isnan(y))
    print (~np.isnan(x))
    print (~np.isnan(y))
    print (nonas)
    
    # calculate Pearson correlation
    # using function pearson_cor below
    # NAs are ignored
    result = pearsonr(x[nonas], y[nonas])

    return result
