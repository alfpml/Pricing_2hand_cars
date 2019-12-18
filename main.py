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
##query = {'Brand':ci.InputBrand}
##Brand_q = coll.find(query)

##2. Import data
Brand_q = coll.find()
dfBrand=pd.DataFrame(Brand_q)
dfBrand=cln.dropcolumns(dfBrand,prm.columnsdrop)
dfBrand['inputcar']=0
print("Dataset imported from Mongo")

dfBrand = dfBrand.append(ci.input_car, ignore_index=True)
print(dfBrand[dfBrand['inputcar']==1])
print("Input car added to df")

car_columns=cln.listcolumns(dfBrand)
print("car columns")
print(car_columns)

##3. Cleaning Dataset
dfBrand_N=cln.cleaningfunction(dfBrand)
##print("lenghth dfBrand_N is {}".format(len(dfBrand_N)))
print("df is now clean and normalized")

##4. Defining Train test
df_Train=dfBrand_N[dfBrand_N['inputcar']==0]
print("lenghth of Train df is {}".format(len(df_Train)))
df_Car=dfBrand_N[dfBrand_N['inputcar']==1]
print("lenghth of Car df is {}".format(len(df_Car)))
Xcolumns=cln.listcolumns(df_Train)
##print("Xcolumns are:")
##print(Xcolumns)
print("X columns defined")

###5. Performing Regression
mdl.regression(dfBrand_N,df_Car,Xcolumns)
