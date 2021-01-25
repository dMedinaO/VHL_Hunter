from pymongo import MongoClient
import json
import pandas as pd
import numpy as np
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
data = pd.read_csv("../datasets/DatasetVHLType.csv", sep = ";")
data = data.drop(["Mutation","Molecule", "Mutation_type"], axis = 1)
combinaciones = []
cont_nulos = 0
for i in range(len(data)):
    combinacion = []
    if(sum(data.loc[i]) == 0):
        cont_nulos+=1
    for j in data.loc[i].keys():
        if(data.loc[i][j] == 1):
            combinacion.append(j)
    if(combinacion not in combinaciones):
        combinaciones.append(combinacion)
diccionario = []
for j in combinaciones:
    filters = []
    for i in j:
        filters.append({"Case.VHL_type": i})
    cant = 0
    if(filters != []):
        cant = len(list(coleccion.aggregate([{"$match": {"$and": filters}}])))
    diccionario.append({"name": str(j).replace("[","").replace("]", "").replace("'", ""), "sets": j, "value": cant})
for k in diccionario:
    if(k["name"] == ""):
        k["value"] = cont_nulos
print(diccionario)
with open('../datasets/vhl-venn.json', 'w') as json_file:
    json.dump(diccionario, json_file)
"""
conteo = {}
for i in combinaciones:
    key = str(i)
    conteo[key] = 0
for i in range(len(data)):
    combinacion = []
    for j in data.loc[i].keys():
        if(data.loc[i][j] == 1):
            combinacion.append(j)
    conteo[str(combinacion).replace("[", "").replace("]", "").replace("'", "")] += 1
data = []
for i in conteo.keys():
    data.append({"name": i,
                 "sets": str.split(i, ", "),
                 "value": conteo[i]})
with open('../datasets/vhl-venn.json', 'w') as json_file:
    json.dump(data, json_file)
"""