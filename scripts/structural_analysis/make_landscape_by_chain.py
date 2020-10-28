import sys
from Bio.PDB.PDBParser import PDBParser
import os

pdb_file = sys.argv[1]
path_output = sys.argv[2]

parser = PDBParser()#creamos un parse de pdb
structure = parser.get_structure("1lm8", pdb_file)#trabajamos con la proteina cuyo archivo es 1AQ2.pdb

residues_in_pdb = []

chain_data = []
for model in structure:
	for chain in model:
		for residue in chain:
			if residue.resname in ['ALA', 'LYS', 'ARG', 'HIS', 'PHE', 'THR', 'PRO', 'MET', 'GLY', 'ASN', 'ASP', 'GLN', 'GLU', 'SER', 'TYR', 'TRP', 'VAL', 'ILE', 'LEU', 'CYS']:
				res_value = chain.id + "-"+residue.resname+"-"+str(residue.id[1])
				residues_in_pdb.append(res_value)
		chain_data.append(chain.id)

dic_residues = {'ALA':'A', 'ARG':'R', 'ASN':'N','ASP':'D', 'CYS':'C', 'GLU':'E', 'GLN':'Q', 'GLY':'G','HIS':'H', 'ILE':'I', 'LEU':'L', 'LYS':'K', 'MET':'M', 'PHE':'F', 'PRO':'P', 'SER':'S', 'THR':'T', 'TRP':'W', 'TYR':'Y','VAL':'V'}

#make a directory
for chain in chain_data:
	command = "mkdir -p %s%s_chain_landscape" % (path_output, chain)
	print(command)
	os.system(command)

	#generate landscape for each residue in chain
	residues_in_chain = []
	for residue in residues_in_pdb:
		values = residue.split("-")
		if values[0] == chain:
			residues_in_chain.append(values)

	print(len(residues_in_chain))

	landscape_for_chain = []

	for element in residues_in_chain:

		for residue in dic_residues:
			if element[1] != residue:

				mutation = "%s %s%s%s" % (chain, dic_residues[element[1]], element[2], dic_residues[residue])
				landscape_for_chain.append(mutation)

	
	file_output = open(path_output+chain+"_chain_landscape/landscape_data.txt", 'w')
	for i in range(len(landscape_for_chain)):
		if i == len(landscape_for_chain)-1:
			file_output.write(landscape_for_chain[i])
		else:
			file_output.write(landscape_for_chain[i]+"\n")

	file_output.close()



