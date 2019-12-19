from bottle import route, run, get, post, request
from bson.json_util import dumps
import json
import dns
import requests
import src.mongoconnect as mf
import src.clean_functions as cl_f
import parameters as prm
import clean as cln
import model as mdl
import car_input as ci
import pandas as pd
import numpy as np
import re
from pymongo import MongoClient
import getpass

@route("/")
def index():
    return {'Car pricing app'}

@get("/model")
def modelstats():
    """Returns model statistics"""
    Model = str(request.forms.get("Model"))
    ##query = {'Brand':Brand}
    query = {'Carroceria':"Berlina"}
    Model_q = coll.find(query)

    dfModel=pd.DataFrame(Model_q)
    ##dfModel=cln.dropcolumns(dfModel,prm.columnsdrop)
    print("Dataset imported from Mongo")
    return len(dfModel)

@get("/carprice")
def getPrice():
    """Returns car price"""

    """1. Input car details"""
    Brand = str(request.forms.get("Brand"))
    Model = str(request.forms.get("Model"))
    Year = str(request.forms.get("Year"))
    Potencia = float(request.forms.get("Potencia"))
    Kilometros = float(request.forms.get("Kilometros"))
    Puertas = float(request.forms.get("Puertas"))
    Cambio = str(request.forms.get("Cambio"))
    Cilindros = float(request.forms.get("Cilindros"))
    Marchas = float(request.forms.get("Marchas"))
    Traccion = str(request.forms.get("Traccion"))
    Combustible = str(request.forms.get("Combustible"))

    """2. Import data"""
    query = {'Brand':Brand}
    Brand_q = coll.find(query)
    ##Brand_q = coll.find()
    dfBrand=pd.DataFrame(Brand_q)
    dfBrand=cln.dropcolumns(dfBrand,prm.columnsdrop)
    dfBrand['inputcar']=0
    print("Dataset imported from Mongo")
    ##print(len(dfBrand))

    """3. Creating dict for df"""
    data={
    'Brand':Brand,
    'Model':Model,
    'Ano': Year, 
    'Potencia':Potencia,
    'Kilometros':Kilometros,
    'Puertas':Puertas,
    'Cambio':Cambio, 
    'Cilindros':Cilindros,
    'Marchas':Marchas,
    'Traccion':Traccion,
    'Combustible':Combustible,
    'inputcar':1,
    'Precio':9999
    }
    ##print(data)
    """4. Appending to DataFrame"""
    dfBrand = dfBrand.append(data, ignore_index=True)
    ##dfBrand.reset_index(inplace=True)
    dfBrand = dfBrand.drop('_id', 1)
    ##print(dfBrand[dfBrand['inputcar']==1])
    ##print(len(dfBrand))
    ##print("Input car added to df")
    car_columns=cln.listcolumns(dfBrand)

    ##3. Cleaning Dataset
    dfBrand_N=cln.cleaningfunction(dfBrand)

    ##4. Defining Train test
    df_Train=dfBrand_N[dfBrand_N['inputcar']==0]
    df_Car=dfBrand_N[dfBrand_N['inputcar']==1]
    Xcolumns=cln.listcolumns(df_Train)

    ###5. Performing Regression
    price=mdl.regression(df_Train,df_Car,Xcolumns)
    dfBrand[dfBrand['inputcar']!=1]
    return "Precio recomendado para tu {}: {}€".format(Model,price)


db, coll = mf.connectCollection('carpricing','cars')
run(host="0.0.0.0", port=8080, debug=True)
