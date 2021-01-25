import pandas as pd
from pymongo import MongoClient
import numpy as np
from Bio import SeqIO
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
pvhl = str(list(SeqIO.parse("../sequences/pvhl.fna", "fasta"))[0].seq)
aminoacids = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
data = list(coleccion.find({"Mutation_type": "Missense"},{"_id": 0,"Mutation": 1}))
listaMutaciones = []
for i in data:
    mutacion = i["Mutation"].split(".")[1]
    wt = mutacion[0]
    mut = mutacion[-1]
    pos = mutacion.replace(wt, "").replace(mut, "")
    listaMutaciones.append({"wt": wt, "pos": int(pos), "mut": mut})
largo = len(pvhl)
matriz = np.zeros((largo, 20), int)
data = pd.DataFrame(columns = aminoacids, data = matriz)
for i in listaMutaciones:
    data.loc[i["pos"]-1, i["mut"]] = 1
data.transpose().to_csv("../datasets/SubstitutionPosition.csv", sep = ",", index = False)