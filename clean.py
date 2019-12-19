import src.parameters as prm
import src.clean_functions as cl_f
import pandas as pd
import numpy as np
import json
import re


###Bringing up all CSVs from scraping
##df1 = mc.Brand_audi
##print(df1.shape)

def listcolumns(df):
    df = df.drop('Precio', 1)
    list_col=[col for col in df.columns]
    list_col_len=len(list_col)-1
    list_col=list_col[-list_col_len:]
    return list_col

def dropcolumns(df,columnsdrop):
    df.drop(columnsdrop, axis=1, inplace=True)
    df=df.dropna()
    return df

def cleaningfunction(df1):
    ##Casting columns
    df1=df1.dropna()

    df1['Potencia']=[pd.to_numeric(x, errors='coerce',downcast='float') for x in df1['Potencia']]
    df1['Cilindros']=[pd.to_numeric(x, errors='coerce',downcast='float') for x in df1['Cilindros']]
    df1['Puertas']=[pd.to_numeric(x, errors='coerce',downcast='float') for x in df1['Puertas']]
    df1['Marchas']=[pd.to_numeric(x, errors='coerce',downcast='float') for x in df1['Marchas']]

    df1['Kilometros']=[pd.to_numeric(x, errors='coerce',downcast='float') for x in df1['Kilometros']]
    df1['Precio']=[pd.to_numeric(x, errors='coerce',downcast='float') for x in df1['Precio']]
    
    df1=df1.dropna()
    df1.reset_index(inplace=True)
    ##print("casting to numeric")
    ##print(df1[df1['inputcar']==1])

    ##Encoding categorical variables
    df1['Cambio']=[cl_f.cambio(i) for i in df1['Cambio']]
    df1['Traccion']=[cl_f.traccion(i) for i in df1['Traccion']]
    df1['Puertas']=[cl_f.puertas(i) for i in df1['Puertas']]
    df1['Marchas']=[cl_f.marchas(i) for i in df1['Marchas']]
    ##print("encoding categorical")
    ##print(df1[df1['inputcar']==1])

    ##Encoding column año
    df1['Ano'] = df1['Ano'].str[-4:]
    df1=df1.dropna()
    df1['Ano']=[pd.to_numeric(x, errors='coerce',downcast='float') for x in df1['Ano']]
    ##df1['Ano'] = df1['Ano'].astype('float', errors='ignore')
    df1['Ano']=2019-df1['Ano']
    ##print("encoding año")
    ##print(df1[df1['inputcar']==1])

    ##Dropping ouliers rows in km
    df1 = df1[df1["Kilometros"]<=prm.kmmax]
    df1 = df1[df1["Kilometros"]>=prm.kmmin]
    print("outliers km")

    ##Dropping ouliers rows for año
    df1 = df1[df1["Ano"]<=prm.anmax]
    df1 = df1[df1["Ano"]>=prm.anmin]
    ##print("outliers year")
    ##print(df1[df1['inputcar']==1])

    ##Dropping ouliers rows for precio
    df1 = df1[df1["Precio"]<=prm.prcmax]
    df1 = df1[df1["Precio"]>=prm.prcmin]
    ##print("outliers precio")
    ##print(df1[df1['inputcar']==1])

    df1=df1.dropna()
    ##df1 = df1[df1["Longitud"] !=0]
    ##df1 = df1[df1["Velocidad"] !=0]
    ##df1 = df1[df1['Cmixto'] !=0]
    ##print("removing zeros")
    ##print(df1[df1['inputcar']==1])


    ##removing low frequency Brands and models
    df1=cl_f.RemoveLowFreq(df1,"Model",prm.lf_model)
    df1=cl_f.RemoveLowFreq(df1,"Brand",prm.lf_brand)
    ##df1=cl_f.RemoveLowFreq(df1,"Carroceria",prm.lf_carro)
    ##print("removing low freq")
    ##print(df1[df1['inputcar']==1])


    ##df1.to_csv('./output/cars_clean_1.csv', index=False)

    ##Bining of longitud/peso to try to adjust for brands distinct models
    ##for i in prm.ColumnsBin:
    ##    cl_f.columnBining(df1,i,prm.Bins[i])

    ##Encoding through get_dummies
    df1 = pd.get_dummies(df1, columns=['Combustible'])
    df1 = pd.get_dummies(df1, columns=['Brand'])
    df1 = pd.get_dummies(df1, columns=['Model'])
    ##df1 = pd.get_dummies(df1, columns=['Carroceria'])
    ##print("get dummies")


    for col in prm.ColumnsNorm:
        cl_f.normalization(df1,col)
    ##print("normalization")

    ##for col in prm.ColumnsNormmaxmin:
    ##    cl_f.normalizationmaxmin(df1,col)


    ###Weighting features
    df1["Kilometros"]=df1["Kilometros"]*prm.n_km
    df1["Ano"]=df1["Ano"]*prm.n_ano
    df1["Potencia"]=df1["Potencia"]*prm.n_pot

    ##print(df1.shape)
    ##dfcols=[col for col in df1.colums]
    ##df1.to_csv('./output/cars_clean2.csv', index=False)
    ##print("final lenghth is {}".format(len(df1)))
    return pd.DataFrame(df1)