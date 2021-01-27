import pandas as pd
from pymongo import MongoClient
import numpy as np
from Bio import SeqIO
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
data = list(coleccion.find({},{"Mutation": 1, "Protein_sequence": 1}))
totalEffects = np.array(list(coleccion.distinct("Case.Disease.Effect")))
columns = np.concatenate((np.array(["Mutation", "Protein_sequence"]), totalEffects))
df = pd.DataFrame(columns = columns)
for ii, i in enumerate(data):
    zeros = np.zeros(len(totalEffects), int)
    eff = list(coleccion.find({"Mutation": i["Mutation"]}, {"Case.Disease.Effect": 1}).distinct("Case.Disease.Effect"))
    for v in eff:
        zeros[np.where(totalEffects == v)[0][0]] = 1
    row = []
    if(type(i["Mutation"]) == list):
        mutacion = str(i["Mutation"]).replace("'", "").replace("[", "").replace("]", "").replace(" ","")
        row.append(mutacion)
    else:
        row.append(i["Mutation"])
    row.append(i["Protein_sequence"].replace("X",""))
    row = np.array(row)
    row = np.concatenate((row, zeros))
    df.loc[ii] = row
df.to_csv("../Datasets/NewDataSets/setEffects.csv", sep = ";", index=False)