import src.clean_functions as cl_f
import pandas as pd
import numpy as np
import json
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns
import re

##Defining cleaning parameters
## params to clean km (max/min)
kmmax=300000
kmmin=2000

## params to clean año column (max/min)
anmax=15
anmin=1

## params to clean precio column (max/min)
prcmax=100000
prcmin=500

## Params low frequency
lf_model=100
lf_brand=200
lf_carro=500

##Bining params
ColumnsBin=['Longitud','Kilometros','Peso','Potencia']
Bins={'Longitud':10,
      'Kilometros':10,
      'Peso':8,
      'Potencia':6
     }

##weighted params
n_km=1
n_ano=1
n_pot=1.2

###Bringing up all CSVs from scraping
df1=pd.DataFrame(pd.read_csv("./input/cars_all.csv"))
print(df1.shape)

df1.columns=[
'Precio',
'Ano',
'Potencia',
'Kilometros',
'Combustible',
'Puertas',
'Cambio',
'Emisiones',
'Vendedor',
'Garantia',
'Colorexterior',
'Maletero',
'Longitud',
'Altura',
'Anchura',
'Plazas',
'Deposito',
'Peso',
'PesoMax.',
'Carroceria',
'Velocidad',
'Cmixto',
'Curbano',
'Extraurbano',
'0-100km/h',
'Autonomia',
'EmisionCO2',
'Cilindrada',
'Cilindros',
'Transmision',
'Parmaximo',
'Marchas',
'Traccion',
'model'
]

##Columns to drop
##dropcolumns=['EmisionCO2','Garantia','Colorexterior','Autonomia','PesoMax.','Transmision','Deposito','Vendedor','Altura','Anchura','Maletero']
##df1.drop(dropcolumns, axis=1, inplace=True)
df1=df1.dropna()
##Specific column/values combinations to remove
df1=df1.loc[df1['Kilometros'] != 'NUEVO']
df1=df1.loc[df1['Combustible'] != 'Híbrido']
df1=df1.loc[df1['Combustible'] != 'Eléctrico']

##Numerical columns (integers)
df1=cl_f.columnreplace(df1,"Precio","€")
df1=cl_f.columnreplace(df1,"Kilometros"," km")
df1=cl_f.columnreplace(df1,"Emisiones"," gr/mdiv3div")
df1=cl_f.columnreplace(df1,"Cilindrada"," cmdiv3div")
df1=cl_f.columnreplace(df1,"Parmaximo"," Nm")
df1=cl_f.columnreplace(df1,"Velocidad"," km/h")

##df1=cl_f.columnreplace(df1,"Maletero"," l")
##df1=cl_f.columnreplace(df1,"Deposito"," l")
df1=cl_f.columnreplace(df1,"Longitud"," cm")
##df1=cl_f.columnreplace(df1,"Anchura"," cm")
##df1=cl_f.columnreplace(df1,"Altura"," cm")
df1=cl_f.columnreplace(df1,"Peso"," kg")

##Numerical columns (floats)
df1=cl_f.columnreplace2(df1,"0-100km/h"," s")
df1=cl_f.columnreplace2(df1,"Cmixto"," l")
df1=cl_f.columnreplace2(df1,"Curbano"," l")
df1=cl_f.columnreplace2(df1,"Extraurbano"," l")

##Adjusting columns with numerical and non numerical
cl_f.columndigits(df1,'Cilindros')
cl_f.columndigits(df1,'Potencia')

## Creating new column
df1['model']=cl_f.columnlist(df1,"model")
df1['Provincia']=[i[1].strip() for i in df1['model']]
df1['Brand']=[i[2].strip() for i in df1['model']]
df1['Model']=[i[3].strip() for i in df1['model']]

##Encoding categorical variables
df1['Cambio']=[cl_f.cambio(i) for i in df1['Cambio']]
df1['Traccion']=[cl_f.traccion(i) for i in df1['Traccion']]
df1['Puertas']=[cl_f.puertas(i) for i in df1['Puertas']]
df1['Marchas']=[cl_f.marchas(i) for i in df1['Marchas']]

##Encoding column año
df1['Ano'] = df1['Ano'].str[-4:]
df1=df1.dropna()
df1['Ano'] = df1['Ano'].astype(float)
df1['Ano']=2019-df1['Ano']

##Dropping ouliers rows in km
df1 = df1[df1["Kilometros"]<=kmmax]
df1 = df1[df1["Kilometros"]>=kmmin]

##Dropping ouliers rows for año
df1 = df1[df1["Ano"]<=anmax]
df1 = df1[df1["Ano"]>=anmin]

##Dropping ouliers rows for precio
df1 = df1[df1["Precio"]<=prcmax]
df1 = df1[df1["Precio"]>=prcmin]

##Casting columns
df1['Potencia']=df1['Potencia'].astype('float')
df1['Cilindros']=df1['Cilindros'].astype('float')

##Dropping columns
dropcolumns2=['Provincia','model']
df1.drop(dropcolumns2, axis=1, inplace=True)
##df1=df1.dropna()
df1 = df1[df1["Longitud"] !=0]
df1 = df1[df1["Velocidad"] !=0]
df1 = df1[df1['Cmixto'] !=0]

##removing low frequency Brands and models
df1=cl_f.RemoveLowFreq(df1,"Model",lf_model)
df1=cl_f.RemoveLowFreq(df1,"Brand",lf_brand)
df1=cl_f.RemoveLowFreq(df1,"Carroceria",lf_carro)


df1.to_csv('./output/cars_clean_1.csv', index=False)


##Bining of longitud/peso to try to adjust for brands distinct models
ColumnsBin=['Longitud','Kilometros','Peso','Potencia']
Bins={'Longitud':8,
      'Kilometros':8,
      'Peso':8,
      'Potencia':8
     }

for i in ColumnsBin:
    cl_f.columnBining(df1,i,Bins[i])

##Encoding through get_dummies
df1 = pd.get_dummies(df1, columns=['Combustible'])
df1 = pd.get_dummies(df1, columns=['Brand'])
df1 = pd.get_dummies(df1, columns=['Carroceria'])

##Normalization
ColumnsNorm=['Emisiones','Longitud','Plazas','Peso','Cilindros','Velocidad','Cmixto','Curbano','Extraurbano','0-100km/h','Cilindrada','Cilindros','Parmaximo']
ColumnsNormmaxmin=["Ano",'Potencia','Kilometros']

for col in ColumnsNorm:
    cl_f.normalization(df1,col)

for col in ColumnsNormmaxmin:
    cl_f.normalizationmaxmin(df1,col)


###Weighting features
df1["Kilometros"]=df1["Kilometros"]*n_km
df1["Ano"]=df1["Ano"]*n_ano
df1["Potencia"]=df1["Potencia"]*n_pot

print(df1.shape)
dfcols=[col for col in df1.colums]

df1.to_csv('./output/cars_clean2.csv', index=False)