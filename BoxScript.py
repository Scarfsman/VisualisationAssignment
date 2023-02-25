# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:48:16 2023

@author: Georg
"""

import pandas as pd
import matplotlib.pyplot as plt

#read in our transofrmed dataset
df = pd.read_csv('gold_df.csv', index_col=0)

def createBox (teams):
    """

    Parameters
    ----------
    teams : list[str()] - The countries we want to create a boxplot for
    -------
    Generates a boxplot of the gold medal wins for the nations passed to the function
    """
    labels = []
    results = []
    
    for team in teams:  
# =============================================================================
#       for each team we pass to the function in our list, we create a pandas series:
#       and append it to our list of results. 
# =============================================================================
        temp = df[df['Team'] == team]
        temp = temp.drop(['Name'], axis = 1)
        temp = temp.groupby(['Year', 'Team', 'Event']).sum(numeric_only = True)
        temp['Medal'] = 1
        temp = temp.groupby(['Year']).sum(numeric_only = True)
        results.append(temp['Medal'])
        labels.append(team)
    
# =============================================================================
#     once we have our results, we pass the list to the boxplot function and 
#     use the teams list as our labels.
# =============================================================================   
    plt.boxplot(results, labels = labels)
    plt.savefig('Boxplot.png')
    plt.show()

#the teams we want to plot on our boxplot
teams = ['Germany', 'France', 'Spain']

createBox(teams)
