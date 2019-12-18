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
lf_model=100
lf_brand=200
lf_carro=500

##Bining params
ColumnsBin=['Longitud','Kilometros','Peso','Potencia']
Bins={'Longitud':10,
      'Kilometros':10,
      'Peso':8,
      'Potencia':6
     }

##weighted params
n_km=1
n_ano=1
n_pot=1.2

##Normalization
columnsdrop=['Emisiones','Peso','0-100km/h','Cilindrada','Transmision','Parmaximo','Curbano','Extraurbano','Plazas']
ColumnsNorm=["Ano",'Potencia','Kilometros','Longitud','Cilindros','Velocidad']
ColumnsNormmaxmin=[]

##Bining of longitud/peso to try to adjust for brands distinct models
ColumnsBin=['Longitud','Kilometros','Peso','Potencia','Cambio','Traccion','Puertas','Marchas']
Bins={'Longitud':8,
    'Kilometros':8,
    'Peso':8,
    'Potencia':8
    }

##Regression parameters
##clf = RandomForestRegressor(n_estimators=250)
##Xcolumns = ["Ano",'Potencia','Kilometros','Longitud','Cilindros','Velocidad',]