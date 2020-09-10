from Bio import SeqIO
from Bio.Seq import MutableSeq
import pandas as pd
from Bio.Alphabet import generic_protein
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

#Este script ve cuales mutaciones están realmente malas, porque el aminoácido
#wild tipe no corresponde al que se nombra
try:
    pvhl = str(list(SeqIO.parse("pvhl.fna", "fasta"))[0].seq)
    print(pvhl)
except: 
    print("Error in .fasta format")
    exit()
aminoacidos ={"Ala":"A","Arg":"R","Asn":"N","Asp":"D","Cys":"C",
             "Gln":"Q","Glu":"E","Gly":"G","His":"H","Ile":"I",
             "Leu":"L","Lys":"K","Met":"M","Phe":"F","Pro":"P",
             "Ser":"S","Thr":"T","Trp":"W","Tyr":"Y","Val":"V"}
missense = pd.read_csv("../Depuradas/Missense_vhldb.csv", sep = "\t")
length = missense.shape[0]
malos = []
for i in range(length):
    mutacion = missense["Mutation_aa"][i]
    wt = mutacion[2] + mutacion[3] +  mutacion[4]
    mut =  mutacion[-3] +  mutacion[-2] +  mutacion[-1]
    pos = int(mutacion.replace(wt, "").replace(mut, "").replace("p.", ""))
    if(pvhl[pos-1] != aminoacidos.get(wt)):
        malos.append(i)
print("Error:",malos)
missense.drop(malos, inplace = True)
missense.to_csv("../Depuradas/Missense_evaluados.csv", sep = "\t", index = False)