# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:16:02 2023

@author: Georg
"""

import pandas as pd
import matplotlib.pyplot as plt

gold_df = pd.read_csv('gold_df.csv', index_col=0)

def plotTeamMedals(Y, years, colours, title):
    """
    Creates a line plot comparing serveral countries gold medals on the same graph
    
    Parameters
    ----------
    Y -> list[str()] - the column name(s) for the variable on 
    the y axis. 
    title -> str() - opional, adds a title to the grpah
    years -> List[int()] - optional, adds vertical lines to the 
    ----------
    """
    
    fig, ax = plt.subplots()
    
    for i, team in enumerate(Y):
        print('Creating line for {}'.format(team))
        temp_df = gold_df[gold_df['Team'] == team]
        temp_df.loc[:,'Medal'] = temp_df.loc[:,'Medal'].cumsum()
        ax.plot(temp_df['Year'], temp_df['Medal'], label = team, color = colours[i])
        if years:
            ax.axvline(years[i], alpha = 0.65, linestyle = '--', color = colours[i])
        
    plt.legend()
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Gold Medals')

countries = ['Australia', 'China', 'Great Britain', 'Japan']
years = [2000, 2008, 2012, 2020]
colours = ['green', 'red', 'blue', 'purple']
title = 'Olympic Event Wins for Recent Host Nations'

plotTeamMedals(countries, years, colours, title)








    