from Bio import SeqIO
import pandas as pd
from Bio.Alphabet import generic_dna, generic_rna, generic_protein
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
seccionesMRNA = [[1,410],[4737,4859],[8010,11890]]
seccionesCNS = [[71,410],[4737,4859],[8010,8188]]
genVHL = str(list(SeqIO.parse("../Secuencias/GRCh38_p13.fasta", "fasta"))[0].seq)
pvhl = str(list(SeqIO.parse("../Secuencias/pvhl.fna", "fasta"))[0].seq)
mRNA = ""
adn = ""
for i, seccion in enumerate(seccionesMRNA):
    inicio = seccion[0] - 1
    fin = seccion[1]
    adn += genVHL[inicio:fin]
    rna =  Seq(genVHL[inicio:fin], generic_dna).transcribe()
    mRNA += rna
inicio = 70
fin = -3702
record = []
print(mRNA[inicio:fin-3].translate())
if(mRNA[inicio:fin-3].translate() == pvhl):
    print("Traducción correcta")
    cds = mRNA[inicio:fin-3].back_transcribe()
    record.append(SeqRecord(Seq(str(cds)), id = "VHL suppresor (cds)", name="VHL suppresor", description= "VHL suppresor cds"))
    SeqIO.write(record, "../Secuencias/VHL_cds.fna", "fasta")
    print("../Secuencias/VHL_cds.fna")