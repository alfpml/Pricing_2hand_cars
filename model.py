# Importing libraries:
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import predtest
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

dfm=pd.DataFrame(pd.read_csv("./output/cars_clean2.csv"))
print(dfm.shape)

##Input parameters (columns to include and clf model)

columns=clean.dfcols

clf = RandomForestRegressor(n_estimators=250)

X = dfm[columns]
y = dfm['Precio']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

clf.fit(X_train, y_train)
y_predr = clf.predict(X_test)

r2_score=r2_score(y_test, y_predr)
print("r2_score is: {}".format(r2_score))
rmse = sqrt(mean_squared_error(y_test, y_predr))
print("rmse is: {}".format(rmse))

##y_test=clf.predict(predtest.cartest)
##print(y_test)