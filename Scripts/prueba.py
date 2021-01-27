import pandas as pd
data = pd.read_csv("../Datasets/NewDataSets/SetVHLType.csv", sep = ";")
data = data[["VHL: 1", "VHL: 2", "VHL: 2A", "VHL: 2B", "VHL: 2C"]]
combinaciones = []
for i in range(len(data)):
    combinacion = []
    if(data.loc[i]["VHL: 1"] == 1):
        combinacion.append("1")
    if(data.loc[i]["VHL: 2"] == 1):
        combinacion.append("2")
    if(data.loc[i]["VHL: 2A"] == 1):
        combinacion.append("2A")
    if(data.loc[i]["VHL: 2B"] == 1):
        combinacion.append("2B")
    if(data.loc[i]["VHL: 2C"] == 1):
        combinacion.append("2C")
    if(combinacion not in combinaciones):
        combinaciones.append((combinacion))
conteo = {}
for i in combinaciones:
    key = str(i).replace("[", "").replace("]", "").replace("'", "")
    conteo[key] = 0
for i in range(len(data)):
    combinacion = []
    if(data.loc[i]["VHL: 1"] == 1):
        combinacion.append("1")
    if(data.loc[i]["VHL: 2"] == 1):
        combinacion.append("2")
    if(data.loc[i]["VHL: 2A"] == 1):
        combinacion.append("2A")
    if(data.loc[i]["VHL: 2B"] == 1):
        combinacion.append("2B")
    if(data.loc[i]["VHL: 2C"] == 1):
        combinacion.append("2C")
    conteo[str(combinacion).replace("[", "").replace("]", "").replace("'", "")] += 1
print(conteo)