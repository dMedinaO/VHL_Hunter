import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np

def create_pie_chart(dict_values,output):

	plt.clf()
	labels = []
	counts = []

	for key in dict_values:
		labels.append(key)
		counts.append(dict_values[key])
	
	fig1, ax1 = plt.subplots()
	ax1.pie(counts, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

	plt.savefig(output)


dataset = pd.read_csv(sys.argv[1], sep="\t")
path_output = sys.argv[2]

def create_bar_plot(dict_values, output):

	plt.clf()
	# Make fake dataset
	labels = []
	counts = []

	for key in dict_values:
		labels.append(key)
		counts.append(dict_values[key])	
	y_pos = np.arange(len(labels))
	 
	# Create horizontal bars
	y_pos = np.arange(len(labels))
 
	# Create bars
	plt.bar(y_pos, counts)
	
	# Create names on the x-axis
	plt.xticks(y_pos, labels)
	plt.xticks(rotation=90) 
	# Show graphic
	plt.savefig(output)

#count mutations by type of vhl
list_type_vhl = {'VHL: 2B':0, 'VHL: 2':0, 'VHL: 1':0, 'VHL: 2C':0,	'VHL: 2A':0, "non_type_detected":0}

print("Evaluated type VHL")
for i in range(len(dataset)):
	non_efect=0

	for key in list_type_vhl:
		if key != "non_type_detected":
			if dataset[key][i] == 1:
				list_type_vhl[key]+=1
			else:
				non_efect+=1

	if non_efect == 5:
		list_type_vhl["non_type_detected"]+=1

print("Export type_vhl")
create_pie_chart(list_type_vhl, path_output+"summary_vhl_type.png")

#same analysis by type of effect
dict_effect = {}
for key in dataset.keys():
	if "Effect" in key:
		dict_effect.update({key:0})

dict_effect.update({"non_efect_detected":0})

print("Evaluated effect VHL")
for i in range(len(dataset)):
	non_type=0

	for key in dict_effect:
		if key != "non_efect_detected":
			if dataset[key][i] == 1:
				dict_effect[key]+=1
			else:
				non_type+=1

	if non_type == len(dict_effect.keys())-1:
		dict_effect["non_efect_detected"]+=1

print("Export effect VHL")
dataset_export = pd.DataFrame()

dict_keys=[]
counts_keys = []

for key in dict_effect:
	dict_keys.append(key)
	counts_keys.append(dict_effect[key])

dataset_export["effect"] = dict_keys
dataset_export["counts"] = counts_keys
dataset_export.to_csv(path_output+"summary_effects.csv", index=False)
create_bar_plot(dict_effect, path_output+"summary_effects.png")
#summary type 

#get information about number of type possible by 