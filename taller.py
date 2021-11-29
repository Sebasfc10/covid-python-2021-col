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

#2
data['Nombre municipio'].replace('puerto colombia','PUERTO COLOMBIA',inplace=True)
data['Nombre municipio'].replace('puerto COLOMBIA','PUERTO COLOMBIA',inplace=True)
data['Nombre municipio'].replace('MEDELLiN','MEDELLIN',inplace=True)
data['Nombre municipio'].replace('Galapa','GALAPA',inplace=True)
data['Nombre municipio'].replace('momil','MOMIL',inplace=True)
data['Nombre municipio'].replace('Guepsa','GUEPSA',inplace=True)
data['Nombre municipio'].replace('barrancabermeja','BARRANCABERMEJA',inplace=True)
data['Nombre municipio'].replace('Pensilvania','PENSILVANIA',inplace=True)
data['Nombre municipio'].replace('Anserma','ANSERMA',inplace=True)
n_m = len(data.groupby('Nombre municipio').size())
print(f"ejercicio 2: {n_m}")

#3
lista_m = data.groupby('Nombre municipio').size().sort_values(ascending = False)
print(f"ejericicio 3: {lista_m}")

#4
data['Ubicación del caso'].replace('casa','Casa',inplace=True)
data['Ubicación del caso'].replace('CASA','Casa',inplace=True)
casa = len(data[data['Ubicación del caso'] == 'Casa'])
print(f"ejercicio 4: {casa}")

#5
data['Recuperado'].replace('fallecido','Fallecido',inplace=True)
recuperado = len(data[data['Recuperado'] == 'Recuperado'])
print(f"ejercicio 5: {recuperado}")
