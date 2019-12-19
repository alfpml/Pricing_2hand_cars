import src.clean_functions as cl_f
import parameters as prm
import mongoconnect as mc
import clean as cln
import model as mdl
import car_input as ci

import pandas as pd
import numpy as np
import json
import re
from pymongo import MongoClient
import getpass

##1. Connect to DB
client = MongoClient(mc.connection)
db, coll = mc.connectCollection('carpricing','cars')
print("connection ready")

##2. Import data
query = {'Carroceria':'Berlina'}
Brand_q = coll.find(query)
##Brand_q = coll.find()
dfBrand=pd.DataFrame(Brand_q)
dfBrand=cln.dropcolumns(dfBrand,prm.columnsdrop)
dfBrand['inputcar']=0
print("Dataset imported from Mongo")

dfBrand = dfBrand.append(ci.input_car, ignore_index=True)
##dfBrand.reset_index(inplace=True)
dfBrand = dfBrand.drop('_id', 1)
print(dfBrand[dfBrand['inputcar']==1])
print("Input car added to df")

car_columns=cln.listcolumns(dfBrand)

##3. Cleaning Dataset
dfBrand_N=cln.cleaningfunction(dfBrand)

##4. Defining Train test
df_Train=dfBrand_N[dfBrand_N['inputcar']==0]
df_Car=dfBrand_N[dfBrand_N['inputcar']==1]
Xcolumns=cln.listcolumns(df_Train)

###5. Performing Regression
print(mdl.regression(df_Train,df_Car,Xcolumns,ci.InputModel))
