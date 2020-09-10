from Bio import SeqIO
from Bio.Seq import MutableSeq
import pandas as pd
from Bio.Alphabet import generic_protein
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

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
silent = pd.read_csv("../Depuradas/Silent_vhldb.csv", sep = "\t")
length = silent.shape[0]
malos = []
cont = 0
for i in range(length):
    mutacion = silent["Mutation_aa"][i]
    wt = mutacion[2] + mutacion[3] +  mutacion[4]
    pos = int(mutacion.replace(wt, "").replace("p.", ""))
    if(pvhl[pos-1] != aminoacidos.get(wt)):
        malos.append(i)
silent.drop(malos, inplace = True)
silent.to_csv("../Depuradas/Silent_evaluados.csv", sep = "\t", index = False)