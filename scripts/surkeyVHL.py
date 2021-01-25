from pymongo import MongoClient
import json
import pandas as pd
import numpy as np
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
data = pd.read_csv("../datasets/DatasetVHLType.csv", sep = ";")
comb = []
for i in range(len(data)):
    mutacion = data.loc[i]
    if([mutacion["Molecule"], mutacion["Mutation_type"]] not in comb):
        comb.append([mutacion["Molecule"], mutacion["Mutation_type"]])
data = []
eff = ["1", "2", "2A", "2B", "2C"]
for i in comb:
    for j in eff:
        value = len(list(coleccion.find({"Molecule": i[0], "Mutation_type": i[1], "Case.VHL_type": j})))
        row = [str(i[0])+" "+str(i[1]), j, value]
        data.append(row)
i = 0
while(i < len(data)):
    if(data[i][2] == 0):
        data.pop(i)
    else:
        i+=1
dataframe = pd.DataFrame(columns = ["from", "to", "value"], data= data)
dataframe.to_csv("../datasets/SurveyVHL.csv", sep = ",", index = False)