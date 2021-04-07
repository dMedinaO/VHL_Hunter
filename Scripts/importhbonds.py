import pandas as pd
from pymongo import MongoClient
import numpy as np
from Bio import SeqIO
pvhl = str(list(SeqIO.parse("Secuencias/pvhl.fna", "fasta"))[0].seq)
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
data = pd.read_csv("Datasets/RawData/DatasetHbonds.csv")
for i in data.values:
    mutacion = "p." + i[0]
    dHbonds = i[1]
    dEnergy = i[2]
    coleccion.update_one({"Mutation": mutacion},{"$set": {"dHbonds": i[1], "dEnergyHbonds": i[2]}})