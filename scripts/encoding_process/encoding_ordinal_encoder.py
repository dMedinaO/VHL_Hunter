import pandas as pd
import sys

dataset = pd.read_csv(sys.argv[1])
path_output = sys.argv[2]

matrix_encoding = []
length_data = []
index_sequences = []
index=0

residues = ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]
residues.sort()
dict_residues = {}
for i in range(len(residues)):
	dict_residues.update({residues[i]:i})

print("Encoding sequences")
for sequence in dataset['sequence']:
	index_sequences.append([index, sequence])

	sequence = sequence.replace(" ", "")
	sequence = sequence.replace("O", "")
	sequence = sequence.replace("X", "")
	print(sequence)
	row_encoding = []

	for residue in sequence:
		residue_encoding = dict_residues[residue]
		row_encoding.append(residue_encoding)

	length_data.append(len(row_encoding))
	matrix_encoding.append(row_encoding)
	index+=1

print("Add zero padding")
#create zero padding
for i in range(len(matrix_encoding)):

	for j in range(len(matrix_encoding[i]),max(length_data)):
		matrix_encoding[i].append(0)

header = ["P_"+str(i) for i in range(len(matrix_encoding[0]))]

dataset = pd.DataFrame(matrix_encoding, columns=header)
dataset.to_csv(path_output+"encoding_Ordinal.csv", index=False)

dataIndex = pd.DataFrame(index_sequences, columns=["index_pos", "sequence"])
dataIndex.to_csv(path_output+"index_sequences.csv", index=False)