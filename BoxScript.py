# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:48:16 2023

@author: Georg
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gold_df.csv', index_col=0)

temp = df[df['Team'] == 'Great Britain']
temp = temp.drop(['Name'], axis = 1)
temp = temp.groupby(['Year', 'Team', 'Event']).sum(numeric_only = True)
temp['Medal'] = 1
temp = temp.groupby(['Year']).sum(numeric_only = True)

plt.boxplot(temp['Medal'])

