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
aminoacidos ={"Ala":"A","Arg":"R","Asn":"N","Asp":"D","Cys":"C",
             "Gln":"Q","Glu":"E","Gly":"G","His":"H","Ile":"I",
             "Leu":"L","Lys":"K","Met":"M","Phe":"F","Pro":"P",
             "Ser":"S","Thr":"T","Trp":"W","Tyr":"Y","Val":"V"}
data = pd.read_csv("../Depuradas/vhldb_missense_silent_nonsense.csv", sep = "\t")
record = []
#Partimos con las missense
xd = []
for i in data.query("Mutation_type == 'Missense'").Mutation_aa:
    wt = i[2] + i[3] + i[4]
    mut = i[-3] + i[-2] + i[-1]
    pos = i.replace(wt, "").replace(mut,"").replace("p.","")
    xd.append((aminoacidos[wt], pos, aminoacidos[mut]))
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
#Nonsenses
xd = []
for i in data.query("Mutation_type == 'Nonsense'").Mutation_aa:
    wt = i[2] + i[3] + i[4]
    pos = i.replace(wt, "").replace("X","").replace("p.","")
    xd.append((aminoacidos[wt], pos))
mutaciones = np.array(xd)
data_frame = pd.DataFrame(mutaciones, columns = ["wt", "pos"])
data_frame.drop_duplicates(inplace = True)
data_frame.reset_index(inplace=True)
data_frame.drop("index", axis = 1, inplace = True)
for i in range(len(data_frame)):
    mutated = MutableSeq(pvhl, generic_protein)
    mutated[int(data_frame.loc[i].pos) - 1] = "X"
    mutated = mutated[0:int(data_frame.loc[i].pos)] 
    nombre = str(data_frame.loc[i].wt) + str(data_frame.loc[i].pos) + "X"
    record.append(SeqRecord(Seq(str(mutated)), id = "p." + nombre, name="pVHL", description= "pVHL mutation p." + nombre))
    print("Success: p."+ str(data_frame.loc[i].wt), (data_frame.loc[i].pos), "X", sep = "")
SeqIO.write(record, "../Mutaciones/pVHL_mutations.fna", "fasta")
