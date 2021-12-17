# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 20:06:20 2021

@author: Ethan
"""

import streamlit as st
import numpy as np
import pandas as pd
import random as rd
import matplotlib.pyplot as plt


st.title('Seneca Trading Returns - 2021')

# Generate our random monthly returns data
returns = rd.sample(range(0,15), 12)

d = pd.DataFrame(np.array([1,2,3,4,5,6,7,8,9,10,11,12]), 
                 columns = ['Month'])

# Append returns to dataframe
d['Returns'] = returns


plt.bar(d['Month'], d['Returns'], 
        color = 'cadetblue', edgecolor = 'slategray', zorder=3)
plt.ylabel('Return %')
plt.xlabel('Month')
plt.grid(zorder=0)

st.bar_chart(d.iloc[:, 1:2])
st.table(d)