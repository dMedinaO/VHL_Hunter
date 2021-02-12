from pymongo import MongoClient
import json
import pandas as pd
import numpy as np
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
data = pd.read_csv("../datasets/DatasetEffect.csv", sep = ";")
data = data[["Renal Cell Carcinoma", "Pheochromocytoma", "Hemangioblastoma", "Cyst Adenoma", "Angioma", "Adenocarcinoma"]]
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
for j in data:
    diccionario.append({"name": j, "sets": [j], "value": len(list(coleccion.find({"Case.Disease.Effect": j})))})
for j in combinaciones:
    filters = []
    for i in j:
        filters.append({"Case.Disease.Effect": i})
    cant = 0
    if(len(filters) > 1):
        cant = len(list(coleccion.aggregate([{"$match": {"$and": filters}}])))    
        diccionario.append({"name": str(j).replace("[","").replace("]", "").replace("'", ""), "sets": j, "value": cant})
diccionario.append({"name": "", "sets": [], "value": cont_nulos})
print(diccionario)
with open('../datasets/eff-venn.json', 'w') as json_file:
    json.dump(diccionario, json_file)