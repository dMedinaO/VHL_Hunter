import json
from pymongo import MongoClient
import numpy as np
import pandas as pd
from Bio.Seq import Seq
from Bio import SeqRecord
from Bio import SeqIO
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
data = list(coleccion.find({},{"Mutation": 1, "Mutation_type": 1, "Protein_sequence": 1, "DNA_sequence":1}))
df = pd.DataFrame(data = data)
listRecords = []
for i in range(len(df)):
    if(type(df.loc[i].Mutation) != str):
        df.loc[i].Mutation = str(df.loc[i].Mutation).replace("'","").replace("[","").replace("]","")
    dicc = {"Mutation": df.loc[i].Mutation}
    dicc["Mutation_type"] = df.loc[i].Mutation_type
    if(type(df.loc[i].DNA_sequence) != float):
        dicc["Protein_sequence"] = df.loc[i].Protein_sequence
        dicc["DNA_sequence"] = df.loc[i].DNA_sequence
    if(type(df.loc[i].DNA_sequence) == float):
        dicc["Protein_sequence"] = df.loc[i].Protein_sequence
    req = SeqRecord.SeqRecord(seq = Seq(dicc["Protein_sequence"]), id = dicc["Mutation"] + " Protein sequence", name = dicc["Mutation"] + " Protein sequence", description = dicc["Mutation_type"])
    listRecords.append(req)
with open("../datasets/AllDataFasta.fasta", "w") as output_handle:
    SeqIO.write(listRecords, output_handle, "fasta")