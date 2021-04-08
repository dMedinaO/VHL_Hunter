import pandas as pd
from Bio.PDB.PDBParser import PDBParser
import networkx as nx
from networkx.algorithms import approximation
import json
import os
import matplotlib.pyplot as plt
import tqdm
main = os.listdir("PDB/total_chain_v/")
for filename in tqdm.tqdm(main):
    pathSubGraphs = "SubGraphs/" + filename.replace(".pdb", ".json")
    datafile = pd.read_csv("csv/" + filename.replace(".pdb", ".csv"), sep = ";")
    graph_data = nx.Graph()
    for i in datafile.values:
        node1 = i[0]
        node2 = i[1]
        weight = round(i[2], 3)
        graph_data.add_edge(node1, node2, weight = weight)
    data = nx.to_dict_of_dicts(graph_data)
    with open(pathSubGraphs, 'w') as file:
        json.dump(data, file, indent=2)