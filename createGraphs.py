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
	pos = data_values[2].find("Val=")
	weight = float(data_values[2][pos: pos+12].replace("Val=", ""))
	node1 = node1[1]+"-"+str(node1[2])
	node2 = node2[-2]+"-"+str(node2[-1])
	return node1, node2, weight
main = os.listdir(path = "PDB")
for m in main:
	pdbs = os.listdir(path = "PDB/" + m)
	for p in tqdm.tqdm(pdbs):
		#Rutas
		pathPdb = "PDB/" + m + "/" + p
		pathHydrogenBonds = "HydrogenBonds/" + m + "/" + p.replace("pdb", "txt")
		pathSubGraphs = "SubGraphs/" + m + "/" + p.replace("pdb", "json")
		pathFullGraphs = "FullGraphs/" + m + "/" + p.replace("pdb", "json")
		pathSubImg = "ViewSubGraphs/" + m + "/" + p.replace("pdb", "png")
		pathFullImg = "ViewFullGraphs/" + m + "/" + p.replace("pdb", "png")
		pathConectivityGraphs = "ConectivityGraphs/" + m + "/" + p.replace("pdb", "json")
		datafile= pathHydrogenBonds
		pdb_file = pathPdb
		path_output = pathSubGraphs
		graph_data = nx.Graph()
		#parser HBond File
		file_open = open(datafile, 'r')
		line = file_open.readline()
		while line:
			if(str(line[0:2]) == "  "):
				line = line.replace("\n", "")
				#get information for line
				node1, node2, weight = get_edges_from_line(line)
				#add edge
				if "HOH" not in node1 and "HOH" not in node2:
					graph_data.add_edge(node1, node2, weight = weight)
			line = file_open.readline()	
		file_open.close()
		#data = approximation.connectivity.all_pairs_node_connectivity(graph_data)
		#Exportar
		data = nx.to_dict_of_dicts(graph_data)
		with open(pathSubGraphs, 'w') as file:
			json.dump(data, file, indent=2)
		#Dibujar
		""" plt.figure(figsize = (50, 50))
		pos=nx.spring_layout(graph_data) # pos = nx.nx_agraph.graphviz_layout(G)
		nx.draw_networkx(graph_data,pos, node_size = 1000, font_size=15)
		labels = nx.get_edge_attributes(graph_data,'weight')
		nx.draw_networkx_edge_labels(graph_data,pos,edge_labels=labels)
		plt.axis("off")
		plt.savefig(pathSubImg) """
		#read pdb and get information about residues
		#Agregar nodos del pdb
		residues_in_pdb = []
		parser = PDBParser()#creamos un parse de pdb
		structure = parser.get_structure("1lm8", pdb_file)#trabajamos con la proteina cuyo archivo es 1AQ2.pdb
		for model in structure:
			for chain in model:
				for residue in chain:
					if residue.resname in ['ALA', 'LYS', 'ARG', 'HIS', 'PHE', 'THR', 'PRO', 'MET', 'GLY', 'ASN', 'ASP', 'GLN', 'GLU', 'SER', 'TYR', 'TRP', 'VAL', 'ILE', 'LEU', 'CYS']:
						res_value = residue.resname+"-"+str(residue.id[1])
						residues_in_pdb.append(res_value)
		for residue in residues_in_pdb:
			if(residue not in graph_data.nodes):
				graph_data.add_node(residue)
		#Exportar
		data = nx.to_dict_of_dicts(graph_data)
		with open(pathFullGraphs, 'w') as file:
			json.dump(data, file, indent=2)
		#Dibujar
		""" plt.figure(figsize = (50, 50))
		pos=nx.spring_layout(graph_data) # pos = nx.nx_agraph.graphviz_layout(G)
		nx.draw_networkx(graph_data,pos, node_size = 1000, font_size=15)
		labels = nx.get_edge_attributes(graph_data,'weight')
		nx.draw_networkx_edge_labels(graph_data,pos,edge_labels=labels)
		plt.axis("off")
		plt.savefig(pathFullImg) """
		data = nx.algorithms.approximation.connectivity.all_pairs_node_connectivity(graph_data)
		with open(pathConectivityGraphs, 'w') as file:
			json.dump(data, file, indent=2)