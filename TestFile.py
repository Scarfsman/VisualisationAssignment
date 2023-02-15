# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:16:02 2023

@author: Georg
"""

import pandas as pd
import matplotlib.pyplot as plt

#importing the data
df = pd.read_csv('interest_rate.csv', sep = ";")
#converting the date column to a format that works with the plot function in matplotlib
df['date'] = pd.to_datetime(df['date'])
#forward filling the missing values. I have assumed that once an interest rate has been oberserved
#at a specific date, it is unchanged until the next value is given
df = df.fillna(method = 'ffill')

cols = ['federal_reserve_system', 'bank_england', 'bank_japan']

def dfToLines(data, X, Y, ax, labels = None, title = None):
    """
    Creates a line plot comparing serveral variables on the same graph
    
    data -> pd.Dataframe - the data frame the values are taken from
    
    X -> str() - the column name for the variable on the X-axis
    
    Y -> list[str()] - the column name(s) for the variable on 
    the y axis. 
    
    ax -> plt.ax - the axis to plot the graph on 
    
    labels -> list[str()] - optional list, overrides the column names for the graph lables
    
    title -> str() - opional, adds a title to the grpah
    """
    
    for column in Y:
        ax.plot(data[X], data[column], label = column)
        
    plt.legend()
    plt.show()
        
    
fig, ax = plt.subplots()

dfToLines(df, 'date', cols, ax)






    