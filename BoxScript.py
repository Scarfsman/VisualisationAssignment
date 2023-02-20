# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:48:16 2023

@author: Georg
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gold_df.csv', index_col=0)

country_df = df.groupby(['Year', 'Team', 'Event']).sum(numeric_only = True).reset_index()
britain_df = country_df[country_df['Team'] == 'Great Britain']
