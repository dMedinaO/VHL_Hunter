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
                            "SDM: MT_DEPTH", "SDM: MT_OSP", "SDM: MT_RSA","SDM: MT_SN", "SDM: MT_SO",
                            "SDM: MT_SS","SDM: MT_SSE","SDM: WT_DEPTH", "SDM: WT_OSP", "SDM: WT_RSA",
                            "SDM: WT_SN", "SDM: WT_SO", "SDM: WT_SS","SDM: WT_SSE", "SDM: Predicted ddg", 
                            "SDM: Outcome", "WhatIf: dHBonds", "WhatIf: dEnergyHbonds", "Epistatic: Prediction epistatic", 
                            "Epistatic: Prediction independent","Epistatic: Column conservation", "Epistatic: Frequency",
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
    for j in RCC_detail:
        if(j in description):
            diccionario["Carcinoma/RCC: " + j] = 1
        else:
            diccionario["Carcinoma/RCC: " + j] = 0
    print(i)
    try:
        diccionario["SDM: WT_DEPTH"] = i["sdm_WT_DEPTH"]
    except:
        pass
    try:
        diccionario["SDM: WT_OSP"] = i["sdm_WT_OSP"]
    except:
        pass
    try:
        diccionario["SDM: WT_RSA"] = i["sdm_WT_RSA"]
    except:
        pass
    try:
        diccionario["SDM: WT_SN"] = i["sdm_WT_SN"]
    except:
        pass
    try:
        diccionario["SDM: WT_SO"] = i["sdm_WT_SO"]
    except:
        pass
    try:
        diccionario["SDM: WT_SS"] = i["sdm_WT_SS"]
    except:
        pass
    try:
        diccionario["SDM: WT_SSE"] = i["sdm_WT_SSE"]
    except:
        pass
    try:
        diccionario["SDM: MT_DEPTH"] = i["sdm_MT_DEPTH"]
    except:
        pass
    try:
        diccionario["SDM: MT_OSP"] = i["sdm_MT_OSP"]
    except:
        pass
    try:
        diccionario["SDM: MT_RSA"] = i["sdm_MT_RSA"]
    except:
        pass
    try:
        diccionario["SDM: MT_SN"] = i["sdm_MT_SN"]
    except:
        pass
    try:
        diccionario["SDM: MT_SO"] = i["sdm_MT_SO"]
    except:
        pass
    try:
        diccionario["SDM: MT_SS"] = i["sdm_MT_SS"]
    except:
        pass
    try:
        diccionario["SDM: MT_SSE"] = i["sdm_MT_SSE"]
    except:
        pass
    try:
        diccionario["SDM: Outcome"] = i["sdm_Outcome"]
    except:
        pass
    data = data.append(diccionario, ignore_index = True)
data.sort_values(by= "Position").to_csv("Landscape.csv", index = False)