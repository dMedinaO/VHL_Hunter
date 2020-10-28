import pandas as pd
import pymongo
from pymongo import MongoClient
import numpy as np
import json
muts = np.array(pd.read_csv("../Datasets/Data.csv", sep = "\t"))
arreglo = []
mutaciones = []
types = []
for i in range(muts.shape[0]):
    mutacion = ""
    mutacion += '{"Mutation": "' + str(muts[i,0]) + '", "Mutation_type": "' + str(muts[i,1]) + '", '
    if(str(muts[i,2]) != "nan"):
        mutacion += '"VHL_type": "' + str(muts[i,2]) + '", '
    if(str(muts[i,3]) != "nan"):
        mutacion += '"Disease": ' + str(muts[i,3]) + ', '
    mutacion += '"Pubmed_ID": ' + str(muts[i, 4]) + '}'
    if(muts[i,0] not in mutaciones):
        mutaciones.append(muts[i,0])
        types.append(muts[i,1])
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
print("Mutaciones simples importadas")
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
print("Mutaciones riesgo clínico importadas")



complejas = np.array(pd.read_csv("../Datasets/Complex.csv", sep = "\t"))
arreglo = []
mutaciones = []
for i in range(complejas.shape[0]):
    mutacion = ""
    mutacion += '{"Mutations": ' + str(complejas[i,0]) + ', "Mutation_types": ' + str(complejas[i,1]) + ', '
    if(str(complejas[i,2]) != "nan"):
        mutacion += '"VHL_type": "' + str(complejas[i,2]) + '", '
    if(str(complejas[i,3]) != "nan"):
        mutacion += '"Disease": ' + str(complejas[i,3]) + ', '
    mutacion += '"Pubmed_ID": ' + str(complejas[i, 4]) + '}'
    diccionario = json.loads(mutacion)
    if(complejas[i,0] not in mutaciones):
        mutaciones.append(complejas[i,0])
    arreglo.append(diccionario)
bd = []
for i in range(len(mutaciones)):
    documento = '{"Mutations": ' + mutaciones[i] + ', '
    documento += '"Case": ['
    for j in arreglo:
        if(str(j["Mutations"]).replace("'", '"') == mutaciones[i]):
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
coleccion = db.Complex
coleccion.delete_many({})
coleccion.insert_many(bd, ordered = True)
print("Mutaciones complejas importadas")
