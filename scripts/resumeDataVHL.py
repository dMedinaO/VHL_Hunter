import json
from pymongo import MongoClient
import numpy as np
import pandas as pd
data = pd.read_csv("../datasets/DatasetVHLType.csv", sep = ";").drop(["Mutation"], axis = 1)
nulos = data.query("`1` == 0 and `2` == 0 and `2A` == 0 and `2B` == 0 and `2C` == 0").index
for index, row in data.iterrows():
    if(index in nulos):
        data.loc[index, "No VHL"] = 1
    else:
        data.loc[index, "No VHL"] = 0
data["No VHL"] = data["No VHL"].astype(int)
data = data.groupby(["Molecule", "Mutation_type"]).sum()
data.transpose().to_json("../datasets/resumeDataVHL.json",orient="index")
exit()
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
mutationType = list(coleccion.find({}, {"Mutation_type": 1}).distinct("Mutation_type"))
molecules = ["DNA", "Protein"]
vhls = list(coleccion.find({}, {"Case.VHL_type": 1}).distinct("Case.VHL_type"))
columns = ["VHL type"] + vhls 
data = pd.DataFrame()
for ij, j in enumerate(vhls):
    row = {"VHL type": j}
    total = 0
    for i in mutationType:
        count = len(list(coleccion.find({"Mutation_type": i, "Case.VHL_type": j}, {"Mutation": 1, "_id": 0})))
        total += count
        row[i] = count
    row["Total"] = total
    data = data.append(row, ignore_index = True)
data[mutationType] = data[mutationType].astype(int)
data.Total = data.Total.astype(int)
data.set_index("VHL type", inplace = True)
data.to_csv("../datasets/resumeDataVHL.csv", sep = ",")