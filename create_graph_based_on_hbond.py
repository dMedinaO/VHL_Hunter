import pandas as pd
from Bio.PDB.PDBParser import PDBParser
import networkx as nx
from networkx.algorithms import approximation
import json
import os
import matplotlib.pyplot as plt
import tqdm
def get_edges_from_line(line_hbond_file):
	data_values = line_hbond_file.split("       ")
	node1 = data_values[0].split(" ")
	node1 = [value for value in node1 if str(value)!= "" and "(" not in str(value) and ")" not in str(value)]
	node2 = data_values[1].split(" ")
	node2 = [value for value in node2 if str(value)!= "" and "(" not in str(value) and ")" not in str(value)]
	node1 = node1[1]+"-"+str(node1[0])
	node2 = node2[-2]+"-"+str(node2[-1])
	
	return node1, node2
	
main = os.listdir(path = "PDB")
for m in main:
	pdbs = os.listdir(path = "PDB/" + m)
	for p in tqdm.tqdm(pdbs):
		datafile = "HydrogenBonds/" + m + "/" + p.replace("pdb", "txt")
		pdb_file = "PDB/" + m + "/" + p
		path_output = "ConectivityGraphs/" + m + "/" + p.replace("pdb", "json")

		#read pdb and get information about residues
		residues_in_pdb = []

		parser = PDBParser()#creamos un parse de pdb
		structure = parser.get_structure("1lm8", pdb_file)#trabajamos con la proteina cuyo archivo es 1AQ2.pdb

		for model in structure:
			for chain in model:
				for residue in chain:
					if residue.resname in ['ALA', 'LYS', 'ARG', 'HIS', 'PHE', 'THR', 'PRO', 'MET', 'GLY', 'ASN', 'ASP', 'GLN', 'GLU', 'SER', 'TYR', 'TRP', 'VAL', 'ILE', 'LEU', 'CYS']:
						res_value = residue.resname+"-"+str(residue.id[1])
						residues_in_pdb.append(res_value)

		graph_data = nx.Graph()
		for residue in residues_in_pdb:
			graph_data.add_node(residue)
		#parser HBond File
		file_open = open(datafile, 'r')
		line = file_open.readline()
		while line:
			if(str(line[0:2]) == "  "):
				line = line.replace("\n", "")
				#get information for line
				node1, node2 = get_edges_from_line(line)
				#add edge
				if "HOH" not in node1 and "HOH" not in node2:
					graph_data.add_edge(node1, node2)
			line = file_open.readline()	
		file_open.close()
		data = nx.algorithms.approximation.connectivity.all_pairs_node_connectivity(graph_data)
		with open(path_output, 'w') as file:
			json.dump(data, file, indent=2)