import pandas as pd
import sys
from Bio.PDB.PDBParser import PDBParser
import networkx as nx
#import community as community_louvain
from networkx.algorithms import community
import matplotlib.pyplot as plt

def get_edges_from_line(line_hbond_file):

	data_values = line_hbond_file.split("       ")
	
	node1 = data_values[0].split(" ")
	node1 = [value for value in node1 if str(value)!= "" and "(" not in str(value) and ")" not in str(value)]
	node2 = data_values[1].split(" ")
	node2 = [value for value in node2 if str(value)!= "" and "(" not in str(value) and ")" not in str(value)]

	node1 = node1[1]+"-"+str(node1[0])
	node2 = node2[-2]+"-"+str(node2[-1])
	
	return node1, node2
	
datafile= sys.argv[1]
pdb_file = sys.argv[2]
path_output = sys.argv[3]

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
	line = line.replace("\n", "")

	#get information for line
	node1, node2 = get_edges_from_line(line)
	
	#add edge
	if "HOH" not in node1 and "HOH" not in node2:
		graph_data.add_edge(node1, node2)
	line = file_open.readline()	
file_open.close()

print(graph_data.number_of_nodes())
print(graph_data.number_of_edges())

data = nx.algorithms.approximation.connectivity.all_pairs_node_connectivity(graph_data)
print(data)