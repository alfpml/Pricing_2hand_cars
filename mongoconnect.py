from pymongo import MongoClient
import getpass
import json

#Get Password
password = getpass.getpass("Insert your AtlasMongoDB admin_1019 password: ")
connection = "mongodb+srv://alfpml:{}@cluster0-c3fib.mongodb.net/test?retryWrites=true&w=majority".format(password)

#Connect to DB
client = MongoClient(connection)
def connectCollection(database, collection):
    db = client[database]
    coll = db[collection]
    return db, coll

db, coll = connectCollection('pricingcars','cars_all')

with open('./input/cars_all.json') as f:
    cars_all_json = json.load(f)
coll.insert_many(cars_all_json)
