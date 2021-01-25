import pandas as pd
from pymongo import MongoClient
import numpy as np
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
aminoacids = np.array(["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"])
data = list(coleccion.find({"Mutation_type": "Missense"},{"_id": 0,"Mutation": 1}))
listaMutaciones = []
for i in data:
    listaMutaciones.append(i["Mutation"])
mat = np.zeros([20,20], int)
for i in listaMutaciones:
    mutacion = i.split(".")[1]
    wt = mutacion[0]
    mut = mutacion[-1]
    pos = mutacion.replace(wt, "").replace(mut, "")
    mat[np.where(aminoacids == wt)[0][0]][np.where(aminoacids == mut)[0][0]] += 1
data = pd.DataFrame(columns = aminoacids, data = mat)
data.to_csv("../datasets/SubstitutionMatriz.csv", index = False)