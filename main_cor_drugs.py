# -*- coding: utf-8 -*-
'''
    A demo of calling functions in another local file.
    Usage: calculating correlations.  The general syntax is:
    
        $ python main_cor.py <xx.csv>
    
    '''

import sys
import myFunctions_drugs as mf
import pandas as pd
import numpy as np
from scipy.stats.stats import pearsonr

if __name__ == '__main__':

    # read path to file    
    path = sys.argv[1]
    print(path)
    
    # read data
    data = pd.read_table(path, index_col=0)
    
    # overview of data
    print("dimensions: {}".format(data.shape))
    # display first few rows
    print(data.head())

    # calculate correlation between two vectors
    
    # use the correlation method
    print ("Using the correlation method from Pandas:")
    print (data.iloc[:,range(3)].corr(method="pearson"))
    
    # use our own function
    print ("Using our own correlation function:")
    x = data.iloc[range(5),1]
    y = data.iloc[range(5),2]
    print (x)
    print (y)
    
#    print (pearsonr(x,y))
    
    result = mf.pearson_cor(x, y)
    print("Pearson corr: {}".format(result))

