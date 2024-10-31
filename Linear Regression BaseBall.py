# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 21:03:46 2024

@author: LENOVO
"""
# Importing the Libraries 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Importing the Baseball Dataset
moneyball_new = pd.read_csv(r"C:\Users\LENOVO\Downloads\baseball.csv")

# Filtering out the teams qualified for Playoffs
moneyball_new_1=moneyball_new[(moneyball_new['Playoffs'] == 1)]

# Removing the missing values(if any)
moneyball_new_1=moneyball_new_1.dropna()
# Calculating the average runscore, run difference & wins for the teams qualified for the Playoffs
avg_wins = moneyball_new_1.W.mean()
avg_rs = moneyball_new_1.RS.mean()
avg_rd=moneyball_new_1.RD.mean()

# Defining the dependent variables On Base Percentage(OBP),Slugging Rate(SLG) & Batting Average(BA)
# Independent variable(y) as Run Score(RS) & fitting the linear regression model
x = moneyball_new_1[['OBP','SLG','BA']].values
y = moneyball_new_1[['RS']].values
# Calling our model object.
RS_model_1 = LinearRegression()
# Fitting the model.
RS_model_1.fit(x,y)
# Printing model intercept and coefficients.
print(RS_model_1.intercept_)
print(RS_model_1.coef_)

# Using above model without Batting Average(BA) because of multi-colinearity 
x = moneyball_new_1[['OBP','SLG']].values
y = moneyball_new_1[['RS']].values
# Calling our model object.
RS_model = LinearRegression()
# Fitting the model.
RS_model.fit(x,y)
# Printing model intercept and coefficients.
print(RS_model.intercept_)
print(RS_model.coef_)

# Extracting our variables from the dataframe.
# Defining the dependent variables Oponents's On-Base Percentage(OOBP) & Oponent's Slugging Rate(OSLG)
# Independent variable(y) as Run Allowed(RA) & fitting the linear regression model
x = moneyball_new_1[['OOBP','OSLG']].values
y = moneyball_new_1[['RA']].values
# Calling our model object.
RA_model = LinearRegression()
# Fitting the model.
RA_model.fit(x,y)
# Printing model intercept and coefficients.
print(RA_model.intercept_)
print(RA_model.coef_)


# Extracting our variables from the dataframe.
# Defining the dependent variables as Run Difference(RD)
# Independent variable(y) as Wins (W) & fitting the linear regression model
x = moneyball_new_1[['RD']].values
y = moneyball_new_1[['W']].values
# Calling our model object.
W_model = LinearRegression()
# Fitting the model.
W_model.fit(x,y)
# Printing model intercept and coefficients.
print(W_model.intercept_)#85.60
print(W_model.coef_)#0.079
#0.345,0.439,0.264




moneyball_OAK= moneyball_new_1[moneyball_new_1['Team'] == 'OAK']
moneyball_OAK["OBP"].mean()#0.328
moneyball_OAK["SLG"].mean()#0.392
moneyball_OAK["BA"].mean()#0.2542
moneyball_OAK["OOBP"].mean()#0.332
moneyball_OAK["OSLG"].mean()#0.418

moneyball_OAK= moneyball_new_1[moneyball_new_1['Team'] == 'OAK']
moneyball_OAK["OBP"].mean()#0.336
moneyball_OAK["SLG"].mean()#0.399
moneyball_OAK["BA"].mean()#0.258
moneyball_OAK["OOBP"].mean()#0.331
moneyball_OAK["OSLG"].mean()#0.416


RS_model_1.predict([[0.336,0.399,0.258]])#757

# Predictions for runs allowed.
RA_model.predict([[0.331,0.416]])#654

# Prediction for runs scored .
RS_model.predict([[0.336,0.399]])#757


# Values are taken for the year 2001 only
#RS_model_1.predict([[0.328,0.392,0.2542]])#725

# Predictions for runs allowed.
#RA_model.predict([[0.332,0.418]])#655

# Prediction for runs scored .
#RS_model.predict([[0.328,0.392]])#725

# Values are taken for the year 2001 only
# Prediction for runs scored with BA.
RS_model_1.predict([[0.345,0.429,0.264]])#827

# Predictions for runs allowed.
RA_model.predict([[0.308,0.38]])#604

# Prediction for runs scored .
RS_model.predict([[0.345,0.429]])#827

# RS = 827 , RA= 604 
# RD= 223

W_model.predict([[223]]) # 103 

# Our model RS = 827, RA= 604, Wins= 103 
# Actual model RS = 800, RA= 654, Wins= 103 
# Podesta's model RS= 814, RA= 645, Wins= 99
