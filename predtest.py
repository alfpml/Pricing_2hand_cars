import pandas as pd

cardict = {
'Ano':[5],
'Potencia':[150],
'Kilometros':[100000],
'Puertas':[1],
'Cambio':[0],
'Cilindros':[4],
'Marchas':[5],
'Traccion':[0],
'Longitud':[446],
'Plazas':[1],
'Combustible_Diesel':[1],
'Combustible_Gasolina':[0],
'Brand_Audi':[1],
'Brand_Bmw':[0],
'Brand_Citroen':[0],
'Brand_Fiat':[0],
'Brand_Ford':[0],
'Brand_Hyundai':[0],
'Brand_Kia':[0],
'Brand_Land Rover':[0],
'Brand_Mazda':[0],
'Brand_Mercedes':[0],
'Brand_Mini':[0],
'Brand_Nissan':[0],
'Brand_Opel':[0],
'Brand_Peugeot':[0],
'Brand_Renault':[0],
'Brand_Seat':[0],
'Brand_Skoda':[0],
'Brand_Toyota':[0],
'Brand_Volkswagen':[0],
'Carroceria_Berlina':[1],
'Carroceria_Monovolumen':[0],
'Carroceria_Stationwagon':[0],
'Carroceria_Todo Terreno':[0]
}

cols=list(cardict.keys())
cartest = pd.DataFrame.from_dict(cardict)

print(cartest)