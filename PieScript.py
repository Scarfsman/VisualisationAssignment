# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 16:10:42 2023

@author: Georg
"""

import pandas as pd
import matplotlib.pyplot as plt

gold_df = pd.read_csv('gold_df.csv')

phelps_df = gold_df[gold_df['Year'] >= 2004]

def namesToPie(names, df):
    """    
    Parameters
    ----------
    cat : lis[st()] -> Whether the ith name passed in the name list is an athlete or a country. 
    a -> athlete
    c-> country
    name : lis[st()] -> list holding the names of the 
    -------
    
    Plots a pir chart of the gold medals for the selected names
    """
    pie_df = pd.DataFrame(columns = ['Name', 'Count'])
    
    
    for x in names:
# =============================================================================
#         checks whether the names passed is in the athlete column, so that we can filter the correct row in the
#         database
# =============================================================================
        if x in df['Name'].unique():
            newRow = pd.DataFrame([{'Name': x, 'Count': df[df['Name'] == x]['Medal'].sum()}])
        else:
            newRow = pd.DataFrame([{'Name': x, 'Count': df[df['Team'] == x]['Medal'].sum()}])
        pie_df = pd.concat([pie_df, newRow], axis=0, ignore_index=True)
        print(pie_df)
            
    fig, ax = plt.subplots()
    ax.pie(pie_df['Count'], labels = pie_df['Name'])
    plt.show()
        
#the list of names we want to use for our pie chart
namesToPlot = ['Michael Fred Phelps, II', 'Brazil', 'Russia', 'India', 'China']

namesToPie(namesToPlot, phelps_df)
            
            
        


