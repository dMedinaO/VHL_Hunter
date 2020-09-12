from Bio import SeqIO
from Bio.Seq import MutableSeq
import pandas as pd
from Bio.Alphabet import generic_protein
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import numpy as np
#Este script toma una mutación y devuelve un .fasta con todas las proteínas mutadas
try:
    pvhl = str(list(SeqIO.parse("../Proteina/pvhl.fna", "fasta"))[0].seq)
    print(pvhl)
except: 
    print("Error in .fasta format")
    exit()
data = pd.read_csv("../Datasets/dataset.csv", sep = "\t")
record = []
#Partimos con las missense
xd = []
for i in data.query("Mutation_type == 'Missense'").Mutation_aa:
    wt = i[2]
    mut = i[-1]
    pos = i.replace(wt, "").replace(mut,"").replace("p.","")
    xd.append((wt, pos, mut))
mutaciones = np.array(xd)
data_frame = pd.DataFrame(mutaciones, columns = ["wt", "pos", "mut"])
data_frame.drop_duplicates(inplace = True)
data_frame.reset_index(inplace=True)
data_frame.drop("index", axis = 1, inplace = True)
record = []
for i in range(len(data_frame)):
    mutated = MutableSeq(pvhl, generic_protein)
    mutated[int(data_frame.loc[i].pos) - 1] = data_frame.loc[i].mut
    nombre = str(data_frame.loc[i].wt) + str(data_frame.loc[i].pos) + str(data_frame.loc[i].mut)
    record.append(SeqRecord(Seq(str(mutated)), id = "p." + nombre, name="pVHL", description= "pVHL mutation p." + nombre))
    print("Success: p."+ str(data_frame.loc[i].wt), (data_frame.loc[i].pos), str(data_frame.loc[i].mut), sep = "")
#Nonsense
xd = []
for i in data.query("Mutation_type == 'Nonsense'").Mutation_aa:
    wt = i[2]
    pos = i.replace(wt, "").replace("p.","").replace("X","")
    xd.append((wt, pos))
mutaciones = np.array(xd)
data_frame = pd.DataFrame(mutaciones, columns = ["wt", "pos"])
data_frame.drop_duplicates(inplace = True)
data_frame.reset_index(inplace=True)
data_frame.drop("index", axis = 1, inplace = True)
for i in range(len(data_frame)):
    mutated = MutableSeq(pvhl, generic_protein)
    mutated = mutated[0:int(data_frame.loc[i].pos) - 1]
    nombre = str(data_frame.loc[i].wt) + str(data_frame.loc[i].pos) + "X"
    record.append(SeqRecord(Seq(str(mutated)), id = "p." + nombre, name="pVHL", description= "pVHL mutation p." + nombre))
    print("Success: p."+ str(data_frame.loc[i].wt), (data_frame.loc[i].pos), "X", sep = "")
#Simple Delete
xd = []
for i in data.query("Mutation_type == 'Nonsense'").Mutation_aa:
    wt = i[2]
    pos = i.replace(wt, "").replace("p.","").replace("X","")
    xd.append((wt, pos))
mutaciones = np.array(xd)
data_frame = pd.DataFrame(mutaciones, columns = ["wt", "pos"])
data_frame.drop_duplicates(inplace = True)
data_frame.reset_index(inplace=True)
data_frame.drop("index", axis = 1, inplace = True)
for i in range(len(data_frame)):
    mutated = MutableSeq(pvhl, generic_protein)
    mutated = mutated[0:int(data_frame.loc[i].pos) - 1]
    nombre = str(data_frame.loc[i].wt) + str(data_frame.loc[i].pos) + "X"
    record.append(SeqRecord(Seq(str(mutated)), id = "p." + nombre, name="pVHL", description= "pVHL mutation p." + nombre))
    print("Success: p."+ str(data_frame.loc[i].wt), (data_frame.loc[i].pos), "X", sep = "")
