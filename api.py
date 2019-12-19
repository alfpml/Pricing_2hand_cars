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
    query = {'Model':Model}
    Model_q = coll.find(query)

    dfModel=pd.DataFrame(Model_q)
    dfModel=cln.dropcolumns(dfModel,prm.columnsdrop)
    print("Dataset imported from Mongo")
    return len(dfModel)

@get("/carprice")
def getPrice():
    """Returns car price"""

    """1. Import data"""
    query = {'Carroceria':'Berlina'}
    Brand_q = coll.find(query)
    ##Brand_q = coll.find()
    dfBrand=pd.DataFrame(Brand_q)
    dfBrand=cln.dropcolumns(dfBrand,prm.columnsdrop)
    dfBrand['inputcar']=0
    print("Dataset imported from Mongo")

    """2. Input car details"""
    Name = str(request.forms.get("Name"))
    Brand = str(request.forms.get("Brand"))
    Model = str(request.forms.get("Model"))
    Ano = str(request.forms.get("Ano"))
    Potencia = str(request.forms.get("Potencia"))
    Kilometros = str(request.forms.get("Kilometros"))
    Puertas = str(request.forms.get("Puertas"))
    Cambio = str(request.forms.get("Cambio"))
    Cilindros = str(request.forms.get("Cilindros"))
    Marchas = str(request.forms.get("Marchas"))
    Traccion = str(request.forms.get("Traccion"))
    Combustible = str(request.forms.get("Combustible"))

    """3. Creating dict for df"""
    data={
    'Brand':Brand,
    'Model':Model,
    'Ano': Ano, 
    'Potencia':Potencia,
    'Kilometros':Kilometros,
    'Puertas':Puertas,
    'Cambio':Cambio, 
    'Cilindros':Cilindros,
    'Marchas':Marchas,
    'Traccion':Traccion,
    'Combustible':Combustible,
    'inputcar':name
    }

    """4. Appending to DataFrame"""
    dfBrand = dfBrand.append(ci.input_car, ignore_index=True)
    ##dfBrand.reset_index(inplace=True)
    dfBrand = dfBrand.drop('_id', 1)
    ##print(dfBrand[dfBrand['inputcar']==1])
    print("Input car added to df")
    ##car_columns=cln.listcolumns(dfBrand)

    ##3. Cleaning Dataset
    dfBrand_N=cln.cleaningfunction(dfBrand)

    ##4. Defining Train test
    df_Train=dfBrand_N[dfBrand_N['inputcar']==0]
    df_Car=dfBrand_N[dfBrand_N['inputcar']==name]
    Xcolumns=cln.listcolumns(df_Train)

    ###5. Performing Regression
    price=mdl.regression(df_Train,df_Car,Xcolumns,ci.InputModel)
    return price


db, coll = mf.connectCollection('carpricing','cars')
run(host="0.0.0.0", port=8080, debug=True)
