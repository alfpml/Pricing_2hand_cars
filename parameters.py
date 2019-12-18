##Defining cleaning parameters
## params to clean km (max/min)
kmmax=300000
kmmin=2000

## params to clean año column (max/min)
anmax=15
anmin=1

## params to clean precio column (max/min)
prcmax=100000
prcmin=500

## Params low frequency
lf_model=200
lf_brand=400
lf_carro=400

##Bining params
ColumnsBin=['Ano','Kilometros','Potencia']
Bins={'Ano':5,
      'Kilometros':8,
      'Potencia':8
     }

##weighted params
n_km=1.0
n_ano=1.0
n_pot=1.0

##Normalization
columnsdrop=['Emisiones','Peso','0-100km/h','Cilindrada','Transmision','Parmaximo','Curbano','Extraurbano','Cmixto','Plazas']
ColumnsNorm=["Ano",'Potencia','Kilometros','Longitud','Cilindros','Velocidad']
ColumnsNormmaxmin=[]

##Regression parameters
##clf = RandomForestRegressor(n_estimators=250)
##Xcolumns = ["Ano",'Potencia','Kilometros','Longitud','Cilindros','Velocidad',]


##mongo query
query={'Brand':'Bmw'},{'Model': 'Bmw Serie 1'}