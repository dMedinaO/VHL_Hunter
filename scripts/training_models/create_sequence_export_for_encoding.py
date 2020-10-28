import pandas as pd
import sys

def search_sequence_into_dataset(sequence, dataset):

	index=-1

	for i in range(len(dataset)):
		if dataset['seq'][i] == sequence:
			index = i
			break

	return index

dataset1 = pd.read_csv(sys.argv[1], sep="\t")
dataset2 = pd.read_csv(sys.argv[2], sep="\t")
dataset3 = pd.read_csv(sys.argv[3], sep="\t")
dataset4 = pd.read_csv(sys.argv[4], sep="\t")
dataset5 = pd.read_csv(sys.argv[5], sep="\t")
path_output = sys.argv[6]

seq_data_1 = [element for element in list(set(dataset1['seq']))]
seq_data_2 = [element for element in list(set(dataset2['seq']))]
seq_data_3 = [element for element in list(set(dataset3['seq']))]
seq_data_4 = [element for element in list(set(dataset4['seq']))]
seq_data_5 = [element for element in list(set(dataset5['seq']))]

sequence_full = seq_data_1+seq_data_2+seq_data_3+seq_data_4+seq_data_5

sequence_full = list(set(sequence_full))

dataset_export = pd.DataFrame()
dataset_export['sequence'] = sequence_full
dataset_export['index'] = ["variant_"+str(i+1) for i in range(len(sequence_full))]

#export full data encoding
dataset_export.to_csv(path_output+"all_variants.csv", index=False)
