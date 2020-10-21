import pandas as pd
import pymongo
from pymongo import MongoClient
import numpy as np
import json
proteins = np.array(pd.read_csv("../Datasets/Data.csv", sep = "\t"))
arreglo = []
mutaciones = []
types = []
for i in range(proteins.shape[0]):
    mutacion = ""
    mutacion += '{"Mutation": "' + str(proteins[i,0]) + '", "Mutation_type": "' + str(proteins[i,1]) + '", '
    if(str(proteins[i,2]) != "nan"):
        mutacion += '"VHL_type": "' + str(proteins[i,2]) + '", '
    if(str(proteins[i,3]) != "nan"):
        mutacion += '"Disease": ' + str(proteins[i,3]) + ', '
    mutacion += '"Pubmed_ID": ' + str(proteins[i, 4]) + '}'
    if(proteins[i,0] not in mutaciones):
        mutaciones.append(proteins[i,0])
        types.append(proteins[i,1])
    diccionario = json.loads(mutacion)
    arreglo.append(diccionario)
bd = []
for i in range(len(mutaciones)):
    documento = '{"Mutation": "' + mutaciones[i] + '", '
    documento += '"Mutation_type": "' + types[i] + '", '
    documento += '"Case": ['
    for j in arreglo:
        if(j["Mutation"] == mutaciones[i]):
            documento += "{"
            try: 
                documento += '"VHL_type": "' + j["VHL_type"] + '"'
            except:
                documento = documento
            try:
                documento += '"Disease": ' + str(j["Disease"])
            except:
                documento = documento
            try:
                documento += '"Pubmed_ID": ' + str(j["Pubmed_ID"]) 
            except:
                documento = documento
            documento += "}"
    documento += ']}'
    documento = documento.replace('{}', "").replace("}{", "}, {").replace("'", '"').replace('""', '", "').replace(']"','], "')
    diccionario = json.loads(documento)
    bd.append(diccionario)
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutations
coleccion.delete_many({})
coleccion.insert_many(bd, ordered = True)

ClinicalRisk = pd.read_csv("../Datasets/ClinicalRisk.csv", sep = "\t")[["MUTATION", "RISK"]]
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutations
listRisks = []
for ii, i in enumerate(ClinicalRisk["MUTATION"]):
    res = list(coleccion.find({"Mutation": i}))
    if(len(res) == 1):
        coleccion.update_one({"Mutation": i}, {"$set": {"Risk": ClinicalRisk["RISK"][ii]}})
    else:
        dato = '{"Mutation": "' + i + '", "Mutation_type": "Missense", "Risk": "'+ ClinicalRisk["RISK"][ii] + '"}'
        diccionario = json.loads(dato)
        listRisks.append(diccionario)
coleccion.insert_many(listRisks, ordered = True)
print("Mutaciones simples importadas")