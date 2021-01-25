import pandas as pd
from pymongo import MongoClient
import numpy as np
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
listSurfaces = ["A", "B", "C", "D"]
row = []
for i in listSurfaces:
    data = len(list(coleccion.find({"Surface": i}, {})))
    row.append(data)
df = pd.DataFrame(columns = listSurfaces)
df.loc[0] = row
df.to_csv("../datasets/surface-var.csv", index = False, sep = ",")