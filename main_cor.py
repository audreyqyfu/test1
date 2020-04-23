# -*- coding: utf-8 -*-
'''
    A demo of calling functions in another local file.
    Usage: calculating correlations.  The general syntax is:
    
        $ python main_cor.py <xx.csv>
    
    '''

import sys
import myFunctions as mf
import pandas as pd

if __name__ == '__main__':

    # read path to file    
    path = sys.argv[1]
    print(path)
    
    # read data
    data = pd.read_csv(path)
    
    # overview of data
    print("dimensions: {}".format(data.shape))
    # display first few rows
    print(data.head())

    # add comments


    # calculate correlation for nonzero values
    # in two vectors
    x = data.iloc[:,1]
    y = data.iloc[:,2]
    result = mf.nz_corr(x, y)
    print("nonzero corr: {}".format(result))

    x = data.iloc[:,2]
    y = data.iloc[:,3]
    result = mf.nz_corr(x,y)
    print("nonzero corr: {}".format(result))

    x = data.iloc[:,2]
    y = data.iloc[:,4]
    result = mf.nz_corr(x,y)
    print("nonzero corr: {}".format(result))
