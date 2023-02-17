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
gold_df = gold_df.groupby(['Year', 'Team', 'Event', 'Medal']).sum().reset_index()
gold_df['Medal'] = 1



def plotTeamMedals(Y, ax, years, colours, title):
    """
    Creates a line plot comparing serveral countries gold medals on the same graph
    
    Y -> list[str()] - the column name(s) for the variable on 
    the y axis. 
    
    ax -> plt.ax - the axis to plot the graph on 
    
    title -> str() - opional, adds a title to the grpah
    
    years -> List[int()] - optional, adds vertical lines to the 
    """
    
    for i, team in enumerate(Y):
        print('Creating line for {}'.format(team))
        temp_df = gold_df[gold_df['Team'] == team]
        temp_df['Medal'] = temp_df['Medal'].cumsum()
        ax.plot(temp_df['Year'], temp_df['Medal'], label = team, color = colours[i])
        if years:
            ax.axvline(years[i], alpha = 0.65, linestyle = '--', color = colours[i])
        
    plt.legend()
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Gold Medals')
        
    
fig, ax = plt.subplots()

countries = ['Australia', 'China', 'Great Britain', 'Japan']
years = [2000, 2008, 2012, 2020]
colours = ['green', 'red', 'blue', 'purple']
title = 'All Time Gold Medals for Recent Host Nations'

plotTeamMedals(countries, ax, years, colours, title)








    