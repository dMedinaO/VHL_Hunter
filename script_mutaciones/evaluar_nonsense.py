import numpy as np
import pandas as pd
from Bio import SeqIO
from Bio.Seq import MutableSeq
from Bio.Alphabet import generic_protein
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
#Este script toma los números y ve cual es el aminoácido que está en esa posción
#Deja el dato como nomenclatura de mutación
data = pd.read_csv("../Depuradas/Nonsense_malos.csv", sep = "\t")
try:
    pvhl = str(list(SeqIO.parse("pvhl.fna", "fasta"))[0].seq)
    print(pvhl)
except: 
    print("Error in .fasta format")
    exit()
length = data.shape[0]
malos = []
aminoacidos = {"A":"Ala","R":"Arg","N":"Asn","D":"Asp","C":"Cys",
               "Q":"Gln","E":"Glu","G":"Gly","H":"His","I":"Ile",
               "L":"Leu","K":"Lys","M":"Met","F":"Phe","P":"Pro",
               "S":"Ser","T":"Thr","W":"Trp","Y":"Tyr","V":"Val"}
for i in range(length):
    pos = data["Mutation_aa"][i]
    try:
        data.loc[i, "Mutation_aa"] = str("p." + aminoacidos[pvhl[pos-1]] + str(pos) + "X")
    except:
        malos.append(i)
print("Error:", malos)
data.drop(malos, inplace = True)
data = data.reset_index()
data.drop(["index"], axis = 1, inplace = True)
data.to_csv("../Depuradas/Nonsense_evaluados.csv", sep = "\t", index = False)