import pandas as pd
from pymongo import MongoClient
import numpy as np
import time
from Bio import SeqIO
import sys
def processmutation(mutacion, seqInput):
    print(mutacion)
    mutacion = mutacion.replace("p.","")
    wt = mutacion[0]
    mut = mutacion[-1]
    pos = int(mutacion.replace(wt,"").replace(mut,""))
    seq = (seqInput[:pos-1] + mut + seqInput[pos:])
    return seq

pvhl = str(list(SeqIO.parse("../Secuencias/pvhl.fna", "fasta"))[0].seq)
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Complex
data = list(coleccion.find())

#Toda la data
total_vhl = []
total_effects = []
cant_mutations = 0
for i in data:
    if(len(i["Mutations"]) > cant_mutations):
        cant_mutations = len(i["Mutations"])
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
print(cant_mutations)

dataset = []
columns = []
columns.append("Mutation1")
columns.append("Mutation2")
for i in total_vhl:
    columns.append("VHL: " + i)
for i in total_effects:
    columns.append("Effect: " + i)
columns.append("seq")
print(columns)
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
    seq = pvhl
    fila = []
    for i in i["Mutations"]:
        seq = processmutation(i, seq)
        fila.append(i)
    for v in arreglo_vhl:
        fila.append(int(v))
    for e in arreglo_effects:
        fila.append(int(e))
    fila.append(seq)
    dataset.append(fila)
data = pd.DataFrame(dataset, columns= columns)
print(data)
data.to_csv("../Datasets/trainingSets/set4.csv", index=False, sep = "\t")