import pandas as pd
from Bio.PDB.PDBParser import PDBParser
import networkx as nx
from networkx.algorithms import approximation
import json
import os
import matplotlib.pyplot as plt
import tqdm

def get_edges_from_line(line_hbond_file):
    data_values = line_hbond_file.split("      ")
    node1 = data_values[0].split(" ")
    node1 = [value for value in node1 if str(value)!= "" and "(" not in str(value) and ")" not in str(value)]
    node2 = data_values[1].split(" ")
    node2 = [value for value in node2 if str(value)!= "" and "(" not in str(value) and ")" not in str(value)]
    pos = data_values[2].find("Val=")
    weight = float(data_values[2][pos: pos+12].replace("Val=", ""))
    aa_node1 = node1[1]
    aa_node2 = node2[-2]
    num_node1 = node1[2]
    num_node2 = node2[-1]
    if(int(num_node1) < int(num_node2)):
        node1 = aa_node1 + "-" + str(num_node1)
        node2  = aa_node2 + "-" + str(num_node2)
    else:
        node2 = aa_node1 + "-" + str(num_node1)
        node1 = aa_node2 +"-" + str(num_node2)
    return node1, node2, weight
dirHbonds = "HydrogenBonds/total_chain_v"
dirtables = "csv"
main = os.listdir(path = dirHbonds)
for i in tqdm.tqdm(main):
    df = pd.DataFrame(columns = ["node1", "node2", "weight"])
    datafile = i
    file_open = open(dirHbonds + "/" + datafile, 'r')
    line = file_open.readline()
    while line:
        if(str(line[0:2]) == "  "):
            line = line.replace("\n", "")
            node1, node2, weight = get_edges_from_line(line)
            q = "node1 == '" + node1 + "' and node2 == '" + node2 + "'"
            query = df.query(q)
            if(len(query) == 0):
                df  = df.append({"node1": node1, "node2": node2, "weight": weight}, ignore_index = True)
            else:
                df.loc[int(query.index[0]), "weight"] = df.loc[int(query.index[0]), "weight"] + weight
        line = file_open.readline() 
    file_open.close()
    df.sort_values(by = ["node1", "node2"], inplace =True)
    df.to_csv("csv/" + datafile.replace(".txt", ".csv"), sep = ";", index=False)