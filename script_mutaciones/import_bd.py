import pandas as pd
import pymongo
from pymongo import MongoClient
import numpy as np
import json
data = np.array(pd.read_csv("../Datasets/dataset.csv", sep = "\t"))
arreglo = []
for i in range(data.shape[0]):
    mutacion = ""
    mutacion += '{"Mutation_aa": "' + str(data[i,0]) + '", "Mutation_type": "' + str(data[i,1]) + '", '
    if(str(data[i,2]) != "nan"):
        mutacion += '"VHL_type": "' + str(data[i,2]) + '", '
    if(str(data[i,3]) != "nan"):
        mutacion += '"Disease": [' + str(data[i,3]) + '], '
    mutacion += '"Pubmed_ID": "' + str(data[i, 4]) + '"}'
    diccionario = json.loads(mutacion)
    arreglo.append(diccionario)

con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutations
coleccion.insert_many(arreglo, ordered = True)