from Bio import SeqIO
from Bio.Seq import MutableSeq
import pandas as pd
from Bio.Alphabet import generic_protein
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import argparse
import numpy as np
parser = argparse.ArgumentParser()
parser.add_argument("mutations", help = ".csv with mutations described in columns wt;col;mut (wild type aminoacid, position in chain and mutated aminoacid)")
parser.add_argument("protein", help = ".fasta file with a protein to mutate")
args = parser.parse_args()
try:
    pvhl = str(list(SeqIO.parse(args.protein, "fasta"))[0].seq)
except:
    print("Error in .fasta format")
    exit()
mutations = pd.read_csv(args.mutations, sep = ";")
if(len(mutations.columns) != 3):
    print("Error in .csv format")
    exit()
else:
    if(np.array(mutations.columns) != np.array(["wt", "pos", "mut"])).any():
        print("Error in .csv format")
        exit()
mutations.replace(np.nan, " ", inplace =True)
record = []
for i in range(len(mutations)):
    mutated = MutableSeq(pvhl, generic_protein)
    if(mutated[int(mutations.loc[i].pos) - 1] == mutations.loc[i].wt):
        mutated[int(mutations.loc[i].pos) - 1] = mutations.loc[i].mut
        nombre = str(mutations.loc[i].wt) + str(mutations.loc[i].pos) + str(mutations.loc[i].mut)
        record.append(SeqRecord(Seq(str(mutated)), id = "p." + nombre, name="pVHL", description= "pVHL mutation p." + nombre))
        print("Success: p."+ str(mutations.loc[i].wt), (mutations.loc[i].pos), str(mutations.loc[i].mut))
    else:
        print("Error: p." + str(mutations.loc[i].wt), (mutations.loc[i].pos), str(mutations.loc[i].mut) +  " Not found")
SeqIO.write(record, "pVHL_mutations.fna", "fasta")
