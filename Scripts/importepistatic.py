import pandas as pd
from pymongo import MongoClient
import numpy as np
from Bio import SeqIO
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
epistatic = pd.read_csv("Datasets/RawData/VHL_HUMAN_b0.5_single_mutant_matrix.csv")
for i in epistatic.values:
    mutacion = "p." + i[1]
    frequency = i[5]
    column_conservation = i[6]
    prediction_epistatic = i[7]
    prediction_independent = i[8]
    coleccion.update_one({"Mutation": mutacion},{"$set": {"Epistatic_column_conservation": column_conservation, "Epistatic_frequency": frequency, "Epistatic_Prediction_epistatic": prediction_epistatic, "Epistatic_Prediction_independent": prediction_independent}})