# -*- coding: utf-8 -*-
'''
    A demo of calling functions in another local file.
    Usage: calculating correlations.  The general syntax is:
    
        $ python main_cor.py <xx.csv>
    
    '''

import sys
import myFunctions as mf
import pandas as pd
#import argparse

if __name__ == '__main__':

    # read path to file    
    path = sys.argv[1]
    print(path)
    
    # read data
    data = pd.read_csv(path)
    
    # read data
#    parser = argparse.ArgumentParser(description = 'Help information')
#    parser.add_argument('-infile', help='path to input csv file')

#    infile = parse_args("-infile")
#    print(infile)

    # overview of data
    print("dimensions: {}".format(data.shape))
    # display first few rows
    print(data.head())

    # calculate correlation for nonzero values
    x = data.iloc[:,1]
    y = data.iloc[:,2]
    result = mf.nz_corr(x, y)
    print("nonzero corr: {}".format(result))

    x = data.iloc[:,2]
    y = data.iloc[:,3]
    result = mf.nz_corr(x,y)
    print("nonzero corr: {}".format(result))
