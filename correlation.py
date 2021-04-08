import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("DatasetDDG.csv")
min = (float(data[["Predicted_ddg"]].min()))
max = (float(data[["Predicted_ddg"]].max()))
categorias = np.sort(list(set(data.dHbonds)))
for ii, i in enumerate(categorias):
    query = "dHbonds == " + str(i)
    hbonds_ddg = np.array(data.query(query)[["Predicted_ddg"]])
    if(i > 0):
        title = "+" + str(i)
    else:
        title = str(i)
    plt.title(title)
    plt.hist(hbonds_ddg, bins = np.linspace(min, max, num = 12))
    plt.xlabel(r"$\Delta$$\Delta$G")
    fig = plt.gcf()
    fig.set_size_inches((12, 8.5), forward=False)
    plt.savefig("Views/DDG_Hbonds_" + title + ".png")
    plt.close()
diccionario = {}
for ij, j in enumerate(categorias):
    query = "dHbonds == " + str(j)
    hbonds_ddg = data.query(query)["Predicted_ddg"]
    diccionario[j] = np.array(hbonds_ddg)
plt.boxplot(diccionario.values())
plt.xticks(np.arange(1, len(categorias)+1), categorias)
plt.xlabel(r"$\Delta$Hydrogen bonds")
plt.ylabel(r"$\Delta$$\Delta$G")
fig = plt.gcf()
fig.set_size_inches((12, 8.5), forward=False)
plt.savefig("Views/Boxplot_DDG_Hbonds.png")
