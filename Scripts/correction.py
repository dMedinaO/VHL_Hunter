import pandas as pd
from pymongo import MongoClient
import numpy as np
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
sdm = pd.read_csv("../Datasets/RawData/chain_v_sdm.csv")
for i in sdm.values:
    mutacion = "p." + str(i[2])
    diccionario = {}
    for ij, j in enumerate(sdm.columns):
        if(" (angstrom)" in j):
            diccionario["sdm_" + j.replace(" (angstrom)", "")] = i[ij]
        else:
            if("(%)" in j):
                diccionario["sdm_" + j.replace("(%)", "")] = i[ij]
            else:
                diccionario["sdm_" + j] = i[ij]
    diccionario.pop("sdm_PDB file")
    diccionario.pop("sdm_Chain ID")
    diccionario.pop("sdm_Predicted_ddg")
    diccionario.pop("sdm_Mutation")
    coleccion.update_one({"Mutation": mutacion},{"$set": diccionario})

