import pandas as pd
from pymongo import MongoClient
import numpy as np
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
missense = list(coleccion.find({"Mutation_type": "Missense"}))
effects = list(coleccion.distinct(key = "Case.Disease.Effect", filter = {"Mutation_type": "Missense"}))
vhls = list(coleccion.distinct(key = "Case.VHL_type", filter = {"Mutation_type": "Missense"}))
RCC_detail = ["Clear Cell", "Squamous Cell"]
data = pd.DataFrame(columns = ["Mutation", "Wild aa", "Position", "Mutated aa", "Surface", 
                            "SDM: Predicted ddg", "WhatIf: dHBonds", "Whatif: dEnergyHbonds", 
                            "Epistatic: Prediction epistatic", "Epistatic: Prediction independent",
                            "Epistatic: Column conservation", "Epistatic: Frequency",
                            "RCC Clinical Risk"] 
                            + ["Effect: " + eff for eff in effects] + ["Carcinoma/RCC: Clear Cell", "Carcinoma/RCC: Squamous Cell"]
                            + ["VHL type: " + v for v in vhls] + ["Protein sequence"])
for i in missense:
    diccionario = {}
    diccionario["Mutation"] = i["Mutation"]
    diccionario["Wild aa"] = i["Mutation"][2]
    diccionario["Mutated aa"] = i["Mutation"][-1]
    diccionario["Position"] = int(i["Mutation"].replace(i["Mutation"][2], "").replace(i["Mutation"][-1], "").replace("p.", ""))
    try:
        diccionario["Surface"] = i["Surface"]
    except:
        pass
    try:
        if(i["Risk"] == "HIGH"):
            diccionario["RCC Clinical Risk"] = 1
        else:
            diccionario["RCC Clinical Risk"] = 0
    except:
        pass
    try:
        diccionario["SDM: Predicted ddg"] = i["Predicted_ddg"]
    except:
        pass
    try:
        diccionario["WhatIf: dHBonds"] = i["dHbonds"]
    except:
        pass
    try:
        diccionario["WhatIf: dEnergyHbonds"] = round(i["dEnergyHbonds"],3)
    except:
        pass
    try:
        diccionario["Epistatic: Prediction epistatic"] = round(i["Epistatic_Prediction_epistatic"])
    except:
        pass
    
    try:
        diccionario["Epistatic: Prediction independent"] = round(i["Epistatic_Prediction_independent"])
    except:
        pass
    
    try:
        diccionario["Epistatic: Column conservation"] = round(i["Epistatic_column_conservation"])
    except:
        pass

    try:
        diccionario["Epistatic: Frequency"] = round(i["Epistatic_frequency"])
    except:
        pass
    eff = list(coleccion.distinct(key = "Case.Disease.Effect", filter = {"Mutation_type": "Missense", "Mutation": i["Mutation"]}))
    for e in effects:
        if(e in eff):
            diccionario["Effect: " + e] = 1
        else:
            diccionario["Effect: " + e] = 0
    vhl = list(coleccion.distinct(key = "Case.Disease.VHL_type", filter = {"Mutation_type": "Missense", "Mutation": i["Mutation"]}))
    for v in vhls:
        if(v in vhl):
            diccionario["VHL type: " + v] = 1
        else:
            diccionario["VHL type: " + v] = 0
    diccionario["Protein sequence"] = i["Protein_sequence"]
    description = list(coleccion.distinct(key = "Case.Disease.Description", filter = {"Mutation_type": "Missense", "Mutation": i["Mutation"]}))
    for i in RCC_detail:
        if(i in description):
            diccionario["Carcinoma/RCC: " + i] = 1
        else:
            diccionario["Carcinoma/RCC: " + i] = 0
    data = data.append(diccionario, ignore_index = True)
data.sort_values(by= "Position").to_csv("Landscape.csv", index = False)