import json
from pymongo import MongoClient
import numpy as np
import pandas as pd
from Bio.Seq import Seq
from Bio import SeqRecord
from Bio import SeqIO
data = pd.read_csv("../datasets/DatasetEffect.csv", sep = ";")
data = data.query('Mutation_type == "Missense"')
temp = np.arange(1, 214, 1)
positions = []
for i in temp:
    positions.append({"position" : i, "Renal Cell Carcinoma" : 0, "Pheochromocytoma" : 0, "Hemangioblastoma" : 0, "Cyst Adenoma" : 0, "Angioma" : 0, "Adenocarcinoma": 0})
for index, row in data.iterrows():
    mutacion = row.Mutation
    pos = int(mutacion[3:-1])
    for j in ["Renal Cell Carcinoma", "Pheochromocytoma", "Hemangioblastoma", "Cyst Adenoma", "Angioma", "Adenocarcinoma"]:
        for i in positions: 
            if(i["position"] == pos and row[j] == 1):
                i[j] += 1
newData = pd.DataFrame(data = positions)
newData.sort_values(by= "position", inplace = True)
newData.drop(["position"], axis = 1, inplace= True)
newData.transpose().to_csv("../datasets/histEff.csv", sep = ",", index = False)