#Insert
xd = []
for i in data.query("Mutation_type == 'Insertion'").Mutation_aa:
    inicio = i.find("ins") + 3
    aa = i[inicio:]
    pos = int(i.replace("ins","").replace("p.","").replace(aa,""))
    xd.append((aa, pos))
mutaciones = np.array(xd)
data_frame = pd.DataFrame(mutaciones, columns = ["aa", "pos"])
data_frame.drop_duplicates(inplace = True)
data_frame.reset_index(inplace=True)
data_frame.drop("index", axis = 1, inplace = True)
for i in range(len(data_frame)):
    mutated = MutableSeq(pvhl, generic_protein)
    mutated = mutated[0:int(data_frame.loc[i].pos)-1] + data_frame.loc[i].aa + mutated[int(data_frame.loc[i].pos)-1:]
    nombre = str(data_frame.loc[i].pos) + "ins" + str(data_frame.loc[i].aa) 
    record.append(SeqRecord(Seq(str(mutated)), id = "p." + nombre, name="pVHL", description= "pVHL mutation p." + nombre))
    print("Success: p."+ nombre , sep = "")
#Range Deletions
xd = []
for i in data.query("Mutation_type == 'Range Deletion'").Mutation_aa:
    guion = i.find("_")
    pos_inicial = i[3:guion]
    pos_final = i[guion+2:-3]
    xd.append((i[2], pos_inicial, i[guion+1], pos_final))
mutaciones = np.array(xd)
data_frame = pd.DataFrame(mutaciones, columns = ["aa_inicial", "pos_inicial", "aa_final", "pos_final"])
data_frame.drop_duplicates(inplace = True)
data_frame.reset_index(inplace=True)
data_frame.drop("index", axis = 1, inplace = True)
for i in range(len(data_frame)):
    mutated = MutableSeq(pvhl, generic_protein)
    mutated = mutated[0:int(data_frame.loc[i].pos_inicial)-1] + mutated[int(data_frame.loc[i].pos_final):]
    nombre = data_frame.loc[i].aa_inicial + str(data_frame.loc[i].pos_inicial) + "_" + data_frame.loc[i].aa_inicial +  data_frame.loc[i].pos_final + "del"
    record.append(SeqRecord(Seq(str(mutated)), id = "p." + nombre, name="pVHL", description= "pVHL mutation p." + nombre))
    print("Success: p."+ nombre , sep = "")
#Deletion Insertion
xd = []
for i in data.query("Mutation_type == 'Deletion Insertion'").Mutation_aa:
    guion = i.find("_")
    deletion = i.find("del")
    insertion = i.find("ins")
    pos_inicial = i[3:guion]
    aa_inicial = i[2]
    pos_final = i[guion+2:deletion]
    aa_final = i[guion+1]
    aa_insert = i[insertion+3:]
    xd.append((aa_inicial, pos_inicial, aa_final, pos_final, aa_insert))
mutaciones = np.array(xd)
data_frame = pd.DataFrame(mutaciones, columns = ["aa_inicial", "pos_inicial", "aa_final", "pos_final", "aa_insert"])
data_frame.drop_duplicates(inplace = True)
data_frame.reset_index(inplace=True)
data_frame.drop("index", axis = 1, inplace = True)
for i in range(len(data_frame)):
    mutated = MutableSeq(pvhl, generic_protein)
    mutated = mutated[0:int(data_frame.loc[i].pos_inicial)-1] + data_frame.loc[i].aa_insert + mutated[int(data_frame.loc[i].pos_final):]
    nombre = data_frame.loc[i].aa_inicial + str(data_frame.loc[i].pos_inicial) + "_" + data_frame.loc[i].aa_inicial +  data_frame.loc[i].pos_final + "delins" + data_frame.loc[i].aa_insert
    record.append(SeqRecord(Seq(str(mutated)), id = "p." + nombre, name="pVHL", description= "pVHL mutation p." + nombre))
    print("Success: p."+ nombre , sep = "")

SeqIO.write(record, "../Mutaciones/pVHL_mutations.fna", "fasta")
