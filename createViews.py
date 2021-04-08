#Caso 1: El puente de hidrógeno está en la mutada pero no en la original
#Caso 2: El puente de hidrógeno está en la original pero no en la mutada
#Caso 3: El puente de hidrógeno está en la mutada y la original con el mismo valor
#Caso 4: El puente de hidrógeno está en la mutada y en la original, pero con menor valor en la mutada
#Caso 5: El puente de hidrógeno está en la mutada y en la original, pero con mayor valor en la mutada
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import os
from tqdm import tqdm as load
main = os.listdir("DiffCsv/")
for filename in load(main):
    original = pd.read_csv("1lm8.csv", sep = ";")
    data = pd.read_csv("DiffCsv/" + filename, sep = ";")
    #Grafo original
    plt.subplot(1, 2, 1)
    plt.title("1LM8(V)")
    g = nx.Graph()
    for i in [2, 4, 5]:
        res = data.query("case == " + str(i)).values
        for j in res:
            if(j[3] != 1):
                g.add_edge(j[0], j[1], weight = round(j[4],3), case = j[3])
            else:
                g.add_edge(j[0], j[1], weight = round(j[2],3), case = j[3])
    pos=nx.shell_layout(g)
    ex = [(u, v) for (u, v, d) in g.edges(data=True) if d["case"] != 1]#Está en la original pero no en la mutada
    labels = nx.get_edge_attributes(g,'weight')
    nx.draw_networkx_edge_labels(g,pos,edge_labels=labels, font_size=6)
    nx.draw_networkx_edges(g, pos, edgelist=ex, edge_color="black", width = 2)
    nx.draw_networkx_nodes(g, pos, node_size = 900, node_color = "gold")
    nx.draw_networkx_labels(g, pos, font_size=6)
    #Grafo mutado
    plt.subplot(1, 2, 2)
    plt.title(filename.replace(".csv", "").replace("_", " ").replace(" V ", "(V) ").upper())
    g.clear()
    for i in [1, 4, 5]:
        res = data.query("case == " + str(i)).values
        for j in res:
            g.add_edge(j[0], j[1], weight = round(j[2],3), case = j[3])
    pos=nx.shell_layout(g)
    e1 = [(u, v) for (u, v, d) in g.edges(data=True) if d["case"] == 1]#Está en la mutada pero no en la original
    e4 = [(u, v) for (u, v, d) in g.edges(data=True) if d["case"] == 4]#Menor valor en la mutada
    e5 = [(u, v) for (u, v, d) in g.edges(data=True) if d["case"] == 5]#Mayor valor en la mutada
    labels = nx.get_edge_attributes(g,'weight')
    nx.draw_networkx_edge_labels(g,pos,edge_labels=labels, font_size=6)
    nx.draw_networkx_edges(g, pos, edgelist=e1, edge_color="black", width = 2)#Está en la mutada pero no en la original
    nx.draw_networkx_edges(g, pos, edgelist=e4, edge_color="skyblue", width = 2, label = "Decreased energy")#Menor valor en la mutada
    nx.draw_networkx_edges(g, pos, edgelist=e5, edge_color="teal", width = 2, label = "Increased energy")#Mayor valor en la mutada
    nx.draw_networkx_nodes(g, pos, node_size = 900, node_color = "gold")
    nx.draw_networkx_labels(g, pos, font_size=6)
    fig = plt.gcf()
    fig.legend()
    fig.set_size_inches((12, 8.5), forward=False)
    fig.savefig("ViewDiffs/" + filename.replace(".csv", ".png"), dpi=500)
    plt.close(fig)