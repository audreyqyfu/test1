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
    # reset 0 as NA in x and y   
    nas = np.logical_or(x == 0, y == 0)
    
    # calculate Pearson correlation
    # using function pearson_cor below
    # NAs are ignored
    result = pearson_cor(x[~nas], y[~nas])
    
    # round the result to a desirable number of digits
    # or return nan
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
    print(y.head())
    print("x.std: {}".format(x.std()))
    print("y.std: {}".format(y.std()))
    print("x.mean: {}".format(x.mean()))
    print("y.mean: {}".format(y.mean()))

    corr = pearsonr(x,y)[0]

#    if (len(x) > 2) and (round(x.std(), digits) > 0) and (round(y.std(), digits) > 0):
#        print("defined")
#        corr = pearsonr(x, y)[0]
#    else:
#        print("undefined")
#        corr = np.nan
    
    return corr
