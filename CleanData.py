# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 16:05:01 2023

@author: Georg
"""

# =============================================================================
# Script to format the source data so that it can be used in the way that
# we want to for our graphs
# =============================================================================

import pandas as pd

# =============================================================================
# setting up the gold_df dataframe, sued for graphs where we are interested only in 
# the total number of gold medals an athlete or a nation has won
# =============================================================================

df = pd.read_csv('athlete_events.csv')

gold_df = df[df['Medal'] == 'Gold']
gold_df = gold_df[gold_df['Season'] == 'Summer']
gold_df = gold_df[['Name', 'Team', 'Medal', 'Event', 'Year']]
gold_df = gold_df.groupby(['Year', 'Team', 'Event', 'Medal', 'Name']).sum().reset_index()

# =============================================================================
# changing the stings in the Medal column for 'gold', to 1, so it can easier be used
# for plotting functions:
# =============================================================================
    
gold_df['Medal'] = 1

gold_df.to_csv('gold_df.csv')