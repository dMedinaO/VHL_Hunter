import pandas as pd
from pymongo import MongoClient
import numpy as np
from Bio import SeqIO
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
epistatic = pd.read_csv("Datasets/RawData/VHL_HUMAN_b0.5_single_mutant_matrix.csv")
missenses = list(coleccion.find({"Mutation_type": "Missense"}))
for i in missenses:
    nombre = i["Mutation"]
    largo = len(epistatic.query("mutant == '" + nombre.replace("p.", "") + "'"))
    if(largo == 0):
        print(nombre)