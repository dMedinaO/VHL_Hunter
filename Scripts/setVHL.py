import pandas as pd
from pymongo import MongoClient
import numpy as np
import time
from Bio import SeqIO
import sys
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
data = list(coleccion.find({},{"Mutation": 1, "Protein_sequence": 1}))
df = pd.DataFrame(columns = ["Mutation", "Protein_sequence", "VHL: 1", "VHL: 2", "VHL: 2A", "VHL: 2B", "VHL: 2C"])
encabezados = np.array(["1", "2", "2A", "2B", "2C"])
for ii, i in enumerate(data):
    zeros = [0, 0, 0, 0, 0]
    vhls = list(coleccion.find({"Mutation": i["Mutation"]}, {"Case.VHL_type": 1}).distinct("Case.VHL_type"))
    for v in vhls:
        zeros[np.where(encabezados == v)[0][0]] = 1
    row = []
    if(type(i["Mutation"]) == list):
        mutacion = str(i["Mutation"]).replace("'", "").replace("[", "").replace("]", "")
        row.append(mutacion)
    else:
        row.append(i["Mutation"])
    row.append(i["Protein_sequence"])
    row += zeros
    df.loc[ii] = row
df.to_csv("../Datasets/NewDataSets/SetVHLType.csv", sep = ";", index=False)