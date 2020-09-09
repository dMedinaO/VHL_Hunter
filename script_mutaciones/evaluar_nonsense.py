import numpy as np
import pandas as pd
from Bio import SeqIO
from Bio.Seq import MutableSeq
from Bio.Alphabet import generic_protein
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
data = pd.read_csv("~/Documentos/VHL_databases/Depuradas/Nonsense_malos.csv", sep = "\t")
try:
    pvhl = str(list(SeqIO.parse("pvhl.fna", "fasta"))[0].seq)
    print(pvhl)
except: 
    print("Error in .fasta format")
    exit()
length = data.shape[0]
malos = []
for i in range(length):
    pos = data["Mutation_aa"][i]
    try:
        data.loc[i, "Mutation_aa"] = str("p." + str(pvhl[pos]) + str(pos) + "X")
    except:
        malos.append(i)
print("malos:", malos)
data.drop(malos, inplace = True)
data.to_csv("Nonsense_evaluados.csv", sep = "\t")