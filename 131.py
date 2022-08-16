import csv
import pandas as pd

df = pd.read_csv("totalPlanetData.csv")


massList = df["Mass"]
nameList = df["Name"]
radiusList = df["radius"]

for i in massList:
    if i == "NaN":
        massList.remove(i)
    elif i == "Mass":
        massList.remove(i)

for i in radiusList:
    if i == "NaN":
        radiusList.remove(i)

planet_gravity = []

for index, name in enumerate(nameList):
  gravity = (float(massList[index])*1.989e+30) / (float(radiusList[index])*float(radiusList[index])*6.957e+8*6.957e+8) * 6.674e-11
  planet_gravity.append(gravity)
