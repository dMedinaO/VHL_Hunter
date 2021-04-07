import pandas as pd
from pymongo import MongoClient
import numpy as np
from Bio import SeqIO
pvhl = str(list(SeqIO.parse("Secuencias/pvhl.fna", "fasta"))[0].seq)
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
sdm = pd.read_csv("Datasets/RawData/chain_v_sdm.csv")[["Mutation", "Predicted_ddg"]]
for i in sdm.values:
    print(i[0])
    mut = "p." + i[0]
    if(len(list(coleccion.find({"Mutation": mut}))) != 0):
        coleccion.update_one({"Mutation": mut},{"$set": {"Predicted_ddg": i[1]}})
    else:
        wt = i[0][0]
        mt = i[0][-1]
        pos = int(i[0].replace(wt, "").replace(mt, ""))
        Protein_sequence = pvhl[0:pos-1] + mt + pvhl[pos:]
        coleccion.insert_one({"Mutation": mut, "Mutation_type": "Missense", "Predicted_ddg": i[1], "Protein_sequence": Protein_sequence})