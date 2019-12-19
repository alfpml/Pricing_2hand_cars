from bottle import route, run, get, post, request
from bson.json_util import dumps
import json
import dns
import requests
import src.mongoconnect as mf
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

@route("/")
def index():
    return {'Car pricing app'}

@get("/{name}/car/price")
def getPrice(name):
    """Get messages from a given chat"""
    return dumps(coll.find({'idChat':int(chat_id)}))

@post('/car/create')
def inputCar():
    """Input car detils"""
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

    input_car={
    'Precio':9999,
    'Brand':InputBrand,
    'Model':InputModel,
    'Ano': Ano, 
    'Potencia':Potencia,
    'Kilometros':Kilometros,
    'Puertas':5,
    'Cambio':Cambio, 
    ##'Longitud':420.0,
    ##'Velocidad':207.0,
    'Cilindros':Cilindros,
    'Marchas':Marchas,
    'Traccion':Traccion,
    'Combustible':Combustible,
    ##'Carroceria':"Berlina",
    'inputcar':1
    }
    
    coll.insert_one(input_car)
    return f"{name}'s car added"

db, coll = mc.connectCollection('carpricing','cars')
run(host="0.0.0.0", port=8080, debug=True)
