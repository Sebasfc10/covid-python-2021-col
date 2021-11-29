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

#6
dead = len(data[data['Ubicación del caso'] == 'Fallecido'])
print(f"ejercicio 6: {dead}")

#7
conta = data.groupby('Tipo de contagio').size().sort_values(ascending = False)
print(f"ejercicio 7: {conta}")

#8
data['Nombre departamento'].replace('Tolima','TOLIMA',inplace=True)
data['Nombre departamento'].replace('Caldas','CALDAS',inplace=True)
depa = len(data.groupby('Nombre departamento').size().sort_values(ascending = False))
print(f"ejercicio 8: {depa}")

#9
lista_depa= data.groupby('Nombre departamento').size().sort_values(ascending = False)
print(f"ejercicio 9: {lista_depa}")

#10
ty = data.groupby('Ubicación del caso').size().sort_values(ascending = False)
print(f"ejercicio 10: {ty}")

#11
fdepa = data.groupby('Nombre departamento').size().sort_values(ascending = False).head(10)
print(f"ejercicio 11: {fdepa}")

#12
fdepadead = data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre departamento').size().sort_values(ascending = False).head(10)
print(f"ejercicio 12: {fdepadead}")

#13
fdeparecu = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending = False).head(10)
print(f"ejercicio 13: {fdeparecu}")

#14
contaco = data.groupby('Nombre municipio').size().sort_values(ascending = False).head(10)
print(f"ejercicio 14: {contaco}")

#15
fmundead = data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre municipio').size().sort_values(ascending = False).head(10)
print(f"ejercicio 15: {fmundead}")

#16
fmunrecu = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending = False).head(10)
print(f"ejercicio 16: {fmunrecu}")

#17
city = data.groupby(['Nombre departamento','Nombre municipio']).size().sort_values(ascending = False)
print(f"ejercicio 17: {city}")

#18
citygender = data.groupby(['Nombre departamento','Nombre municipio','Sexo']).size()
print(f"ejercicio 18: {citygender}")

#19
promedioC = data.groupby(['Nombre departamento','Nombre municipio','Sexo']).Edad.mean()
print(f"ejercicio 19: {promedioC}")

#20
data['Nombre del país'].replace('ESTADOS UNIDOS','ESTADOS UNIDOS DE AMÉRICA',inplace=True)
data['Nombre del país'].replace('VENEUELA','VENEZUELA',inplace=True)
data['Nombre del país'].replace('MEXICO','MÉXICO',inplace=True)
cProce = data.groupby('Nombre del país').size().sort_values(ascending = False)
print(f"ejercicio 20: {cProce}")

#21
dateConta = data.groupby('Fecha de diagnóstico').size().sort_values(ascending = False)
print(f"ejercicio 21: {dateConta}")

#22
morta = (len(data[data['Ubicación del caso'] == 'Fallecido']) / len(data)) * 100
recu = (len(data[data['Recuperado'] == 'Recuperado']) / len(data)) * 100
print(f"ejericio 22: la tasa de mortalidad es: {morta} y la tasa de recuperados es de: {recu}")

#23
mordepa = (data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre departamento').size().sort_values(ascending = False) / data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre departamento').size().sort_values(ascending = False).sum()) * 100
recudepa = (data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending = False) / data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending = False).sum()) * 100
print(f"ejercicio 23: tasa de mortalidad de los departamentos {mordepa} y tasa de recuperacion de los departamentos {recudepa}")

#24
mortacity = (data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre municipio').size().sort_values(ascending = False) / data[data['Ubicación del caso'] == 'Fallecido'].groupby('Nombre municipio').size().sort_values(ascending = False).sum()) * 100
recucity = (data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending = False) / data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending = False).sum()) * 100
print(f"ejercicio 24: tasa de mortalidad{mortacity} y tasa de recuperacion {recucity} de la ciudad")

#25
city2 = data.groupby(['Nombre municipio','Ubicación del caso']).size()
print(f"ejericio 25: {city2}")

#26
pedadcity = data.groupby(['Nombre municipio','Sexo']).Edad.mean()
print(f"Punto 26: {pedadcity}")

#27
data.groupby('Fecha de diagnóstico').size().cumsum().plot(label = "Contagios",figsize=(25,10))
Fallecidos = data[data['Ubicación del caso'] == 'Fallecido']
Fallecidos.groupby('Fecha de diagnóstico').size().cumsum().plot(label = "Fallecidos",figsize=(25,10))
Recuperado = data[data['Recuperado'] == 'Recuperado']
Recuperado.groupby('Fecha de diagnóstico').size().cumsum().plot(label = "Recuperados",figsize=(25,10))
plt.legend()
plt.show()

#28
data.groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(label = "Contagios",figsize=(20,10))
Fallecidos = data[data['Ubicación del caso'] == 'Fallecido']
Fallecidos.groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(label = "Fallecidos",figsize=(20,10))
Recuperado = data[data['Recuperado'] == 'Recuperado']
Recuperado.groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(label = "Recuperados",figsize=(20,10))
plt.legend()
plt.show()

#29
data.groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(label = "Contagios",figsize=(20,10))
Fallecidos = data[data['Ubicación del caso'] == 'Fallecido']
Fallecidos.groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(label = "Fallecidos",figsize=(20,10))
Recuperado = data[data['Recuperado'] == 'Recuperado']
Recuperado.groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(label = "Recuperados",figsize=(20,10))
plt.legend()
plt.show()

#30
edadage = data[data['Ubicación del caso'] == 'Fallecido'].groupby('Edad').size().sort_values(ascending = False)
print(f"ejercicio 30: {edad age}")

#31
poraten = ((data.groupby('Ubicación del caso').size().sort_values(ascending = False)) / ((data.groupby('Ubicación del caso').size().sort_values(ascending = False)).sum())) * 100
print(f"ejercicio 31: {poraten}")

#32
data.groupby(['Ubicación del caso']).size().sort_values(ascending = False).plot(kind='bar')

#33
data.groupby(['Sexo']).size().sort_values(ascending = False).plot(kind='bar')