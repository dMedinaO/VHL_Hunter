import json
from pymongo import MongoClient
import numpy as np
import pandas as pd
from Bio.Seq import Seq
from Bio import SeqRecord
from Bio import SeqIO
data = pd.read_csv("../datasets/DatasetVHLType.csv", sep = ";")
data = data.query('Mutation_type == "Missense"')
temp = np.arange(1, 214, 1)
positions = []
for i in temp:
    positions.append({"position" : i, "1": 0, "2": 0, "2A": 0, "2B": 0, "2C": 0})
for index, row in data.iterrows():
    mutacion = row.Mutation
    pos = int(mutacion[3:-1])
    for j in ["1", "2", "2A", "2B", "2C"]:
        for i in positions: 
            if(i["position"] == pos and row[j] == 1):
                i[j] += 1
newData = pd.DataFrame(data = positions)
newData.sort_values(by= "position", inplace = True)
newData.drop(["position"], axis = 1, inplace= True)
newData.transpose().to_csv("../datasets/histVHL.csv", sep = ",", index = False)