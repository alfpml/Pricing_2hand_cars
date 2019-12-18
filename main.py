import src.clean_functions as cl_f
import parameters as prm
import mongoconnect as mc
import clean as cln
import model as mdl
import pandas as pd
import numpy as np
import json
import re
from pymongo import MongoClient
import getpass

#Connect to DB
client = MongoClient(mc.connection)
db, coll = mc.connectCollection('carpricing','cars')

query = {'Brand':"Audi"}
Brand_audi = coll.find(query)
Brand_audi2=pd.DataFrame(Brand_audi)
print("lenghth df is {}".format(len(Brand_audi2)))
Brand_normalized=cln.cleaningfunction(Brand_audi2)
print("lenghth dfn is {}".format(len(Brand_normalized)))

ycolumns=[col for col in Brand_normalized.columns]
lc=len(ycolumns)-1
Xcolumns=ycolumns[-lc:]
print(ycolumns)
##Xcolumns=['Ano', 'Potencia', 'Kilometros', 'Puertas', 'Cambio', 'Longitud', 'Velocidad', 'Cmixto', 'Cilindros', 'Marchas', 'Traccion', 'Combustible_Diesel', 'Combustible_Gasolina', 'Model_Audi A1', 'Model_Audi A3', 'Model_Audi A4', 'Model_Audi A5', 'Model_Audi A6','Carroceria_Berlina']
print(Xcolumns)
mdl.regression(Brand_normalized,Xcolumns)
