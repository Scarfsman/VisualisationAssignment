# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 16:10:42 2023

@author: Georg
"""

import pandas as pd
import matplotlib.pyplot as plt

gold_df = pd.read_csv('gold_df.csv', index_col=0)

#building a pie chart for Michael Phelps active years
phelps_df = gold_df[(gold_df['Year'] >= 2004) & (gold_df['Year'] <= 2016)]

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
        if x in df['Name'].unique():
            #if the name is in the athelte column, we can create a new row for our pie_df
            #by simply filtering for the athletes name nd summing the medal column
            newRow = pd.DataFrame([{'Name': x, 'Count': df[df['Name'] == x]['Medal'].sum(numeric_only = True)}])
        else:
            #if looking for country total, we need to filter out the extra rows for team events
            temp_df = df.groupby(['Event', 'Team', 'Year']).sum(numeric_only = True).reset_index()
            temp_df['Medal'] = 1
            newRow = pd.DataFrame([{'Name': x, 'Count': temp_df[temp_df['Team'] == x]['Medal'].sum(numeric_only = True)}])
        pie_df = pd.concat([pie_df, newRow], axis=0, ignore_index=True)
            
    fig, ax = plt.subplots()
    ax.pie(pie_df['Count'], labels = pie_df['Name'], explode=[0.1,0,0,0,0,0])
    plt.show()
        
#the list of names we want to use for our pie chart
namesToPlot = ['Michael Fred Phelps, II', 'Italy', 'France', 'Germany', 'Spain', 'Poland']

namesToPie(namesToPlot, phelps_df)
            
            
        


