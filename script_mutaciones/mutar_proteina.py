from Bio import SeqIO
from Bio.Seq import MutableSeq
import pandas as pd
from Bio.Alphabet import generic_protein
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import numpy as np
def to_dataframe(aux, list_columns):
    mutaciones = np.array(aux)
    data_frame = pd.DataFrame(mutaciones, columns = list_columns)
    data_frame.drop_duplicates(inplace = True)
    data_frame.reset_index(inplace=True)
    data_frame.drop("index", axis = 1, inplace = True)
    return data_frame

#Este script toma una mutación y devuelve un .fasta con todas las proteínas mutadas
try:
    pvhl = str(list(SeqIO.parse("../Proteina/pvhl.fna", "fasta"))[0].seq)
    print(pvhl)
except: 
    print("Error in .fasta format")
    exit()
data = pd.read_csv("../Datasets/dataset.csv", sep = "\t")
record = []
#Missense
aux = []
for mutacion in data.query("Mutation_type == 'Missense'").Mutation_aa:
    wt = mutacion[2]
    mut = mutacion[-1]
    pos = mutacion.replace(wt, "").replace(mut,"").replace("p.","")
    aux.append((mutacion, wt, pos, mut))
data_frame = to_dataframe(aux, ["name", "wt", "pos", "mut"])
for i in range(len(data_frame)):
    mutated = MutableSeq(pvhl, generic_protein)
    mutated[int(data_frame.loc[i].pos) - 1] = data_frame.loc[i].mut
    nombre = data_frame.loc[i].name
    record.append(SeqRecord(Seq(str(mutated)), id = "p." + nombre, name="pVHL", description= "pVHL mutation p." + nombre))
    print("Success: p."+ str(data_frame.loc[i].wt), (data_frame.loc[i].pos), str(data_frame.loc[i].mut), sep = "")
#Nonsense
aux = []
for mutacion in data.query("Mutation_type == 'Nonsense'").Mutation_aa:
    wt = mutacion[2]
    pos = mutacion.replace(wt, "").replace("p.","").replace("X","")
    aux.append((mutacion, wt, pos))
data_frame = to_dataframe(aux, ["name", "wt", "pos"])
for i in range(len(data_frame)):
    mutated = MutableSeq(pvhl, generic_protein)
    mutated = mutated[0:int(data_frame.loc[i].pos) - 1]
    nombre = data_frame.loc[i].name
    record.append(SeqRecord(Seq(str(mutated)), id = nombre, name="pVHL", description= "pVHL mutation " + nombre))
    print("Success:", nombre)
#Simple Delete
aux = []
for mutacion in data.query("Mutation_type == 'Nonsense'").Mutation_aa:
    wt = mutacion[2]
    pos = mutacion.replace(wt, "").replace("p.","").replace("X","")
    aux.append((mutacion, wt, pos))
data_frame = to_dataframe(aux, ["name", "wt", "pos"])
for i in range(len(data_frame)):
    mutated = MutableSeq(pvhl, generic_protein)
    mutated = mutated[0:int(data_frame.loc[i].pos) - 1]
    nombre = data_frame.loc[i].name
    record.append(SeqRecord(Seq(str(mutated)), id = nombre, name="pVHL", description= "pVHL mutation " + nombre))
    print("Success:", nombre)
#Insert
aux = []
for mutacion in data.query("Mutation_type == 'Insertion'").Mutation_aa:
    inicio = mutacion.find("ins") + 3
    aa = mutacion[inicio:]
    pos = int(mutacion.replace("ins","").replace("p.","").replace(aa,""))
    aux.append((mutacion, aa, pos))
data_frame = to_dataframe(aux, ["name", "aa", "pos"])
for i in range(len(data_frame)):
    mutated = MutableSeq(pvhl, generic_protein)
    mutated = mutated[0:int(data_frame.loc[i].pos)-1] + data_frame.loc[i].aa + mutated[int(data_frame.loc[i].pos)-1:]
    nombre = data_frame.loc[i].name
    record.append(SeqRecord(Seq(str(mutated)), id = nombre, name="pVHL", description= "pVHL mutation " + nombre))
    print("Success:", nombre)
#Range Deletions
aux = []
for mutacion in data.query("Mutation_type == 'Range Deletion'").Mutation_aa:
    guion = mutacion.find("_")
    aa_inicial = mutacion[2]
    pos_inicial = mutacion[3:guion]
    aa_final = mutacion[guion + 1]
    pos_final = mutacion[guion+2:-3]
    aux.append((mutacion, aa_inicial, pos_inicial, aa_final, pos_final))
data_frame = to_dataframe(aux, ["name", "aa_inicial", "pos_inicial", "aa_final", "pos_final"])
for i in range(len(data_frame)):
    mutated = MutableSeq(pvhl, generic_protein)
    mutated = mutated[0:int(data_frame.loc[i].pos_inicial)-1] + mutated[int(data_frame.loc[i].pos_final):]
    nombre = data_frame.loc[i].name
    record.append(SeqRecord(Seq(str(mutated)), id = nombre, name="pVHL", description= "pVHL mutation " + nombre))
    print("Success:", nombre)
#Deletion Insertion
aux = []
for mutacion in data.query("Mutation_type == 'Deletion Insertion'").Mutation_aa:
    guion = mutacion.find("_")
    deletion = mutacion.find("del")
    insertion = mutacion.find("ins")
    pos_inicial = mutacion[3:guion]
    aa_inicial = mutacion[2]
    pos_final = mutacion[guion+2:deletion]
    aa_final = mutacion[guion+1]
    aa_insert = mutacion[insertion+3:]
    aux.append((mutacion, aa_inicial, pos_inicial, aa_final, pos_final, aa_insert))
data_frame = to_dataframe(aux, ["name", "aa_inicial", "pos_inicial", "aa_final", "pos_final", "aa_insert"])
for i in range(len(data_frame)):
    mutated = MutableSeq(pvhl, generic_protein)
    mutated = mutated[0:int(data_frame.loc[i].pos_inicial)-1] + data_frame.loc[i].aa_insert + mutated[int(data_frame.loc[i].pos_final):]
    nombre = data_frame.loc[i].name
    record.append(SeqRecord(Seq(str(mutated)), id = nombre, name="pVHL", description= "pVHL mutation " + nombre))
    print("Success:", nombre)
SeqIO.write(record, "../Mutaciones/pVHL_mutations.fna", "fasta")