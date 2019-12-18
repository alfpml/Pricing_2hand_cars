import pandas as pd
import numpy as np
import json
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns
import re

##Columns to drop
##def dropcolumns(df,columns):
##    df=df.drop(columns, axis=1, inplace=True)
##    return df

##Replace functions
def columnreplace(df,column,string):
    df[column]=df[column].str.replace(string,'')
    df[column]=df[column].str.replace(".",'')
    df[column]=df[column].astype('float')
    return df

def columnreplace2(df,column,string):
    df[column]=df[column].str.replace(string,'')
    df[column]=df[column].str.replace(",",'')
    df[column]=df[column].astype('float')/10
    return df

def columndigits(df,column):
    df[column]=[re.findall(r'\d+',str(i))[0] for i in df[column]]
    return df

def columnlist(df,column):
    ##df[column]=df[column].str.replace("'",'')
    df[column]=df[column].str.replace("[",'')
    df[column]=df[column].str.replace("]",'')
    df[column]=[i.split(",") for i in df[column]]
    return df[column]

def removevalues(df1,column,value):
    df1.column
    indexNames = df1[ df1[column] == value].index
    df1.drop(indexNames , inplace=True)
    return df1

##column specifc functions to convert to numerical
def cambio(cambio):
    if (cambio.lower()).find('secuencial')>-1:
        return 1
    if (cambio.lower()).find('automática')>-1:
        return 0.75
    else:
        return 0

def traccion(traccion):
    if (traccion.lower()).find('total')>-1:
        return 1
    if (traccion.lower()).find('trasera')>-1:
        return 0.5
    else:
        return 0

def puertas(puertas):
    if puertas>3:
        return 1
    else:
        return 0


def marchas(marchas):
    if float(marchas)>=6:
        return 1
    else:
        return 0

##Removing low frequency columns
def RemoveLowFreq(df,column,threshold):
    value_counts = df[column].value_counts() # Specific column 
    to_remove = value_counts[value_counts <= threshold].index
    df[column].replace(to_remove, np.nan, inplace=True)
    df=df.dropna()
    return df


def columnBining(df,column,bins):
    newcolumn=column+"_bin"
    labels=[float((i+1)/bins)for i in range(bins)]
    df[newcolumn]=pd.qcut(df[column],bins,labels=labels)
    df[newcolumn]=df[newcolumn].astype('float')
    return df[newcolumn]

##Normalization functions
def normalization(df,column):
    df[column]=(df[column]-np.mean(df[column]))/np.std(df[column])
    return df[column]

def normalizationmaxmin(df,column):
    df[column]=(df[column]-(df[column]).min())/((df[column]).max()-(df[column]).min())
    return df[column]