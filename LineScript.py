# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 15:16:02 2023

@author: Georg
"""

import pandas as pd
import matplotlib.pyplot as plt

gold_df = pd.read_csv('gold_df.csv', index_col=0)

def plotTeamMedals(teams, years, colours):
    """
    Parameters
    ----------
    Y -> list[str()] - the column name(s) for the variable on the y axis. 
    years -> List[int()] - adds vertical lines to the graph at the corresponding 
    year value. plots nothing if the value passed in the list is 0.
    colours -> list[str()] - the colour the corresponding countries lines will be, 
    i.e. colours[i] will be the colour for the lines generated for teams[i]
    ----------
    Creates a line plot comparing serveral countries gold medals on the same graph
    """
    
    fig, ax = plt.subplots()
    
    for i, team in enumerate(teams):
        # since we are generating the linegraph to look at cummulative medals, we need to 
        # format our data so that we can run the cumsum() function on the medals column
        temp_df = gold_df[gold_df['Team'] == team]
        temp_df = temp_df.drop(['Name'], axis = 1)
        temp_df = temp_df.groupby(['Year', 'Team', 'Event']).sum(numeric_only = True)
        temp_df['Medal'] = 1
        temp_df = temp_df.groupby(['Year']).sum(numeric_only = True).reset_index()
        temp_df.loc[:,'Medal'] = temp_df.loc[:,'Medal'].cumsum()
        ax.plot(temp_df['Year'], temp_df['Medal'], label = team, color = colours[i])
        #ignore 0s in the year column
        if years[i] != 0:
            ax.axvline(years[i], alpha = 0.85, linestyle = '--', color = colours[i])
        
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Gold Medals')
    plt.savefig('Lineplot.png')
    plt.show()

#the countries we are ploting medals for
countries = ['Germany', 'Canada','China', 'Great Britain', 'Brazil']
#the years the countries hosted the olympics
years = [0, 0, 2008, 2012, 2016]
#the colour the corresponding countries lines will be
colours = ['purple', 'pink','red', 'blue', 'green', ]

plotTeamMedals(countries, years, colours)









    