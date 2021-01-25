import pandas as pd
from pymongo import MongoClient
import numpy as np
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
data = list(coleccion.find({},{"Mutation": 1, "Molecule": 1, "Mutation_type": 1, "Protein_sequence": 1}))
df = pd.DataFrame(columns = ["Mutation", "Molecule", "Mutation_type", "1", "2", "2A", "2B", "2C"])
encabezados = np.array(["1", "2", "2A", "2B", "2C"])
for ii, i in enumerate(data):
    zeros = [0, 0, 0, 0, 0]
    vhls = list(coleccion.find({"Mutation": i["Mutation"]}, {"Case.VHL_type": 1}).distinct("Case.VHL_type"))
    for v in vhls:
        zeros[np.where(encabezados == v)[0][0]] = 1
    row = []
    if(type(i["Mutation"]) == list):
        mutacion = str(i["Mutation"]).replace("'", "").replace("[", "").replace("]", "").replace(" ","")
        row.append(mutacion)
    else:
        row.append(i["Mutation"])
    row.append(i["Molecule"])
    row.append(i["Mutation_type"])
    row += zeros
    df.loc[ii] = row
df.to_csv("../datasets/DatasetVHLType.csv", sep = ";", index=False)