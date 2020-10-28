import pandas as pd
import sys

dataset = pd.read_csv(sys.argv[1])

file_export = open(sys.argv[2]+"fasta_sequences.fasta", 'w')

for i in range(len(dataset)):
	line = ">Sequence_"+str(i+1)
	file_export.write(line+"\n")

	sequence = dataset['sequence'][i]
	sequence = sequence.replace(" ", "")
	sequence = sequence.replace("O", "")
	sequence = sequence.replace("X", "")
	if i == len(dataset)-1:
		file_export.write(sequence)
	else:
		file_export.write(sequence+"\n")

file_export.close()