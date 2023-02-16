# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:16:02 2023

@author: Georg
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Athletes_summer_games.csv')

gold_df = df[df['Medal'] == 'Gold']

gold_df = gold_df[['Name', 'Team', 'Medal', 'Event', 'Year']]
gold_df['Medal'] = 1

gold_df = gold_df.groupby(['Year', 'Team']).sum().reset_index()


def plotTeamMedals(Y, ax, labels = None, title = None):
    """
    Creates a line plot comparing serveral countries gold medals on the same graph
    
    Y -> list[str()] - the column name(s) for the variable on 
    the y axis. 
    
    ax -> plt.ax - the axis to plot the graph on 
    
    title -> str() - opional, adds a title to the grpah
    """
    
    for team in Y:
        print('Creating line for {}'.format(team))
        temp_df = gold_df[gold_df['Team'] == team]
        ax.plot(temp_df['Year'], temp_df['Medal'], label = team)
        
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Gold Medals')
    plt.show()
        
    
fig, ax = plt.subplots()

plotTeamMedals(['France', 'United States', 'Great Britain', 'Soviet Union'], ax)






    