import json
from pymongo import MongoClient
import numpy as np
import pandas as pd
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
data = list(coleccion.find({}))
df = pd.DataFrame(data = data)
df = df.drop(["_id"], axis = 1)
df.to_json("../datasets/AllDataJson.json")