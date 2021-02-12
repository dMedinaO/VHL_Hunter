import json
from pymongo import MongoClient
import numpy as np
import pandas as pd

con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
data = pd.read_csv("../datasets/DatasetEffect.csv", sep = ";").drop(["Mutation"], axis = 1)
effects = list(coleccion.find({}, {"Case.Disease.Effect": 1}).distinct("Case.Disease.Effect"))
query = ""
for i in effects:
    query = query + "`" + i + "` == 0 and"
nulos = data.query(query[0:-3]).index
for index, row in data.iterrows():
    if(index in nulos):
        data.loc[index, "No effect"] = 1
    else:
        data.loc[index, "No effect"] = 0
data["No effect"] = data["No effect"].astype(int)
data = data.groupby(["Molecule", "Mutation_type"]).sum()
data.transpose().to_json("../datasets/resumeDataEff.json",orient="index")
