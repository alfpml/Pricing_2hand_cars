# Importing libraries:
import parameters as prm
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import clean
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import confusion_matrix, accuracy_score

from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_classification
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression

from math import sqrt

##dfm=pd.DataFrame(pd.read_csv("./output/cars_clean2.csv"))
##print(dfm.shape)

##Input parameters (columns to include and clf model)

def regression(dfm,dfcar,Xcolumns,modelo):
    ##clf = RandomForestRegressor(n_estimators=250)
    clf = RandomForestRegressor(n_estimators=250)
    X = dfm[Xcolumns]
    y = dfm['Precio']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

    clf.fit(X_train, y_train)
    y_predr = clf.predict(X_test)

    r2_s=r2_score(y_test, y_predr)
    rmse = sqrt(mean_squared_error(y_test, y_predr))
    print("r2_score is: {}. RMSE is: {}".format(r2_s,rmse))

    Xcar = dfcar[Xcolumns]
    y_car=clf.predict(Xcar)
    return "Precio de Venta para tu {} es: {}€".format(modelo,y_car[0])
