import pandas as pd
from pymongo import MongoClient
import numpy as np
import time
from Bio import SeqIO
import sys
def processmutation(mutacion):
    mutacion = mutacion.replace("p.","")
    wt = mutacion[0]
    mut = mutacion[-1]
    pos = int(mutacion.replace(wt,"").replace(mut,""))
    seq = (pvhl[:pos-1] + mut + pvhl[pos:])
    return (wt, pos, mut, seq)

pvhl = str(list(SeqIO.parse("../Secuencias/pvhl.fna", "fasta"))[0].seq)
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutations
data = list(coleccion.find({"Risk": {"$exists": True}}))
#Toda la data
total_vhl = []
total_effects = []
for i in data:
    try: 
        case = i["Case"]
        for c in case:
            try:
                disease = c["Disease"]
                for d in disease:
                    if(d["Effect"] not in total_effects):
                        total_effects.append(d["Effect"])
            except:
                pass
            try: 
                vhl = c["VHL_type"]
                if(vhl not in total_vhl):
                    total_vhl.append(vhl)
            except:
                pass
    except:
        pass
total_effects = np.array(total_effects)
total_vhl = np.array(total_vhl)
#Llenado de datos
dataset = []
columns = []
columns.append("wt")
columns.append("pos")
columns.append("mut")
columns.append("risk")
for i in total_vhl:
    columns.append(i)
for i in total_effects:
    columns.append(i)
columns.append("seq")
for i in data:
    arreglo_effects = np.zeros(len(total_effects))
    arreglo_vhl = np.zeros(len(total_vhl))
    try: 
        a = i["Case"]
        for aa in a:
            try:
                arreglo_vhl[np.where(total_vhl == aa["VHL_type"])] = 1
            except:
                pass
            try: 
                b = aa["Disease"]
                for bb in b:
                    arreglo_effects[np.where(total_effects == bb["Effect"])] = 1
            except: 
                pass
    except:
        pass
    wt, pos, mut, seq = processmutation(i["Mutation"])
    fila = []
    fila.append(wt)
    fila.append(pos)
    fila.append(mut)
    if(i["Risk"] == "HIGH"):
        fila.append(1)
    if(i["Risk"] == "LOW"):
        fila.append(0)
    for v in arreglo_vhl:
        fila.append(int(v))
    for e in arreglo_effects:
        fila.append(int(e))
    fila.append(seq)
    dataset.append(fila)
data = pd.DataFrame(dataset, columns= columns)
print(data)
data.to_csv("../Datasets/set5.csv", sep = "\t", index = False)