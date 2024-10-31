
### Logistic Regression 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
moneyball = pd.read_csv(r"C:\Users\LENOVO\Downloads\baseball.csv")
moneyball_new = pd.read_csv(r"C:\Users\LENOVO\Downloads\baseball.csv")
moneyball_new_1=moneyball_new[(moneyball_new['Playoffs'] == 1)]

moneyball_new_1=moneyball_new_1.dropna()

X=moneyball[['RD']].values.reshape(-1,1)
y=moneyball['Playoffs'].values

logreg=LogisticRegression()
logreg.fit(X,y)

rs=223
playoffs_probability=logreg.predict_proba([[rs]])[:,1]

print("Probability of winning is",playoffs_probability)

