# -*- coding: utf-8 -*-
'''
    A demo of calling functions in another local file.
    
'''

import sys
import myFunctions as mf
import pandas as pd

if __name__ == '__main__':
    # read data
    data = pd.read_csv("data.csv")

    # overview of data
    print("dimensions: {}".format(data.shape))
    # display first few rows
    print(data.head())

    # calculate correlation for nonzero values
    x = data.ix[:,1]
    y = data.ix[:,2]
    result = mf.nz_corr(x, y)
    print("nonzero corr: {}".format(result))

    x = data.ix[:,2]
    y = data.ix[:,3]
    result = mf.nz_corr(x,y)
    print("nonzero corr: {}".format(result))
