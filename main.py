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

#Connect to DB
client = MongoClient(mc.connection)
db, coll = mc.connectCollection('carpricing','cars')

##query = {'Brand':ci.InputBrand}
##Brand_q = coll.find(query)

Brand_q = coll.find()
dfBrand=pd.DataFrame(Brand_q)
dfBrand=cln.dropcolumns(dfBrand,prm.columnsdrop)
dfBrand['inputcar']=0
car_columns=cln.listcolumns(dfBrand)
print(car_columns)

##print("lenghth df is {}".format(len(Brand_audi2)))
dfBrand_N=cln.cleaningfunction(dfBrand)
print("lenghth dfBrand_N is {}".format(len(dfBrand_N)))

Xcolumns=cln.listcolumns(dfBrand_N)
print("Xcolumns are:")
print(Xcolumns)

##ycolumns=[col for col in dfBrand_N.columns]
##lc=len(ycolumns)-1
##Xcolumns=ycolumns[-lc:]
##print(ycolumns)
##Xcolumns=['Ano', 'Potencia', 'Kilometros', 'Puertas', 'Cambio', 'Longitud', 'Velocidad', 'Cmixto', 'Cilindros', 'Marchas', 'Traccion', 'Combustible_Diesel', 'Combustible_Gasolina', 'Model_Audi A1', 'Model_Audi A3', 'Model_Audi A4', 'Model_Audi A5', 'Model_Audi A6','Carroceria_Berlina']
##print(Xcolumns)
mdl.regression(dfBrand_N,Xcolumns)
