import pandas as pd
from pymongo import MongoClient
import numpy as np
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
effects = list(coleccion.find({}, {"Case.Disease.Effect": 1}).distinct("Case.Disease.Effect"))
data = list(coleccion.find({},{"Mutation": 1, "Molecule": 1, "Mutation_type": 1, "Protein_sequence": 1}))
df = pd.DataFrame(columns = ["Mutation", "Molecule", "Mutation_type"] + effects)
encabezados = np.array(effects)
for ii, i in enumerate(data):
    zeros = np.zeros(len(effects), int)
    eff = list(coleccion.find({"Mutation": i["Mutation"]}, {"Case.Disease.Effect": 1}).distinct("Case.Disease.Effect"))
    for e in eff:
        zeros[np.where(encabezados == e)[0][0]] = 1
    row = []
    if(type(i["Mutation"]) == list):
        mutacion = str(i["Mutation"]).replace("'", "").replace("[", "").replace("]", "").replace(" ","")
        row.append(mutacion)
    else:
        row.append(i["Mutation"])
    row.append(i["Molecule"])
    row.append(i["Mutation_type"])
    row = np.concatenate((row, zeros))
    df.loc[ii] = row
df.to_csv("../datasets/DatasetEffect.csv", sep = ";", index=False)