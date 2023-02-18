# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 16:05:01 2023

@author: Georg
"""

import pandas as pd

df = pd.read_csv('Athletes_summer_games.csv')

gold_df = df[df['Medal'] == 'Gold']

gold_df = gold_df[['Name', 'Team', 'Medal', 'Event', 'Year']]
gold_df = gold_df.groupby(['Year', 'Team', 'Event', 'Medal', 'Name']).sum().reset_index()
gold_df['Medal'] = 1

gold_df.to_csv('gold_df.csv')