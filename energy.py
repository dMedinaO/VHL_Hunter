import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_csv("DatasetDDG.csv")[["dEnergy", "Predicted_ddg"]]
print(data)
min = int(round(data.dEnergy.min()))
max = int(round(data.dEnergy.max()))
bins = np.arange(min, max)
for i in bins:
    rango = (str(i), str(i+1))
    query = "dEnergy > " + rango[0] + " and dEnergy <= " + rango[1]
    energy_ddg = np.array(data.query(query)[["Predicted_ddg"]])
    plt.title(r" Hbond's $\Delta$Energy $\in$(" + rango[0] + "," + rango[1]+ "]")
    plt.hist(energy_ddg, bins = np.linspace(bins.min(), bins.max(), num = 2*(bins.max() - bins.min())+1))
    plt.xlabel(r"$\Delta$$\Delta$G")
    fig = plt.gcf()
    fig.set_size_inches((12, 8.5), forward=False)
    plt.savefig("Views/DDG_Energy_" + rango[0] + "_" + rango[1] + ".png")
    plt.close()

diccionario = {}
for ij, j in enumerate(bins):
    rango = (str(j), str(j+1))
    query = "dEnergy > " + rango[0] + " and dEnergy <= " + rango[1]
    hbonds_ddg = data.query(query)["Predicted_ddg"]
    diccionario[j] = np.array(hbonds_ddg)
plt.boxplot(diccionario.values())
plt.xlabel(r"Hbond's $\Delta$ Energy")
plt.ylabel(r"$\Delta$$\Delta$G")
lista = ["("+ str(k) + "," + str(k+1) + "]" for k in diccionario.keys()]
plt.xticks(np.arange(1, len(lista) + 1),lista)
fig = plt.gcf()
fig.set_size_inches((12, 8.5), forward=False)
plt.savefig("Views/Boxplot_DDG_Energy.png")
