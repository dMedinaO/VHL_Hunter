from Bio import SeqIO
import pandas as pd
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Seq import MutableSeq
cds_vhl = str(list(SeqIO.parse("../Secuencias/VHL_cds.fna", "fasta"))[0].seq)
pvhl = str(list(SeqIO.parse("../Secuencias/pvhl.fna", "fasta"))[0].seq)
mutaciones = pd.read_csv("../Datasets/Data.csv", sep = "\t")
for i, mutacion in enumerate(mutaciones.query("Mutation_type == 'Range_Deletion (nt)'").Mutation.drop_duplicates()):
    #print(i, mutacion)
    temp = mutacion.replace("c.", "").replace("del", "").split("_")
    ini = int(temp[0])
    fin = int(temp[1])
    delta = fin - ini + 1
    seq = cds_vhl[:ini-1]+cds_vhl[fin:]
    while(len(seq) %3 != 0):
        seq += "N"
    mutpVHL = Seq(str(seq)).translate(to_stop=True)
    print(mutacion)
    print(mutpVHL)
    record = []
    record.append(SeqRecord(mutpVHL, id = mutacion, name = "pVHL", description = "pVHL " + mutacion))
    SeqIO.write(record, "../Resultados/Range_Deletion (nt)/" + mutacion + ".fasta", "fasta")
    
for i, mutacion in enumerate(mutaciones.query("Mutation_type == 'Single_Deletion (nt)'").Mutation.drop_duplicates()):
    #print(i, mutacion)
    temp = mutacion.replace("c.", "").replace("del", "")
    pos = int(temp)
    seq = cds_vhl[:pos-1] + cds_vhl[pos:]
    while(len(seq) %3 != 0):
        seq += "N"
    mutpVHL = Seq(str(seq)).translate(to_stop=True)
    print(mutacion)
    print(mutpVHL)
    record = []
    record.append(SeqRecord(mutpVHL, id = mutacion, name = "pVHL", description = "pVHL " + mutacion))
    SeqIO.write(record, "../Resultados/Single_Deletion (nt)/" + mutacion + ".fasta", "fasta")

for i, mutacion in enumerate(mutaciones.query("Mutation_type == 'Insertion (nt)'").Mutation.drop_duplicates()):
    #print(i, mutacion)
    temp = mutacion.replace("c.", "").split("ins")
    pos = int(temp[0])
    seq = cds_vhl[:pos-1] + temp[1] + cds_vhl[pos-1:]
    while(len(seq) %3 != 0):
        seq += "N"
    mutpVHL = Seq(str(seq)).translate(to_stop=True)
    print(mutacion)
    print(mutpVHL)
    record = []
    record.append(SeqRecord(mutpVHL, id = mutacion, name = "pVHL", description = "pVHL " + mutacion))
    SeqIO.write(record, "../Resultados/Insertion (nt)/" + mutacion + ".fasta", "fasta")

for i, mutacion in enumerate(mutaciones.query("Mutation_type == 'Missense'").Mutation.drop_duplicates()):
    temp = mutacion.replace("p.","")
    wt = temp[0]
    mut = temp[-1]
    pos = int(temp.replace(wt,"").replace(mut,""))
    seq = (pvhl[:pos-1] + mut + pvhl[pos:])
    print(mutacion)
    print(seq)
    record = []
    record.append(SeqRecord(mutpVHL, id = mutacion, name = "pVHL", description = "pVHL " + mutacion))
    SeqIO.write(record, "../Resultados/Missense/" + mutacion + ".fasta", "fasta")

for i, mutacion in enumerate(mutaciones.query("Mutation_type == 'Nonsense'").Mutation.drop_duplicates()):
    temp = mutacion.replace("p.","")
    wt = temp[0]
    pos = int(temp.replace(wt,"").replace("X",""))
    seq = pvhl[:pos-1]
    print(mutacion)
    print(seq)
    record = []
    record.append(SeqRecord(mutpVHL, id = mutacion, name = "pVHL", description = "pVHL " + mutacion))
    SeqIO.write(record, "../Resultados/Nonsense/" + mutacion + ".fasta", "fasta")

for i, mutacion in enumerate(mutaciones.query("Mutation_type == 'Insertion (aa)'").Mutation.drop_duplicates()):
    temp = mutacion.replace("p.", "").split("ins")
    pos = int(temp[0])
    seq = pvhl[:pos-1] + temp[1] + pvhl[pos-1:]
    print(mutacion)
    print(seq)
    record = []
    record.append(SeqRecord(mutpVHL, id = mutacion, name = "pVHL", description = "pVHL " + mutacion))
    SeqIO.write(record, "../Resultados/Insertion (aa)/" + mutacion + ".fasta", "fasta")

for i, mutacion in enumerate(mutaciones.query("Mutation_type == 'Range_Deletion (aa)'").Mutation.drop_duplicates()):
    temp = mutacion.replace("p.", "").replace("del","").split("_")
    pos = int(temp[0])
    pos2 = int(temp[1])
    seq = pvhl[:pos-1] + pvhl[pos2-1:]
    print(mutacion)
    print(seq)
    record = []
    record.append(SeqRecord(mutpVHL, id = mutacion, name = "pVHL", description = "pVHL " + mutacion))
    SeqIO.write(record, "../Resultados/Range_Deletion (aa)/" + mutacion + ".fasta", "fasta")

for i, mutacion in enumerate(mutaciones.query("Mutation_type == 'Single_Deletion (aa)'").Mutation.drop_duplicates()):
    temp = mutacion.replace("p.", "").replace("del","")
    pos = int(temp[0])
    seq = pvhl[:pos-1] + pvhl[pos-1:]
    print(mutacion)
    print(seq)
    record = []
    record.append(SeqRecord(mutpVHL, id = mutacion, name = "pVHL", description = "pVHL " + mutacion))
    SeqIO.write(record, "../Resultados/Single_Deletion (aa)/" + mutacion + ".fasta", "fasta")