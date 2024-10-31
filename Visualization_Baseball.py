### Visualizations

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
moneyball = pd.read_csv(r"C:\Users\LENOVO\Downloads\baseball.csv")
moneyball_new_1=moneyball[(moneyball['Playoffs'] == 1)]
# From model, Actual runs required to qualify for playoffs
plt.figure(figsize=(10,8))
plt.scatter(x=moneyball.W, y=moneyball.RS, c="green",label="Playoff Teams (Moneyball)")  
plt.scatter(x=moneyball.W[moneyball['Playoffs'] == False], y=moneyball.RS[moneyball['Playoffs'] == False], c="red", label="Non-Playoff Teams (Moneyball)",alpha=0.5)
plt.scatter(x=moneyball.W[moneyball['Team'] == 'OAK'], y=moneyball.RS[moneyball['Team'] == 'OAK'], c="yellow",label="Oakland Athletics")
plt.xlabel("Wins")
plt.ylabel("Runs Scored")
plt.axvline(x = 103,c='black')
#plt.axhline(y = 800,c='black')
plt.axhline(y = 827,c='black')
plt.legend()
plt.title("RS(827) required by OA's to win 103 games & qualify for playoffs")

# From model, Minimum runs required to qualify for playoffs
plt.figure(figsize=(10,8))
plt.scatter(x=moneyball.W, y=moneyball.RS, c="green",label="Playoff Teams (Moneyball)")  
plt.scatter(x=moneyball.W[moneyball['Playoffs'] == False], y=moneyball.RS[moneyball['Playoffs'] == False], c="red", label="Non-Playoff Teams (Moneyball)",alpha=0.5)
plt.scatter(x=moneyball.W[moneyball['Team'] == 'OAK'], y=moneyball.RS[moneyball['Team'] == 'OAK'], c="yellow",label="Oakland Athletics")
plt.xlabel("Wins")
plt.ylabel("Runs Scored")
plt.axvline(x = 103,c='black')
#plt.axhline(y = 800,c='black')
plt.axhline(y = 673,c='red')
plt.axhline(y = 827,c='black')
plt.legend()
plt.title("Minimum RS(673) required by OA's to win 103 games & qualify for playoffs")


x = np.array(moneyball.RD)
y = np.array(moneyball.W)
# Deriving slope,intercept values
slope, intercept = np.polyfit(x, y, 1)
abline_values = [slope * i + intercept for i in x]
#Plotting the figure
plt.figure(figsize=(10,8))
plt.scatter(x, y)
plt.plot(x, abline_values, 'b')
plt.title("Slope = %s" % (slope))
plt.xlabel("Run Difference")
plt.ylabel("Wins")
plt.show()  


plt.scatter(x=moneyball_new_1.W, y=moneyball_new_1.RS, c="black", label="Playoff Teams (Moneyball)",alpha=0.7)
plt.scatter(x=moneyball_new_1.W[moneyball_new_1['Team'] == 'OAK'], y=moneyball_new_1.RS[moneyball_new_1['Team'] == 'OAK'], c="red",label="Oakland Athletics")
plt.xlabel("Wins")
plt.ylabel("Runs Scored")
plt.legend(bbox_to_anchor=(1.05,1),loc='upper left')
plt.title("Wins vs Runs Scored by teams who qualified for the playoffs over the years")


moneyball_new = pd.read_csv(r"C:\Users\LENOVO\Downloads\baseball.csv")
moneyball_new_1=moneyball_new[(moneyball_new['Playoffs'] == 1)]
avg_wins = moneyball_new_1.W.mean()
avg_rs = moneyball_new_1.RS.mean()
avg_rd=moneyball_new_1.RD.min()


plt.figure(figsize=(10,8))
plt.scatter(x=moneyball.W, y=moneyball.RA, c="orange",label="Playoff Teams (Moneyball)")  
plt.scatter(x=moneyball.W[moneyball['Playoffs'] == False], y=moneyball.RA[moneyball['Playoffs'] == False], c="black", label="Non-Playoff Teams (Moneyball)",alpha=0.5)
#plt.scatter(x=moneyball.W[moneyball['Team'] == 'OAK'], y=moneyball.RD[moneyball['Team'] == 'OAK'], c="yellow",label="Oakland Athletics")
plt.xlabel("Wins")
plt.ylabel("Runs Allowed")
plt.axvline(x = 103,c='black')
plt.axhline(y = 604,c='black')
plt.legend()
plt.title("RA(604) required by OA's team to qualify for playoffs")

plt.figure(figsize=(10,8))
plt.scatter(x=moneyball.W, y=moneyball.RA, c="orange",label="Playoff Teams (Moneyball)")  
plt.scatter(x=moneyball.W[moneyball['Playoffs'] == False], y=moneyball.RA[moneyball['Playoffs'] == False], c="black", label="Non-Playoff Teams (Moneyball)",alpha=0.5)
#plt.scatter(x=moneyball.W[moneyball['Team'] == 'OAK'], y=moneyball.RD[moneyball['Team'] == 'OAK'], c="yellow",label="Oakland Athletics")
plt.xlabel("Wins")
plt.ylabel("Runs Allowed")
plt.axvline(x = 103,c='black')
plt.axhline(y = 690,c='red')
plt.axhline(y = 604,c='black')
plt.legend()
plt.title("Maximum RA(690) required by OA's team to qualify for playoffs")


plt.scatter(x=moneyball_new_1.W, y=moneyball_new_1.RD, c="black", label="Playoff Teams (Moneyball)",alpha=0.7)
plt.scatter(x=moneyball_new_1.W[moneyball_new_1['Team'] == 'OAK'], y=moneyball_new_1.RD[moneyball_new_1['Team'] == 'OAK'], c="red",label="Oakland Athletics")
plt.xlabel("Wins")
plt.ylabel("Runs Difference")
plt.legend(bbox_to_anchor=(1.05,1),loc='upper left')
plt.title("Wins vs Runs Difference by teams who qualified for the playoffs over the years")


plt.scatter(x=moneyball_new_1.W[moneyball_new_1['Team'] == 'OAK'], y=moneyball_new_1.RD[moneyball_new_1['Team'] == 'OAK'], c="yellow",label="Oakland Athletics")
plt.axvline(x = 95,c='black')
plt.axhline(y = 126,c='black')

