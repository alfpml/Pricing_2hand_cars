import src.clean_functions as cl_f
import pandas as pd
import numpy as np
import json
import re
import parameters as prm


###Bringing up all CSVs from scraping
##df1 = mc.Brand_audi
##print(df1.shape)

def cleaningfunction(df1):
    ##Casting columns
    df1.drop(prm.columnsdrop, axis=1, inplace=True)
    df1=df1.dropna()
    df1['Potencia']=df1['Potencia'].dropna().astype('float', errors='ignore')
    df1['Cilindros']=df1['Cilindros'].dropna().astype('float', errors='ignore')
    df1['Puertas']=df1['Puertas'].dropna().astype('float', errors='ignore')
    df1['Marchas']=df1['Marchas'].dropna().astype('float', errors='ignore')
    df1['Kilometros']=df1['Kilometros'].dropna().astype('float', errors='ignore')
    df1['Precio']=df1['Precio'].dropna().astype('float', errors='ignore')
    df1['Longitud']=df1['Longitud'].dropna().astype('float', errors='ignore')
    df1['Velocidad']=df1['Velocidad'].dropna().astype('float', errors='ignore')
    df1['Cmixto']=df1['Cmixto'].dropna().astype('float', errors='ignore')
    print("casting")

    ##Encoding categorical variables
    df1['Cambio']=[cl_f.cambio(i) for i in df1['Cambio']]
    df1['Traccion']=[cl_f.traccion(i) for i in df1['Traccion']]
    df1['Puertas']=[cl_f.puertas(i) for i in df1['Puertas']]
    df1['Marchas']=[cl_f.marchas(i) for i in df1['Marchas']]
    print("encoding categorical")


    ##Encoding column año
    df1['Ano'] = df1['Ano'].str[-4:]
    df1=df1.dropna()
    df1['Ano'] = df1['Ano'].dropna().astype('float', errors='ignore')
    df1['Ano']=2019-df1['Ano']
    print("encoding año")

    ##Dropping ouliers rows in km
    df1 = df1[df1["Kilometros"]<=prm.kmmax]
    df1 = df1[df1["Kilometros"]>=prm.kmmin]
    print("outliers km")

    ##Dropping ouliers rows for año
    df1 = df1[df1["Ano"]<=prm.anmax]
    df1 = df1[df1["Ano"]>=prm.anmin]
    print("outliers year")

    ##Dropping ouliers rows for precio
    df1 = df1[df1["Precio"]<=prm.prcmax]
    df1 = df1[df1["Precio"]>=prm.prcmin]
    print("outliers precio")

    ##df1=df1.dropna()
    df1 = df1[df1["Longitud"] !=0]
    df1 = df1[df1["Velocidad"] !=0]
    df1 = df1[df1['Cmixto'] !=0]
    print("removing zeros")
    


    ##removing low frequency Brands and models
    df1=cl_f.RemoveLowFreq(df1,"Model",prm.lf_model)
    df1=cl_f.RemoveLowFreq(df1,"Brand",prm.lf_brand)
    df1=cl_f.RemoveLowFreq(df1,"Carroceria",prm.lf_carro)
    print("removing low freq")


    ##df1.to_csv('./output/cars_clean_1.csv', index=False)

    ##Bining of longitud/peso to try to adjust for brands distinct models
    ##for i in prm.ColumnsBin:
    ##    cl_f.columnBining(df1,i,prm.Bins[i])

    ##Encoding through get_dummies
    df1 = pd.get_dummies(df1, columns=['Combustible'])
    df1 = pd.get_dummies(df1, columns=['Brand'])
    df1 = pd.get_dummies(df1, columns=['Model'])
    df1 = pd.get_dummies(df1, columns=['Carroceria'])
    print("get dummies")


    for col in prm.ColumnsNorm:
        cl_f.normalization(df1,col)
    print("normalization")

    ##for col in prm.ColumnsNormmaxmin:
    ##    cl_f.normalizationmaxmin(df1,col)


    ###Weighting features
    ##df1["Kilometros"]=df1["Kilometros"]*prm.n_km
    ##df1["Ano"]=df1["Ano"]*n_ano
    ##df1["Potencia"]=df1["Potencia"]*prm.n_pot

    ##print(df1.shape)
    ##dfcols=[col for col in df1.colums]
    ##df1.to_csv('./output/cars_clean2.csv', index=False)
    print("final lenghth is {}".format(len(df1)))
    return pd.DataFrame(df1)