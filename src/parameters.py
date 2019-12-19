##Defining cleaning parameters
## params to clean km (max/min)
kmmax=300000
kmmin=2000

## params to clean año column (max/min)
anmax=18
anmin=1

## params to clean precio column (max/min)
prcmax=100000
prcmin=500

## Params low frequency
lf_model=100
lf_brand=200
lf_carro=500

##Bining params
ColumnsBin=['Ano','Kilometros','Potencia']
Bins={'Ano':8,
      'Kilometros':8,
      'Potencia':8
     }

##weighted params
n_km=1.0
n_ano=1.0
n_pot=1.0

##Normalization
columnsdrop=['Emisiones','Peso','0-100km/h','Cilindrada','Transmision','Parmaximo','Curbano','Extraurbano','Cmixto','Plazas','Longitud','Velocidad','Carroceria']
ColumnsNorm=["Ano",'Potencia','Kilometros','Cilindros']
ColumnsNormmaxmin=[]

##Regression parameters
##clf = RandomForestRegressor(n_estimators=250)
##Xcolumns = ["Ano",'Potencia','Kilometros','Longitud','Cilindros','Velocidad',]