# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 14:07:44 2021

@author: jeha2
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('covid_22_noviembre.csv')
data['Sexo'].replace('f','F',inplace=True)
data['Sexo'].replace('m','M',inplace=True)
data['Estado'].replace('leve','Leve',inplace=True)
data['Estado'].replace('LEVE','Leve',inplace=True)

#1
n = len(data)
print(f"ejercicio 1: {n}")