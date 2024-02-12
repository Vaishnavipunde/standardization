# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:22:59 2023

@author: sai
"""

import pandas as pd

import numpy as np

from sklearn.preprocessing import StandardScaler

d=pd.read_csv("c:/2-dataset/mtcars.csv")

a=d.describe()

# Initialize the StandardScaler
scalar = StandardScaler()

# Standardize the data in DataFrame 'd' using StandardScaler
df = scalar.fit_transform(d)

# Create a DataFrame 'dataset' to store the standardized data
dataset = pd.DataFrame(df)

# Generate descriptive statistics for the standardized dataset
res = dataset.describe()
















