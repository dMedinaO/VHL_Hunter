from Bio import SeqIO
from Bio.Seq import MutableSeq
import pandas as pd
from Bio.Alphabet import generic_protein
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
#Este script ve cual es el aminoácido que sale en la mutación
#y verifica si realmente está correcto
try:
    pvhl = str(list(SeqIO.parse("pvhl.fna", "fasta"))[0].seq)
    print(pvhl)
except: 
    print("Error in .fasta format")
    exit()
print(pvhl)
aminoacidos ={"Ala":"A","Arg":"R","Asn":"N","Asp":"D","Cys":"C",
             "Gln":"Q","Glu":"E","Gly":"G","His":"H","Ile":"I",
             "Leu":"L","Lys":"K","Met":"M","Phe":"F","Pro":"P",
             "Ser":"S","Thr":"T","Trp":"W","Tyr":"Y","Val":"V"}
missense = pd.read_csv("../Depuradas/Nonsense_buenos.csv", sep = "\t")
length = missense.shape[0]
malos = []
cont = 0
for i in range(length):
    mutacion = missense["Mutation_aa"][i]
    wt = mutacion[2] + mutacion[3] +  mutacion[4]
    pos = int(mutacion.replace(wt, "").replace("p.", "").replace("X", ""))
    if(pvhl[pos-1] != aminoacidos.get(wt)):
        malos.append(i)
    else:
        cont += 1
    print(cont)
print("Error:",malos)
