import pandas as pd
import sys

#get frequency of residues
def get_frequency(sequence, array_data, dict_residues):

	array_summary = [0 for x in range(20)]
	index=0

	for residue in array_data:
		cont=0
		for residue_data in sequence:
			if residue == residue_data:
				cont+=1
		frequency = float(cont)/float(len(sequence))
		array_summary[index] = frequency
		index+=1

	row_encoding_data = [array_summary[dict_residues[residue]] for residue in sequence]	
	return row_encoding_data

dataset = pd.read_csv(sys.argv[1])
path_output = sys.argv[2]

matrix_encoding = []
length_data = []
index_sequences = []

residues = ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]
residues.sort()
dict_residues = {}
for i in range(len(residues)):
	dict_residues.update({residues[i]:i})

print("Encoding sequences")
index=0
for sequence in dataset['sequence']:
	index_sequences.append([index, sequence])

	sequence = sequence.replace(" ", "")
	sequence = sequence.replace("O", "")
	sequence = sequence.replace("X", "")
	row_encoding = get_frequency(sequence, residues, dict_residues)
	
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
dataset.to_csv(path_output+"encoding_frequency.csv", index=False)

dataIndex = pd.DataFrame(index_sequences, columns=["index_pos", "sequence"])
dataIndex.to_csv(path_output+"index_sequences.csv", index=False)