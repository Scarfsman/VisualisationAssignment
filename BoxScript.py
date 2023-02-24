# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:48:16 2023

@author: Georg
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gold_df.csv', index_col=0)

def createBox (teams):
    
    labels = []
    results = []
    
    for team in teams:    
        temp = df[df['Team'] == team]
        temp = temp.drop(['Name'], axis = 1)
        temp = temp.groupby(['Year', 'Team', 'Event']).sum(numeric_only = True)
        temp['Medal'] = 1
        temp = temp.groupby(['Year']).sum(numeric_only = True)
        results.append(temp['Medal'])
        labels.append(team)
    
    plt.boxplot(results, labels = labels)

teams = ['Germany', 'France', 'Spain']

createBox(teams)
