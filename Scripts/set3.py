import pandas as pd
from pymongo import MongoClient
import numpy as np
import time
from Bio import SeqIO
from Bio.Seq import Seq
import sys
def missense(mutacion):
    temp = mutacion.replace("p.","")
    wt = temp[0]
    mut = temp[-1]
    pos = int(temp.replace(wt,"").replace(mut,""))
    seq = (pvhl[:pos-1] + mut + pvhl[pos:])
    return seq
def nonsense(mutacion):
    temp = mutacion.replace("p.","")
    wt = temp[0]
    pos = int(temp.replace(wt,"").replace("X",""))
    seq = pvhl[:pos-1]
    return seq
def insertion_nt(mutacion):
    temp = mutacion.replace("c.", "").split("ins")
    pos = int(temp[0])
    seq = cds_vhl[:pos-1] + temp[1] + cds_vhl[pos-1:]
    while(len(seq) %3 != 0):
        seq += "N"
    seq = Seq(str(seq)).translate(to_stop=True)
    return seq
def insertion_aa(mutacion):
    temp = mutacion.replace("p.", "").split("ins")
    pos = int(temp[0])
    seq = pvhl[:pos-1] + temp[1] + pvhl[pos-1:]
    return seq
def range_deletion_nt(mutacion):
    temp = mutacion.replace("c.", "").replace("del", "").split("_")
    ini = int(temp[0])
    fin = int(temp[1])
    seq = cds_vhl[:ini-1]+cds_vhl[fin:]
    while(len(seq) %3 != 0):
        seq += "N"
    seq = Seq(str(seq)).translate(to_stop=True)
    return seq
def range_deletion_aa(mutacion):
    temp = mutacion.replace("p.", "").replace("del","").split("_")
    pos = int(temp[0])
    pos2 = int(temp[1])
    seq = pvhl[:pos-1] + pvhl[pos2-1:]
    return seq
def single_deletion_nt(mutacion):
    temp = mutacion.replace("c.", "").replace("del", "")
    pos = int(temp)
    seq = cds_vhl[:pos-1] + cds_vhl[pos:]
    while(len(seq) %3 != 0):
        seq += "N"
    seq = Seq(str(seq)).translate(to_stop=True)
    return seq
def single_deletion_aa(mutacion):
    temp = mutacion.replace("p.", "").replace("del","")
    pos = int(temp[0])
    seq = pvhl[:pos-1] + pvhl[pos-1:]
    return seq

cds_vhl = str(list(SeqIO.parse("../Secuencias/VHL_cds.fna", "fasta"))[0].seq)
pvhl = str(list(SeqIO.parse("../Secuencias/pvhl.fna", "fasta"))[0].seq)
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutations
data = list(coleccion.find({"Case.VHL_type": {"$exists": True}}))
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
columns.append("Mutation")
columns.append("Mutation_type")
for i in total_vhl:
    columns.append(i)
for i in total_effects:
    columns.append(i)
columns.append("seq")
for i in data:
    fila = []
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
    fila.append(i["Mutation"])
    fila.append(i["Mutation_type"])
    for v in arreglo_vhl:
        fila.append(int(v))
    for e in arreglo_effects:
        fila.append(int(e))
    if(fila[1] == "Missense"):
        seq = str(missense(fila[0]))
    if(fila[1] == "Nonsense"):
        seq = str(nonsense(fila[0]))
    if(fila[1] == "Insertion (aa)"):
        seq = insertion_aa(fila[0])
    if(fila[1] == "Insertion (nt)"):
        seq = str(insertion_nt(fila[0]))
    if(fila[1] == "Range_Deletion (aa)"):
        seq = str(range_deletion_aa(fila[0]))
    if(fila[1] == "Range_Deletion (nt)"):
        seq = str(range_deletion_nt(fila[0]))
    if(fila[1] == "Single_Deletion (nt)"):
        seq = str(single_deletion_nt(fila[0]))
    if(fila[1] == "Single_Deletion (aa)"):
        seq = str(single_deletion_aa(fila[0]))
    if(fila[1] == "Silent"):
        seq = str(pvhl)
    fila.append(seq)
    dataset.append(fila)
data = pd.DataFrame(dataset, columns= columns)
print(data)
data.to_csv("../Datasets/trainingSets/set3.csv", sep = "\t", index = False)