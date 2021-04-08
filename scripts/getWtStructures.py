import os
import subprocess
import pandas as pd
output = str(subprocess.run(["ls", "../structures/"], capture_output=True).stdout).replace("b'", "").replace("1lm8_", "").replace(".pdb", "").split("\\n")
lista = []
listWts = []
for j in output:
    if(len(j) > 1):
        lista.append(j[:-1])
listWts = list(set(lista))
listDicts = []
for i in listWts:
    listDicts.append({"pos": int(i[1:]), "wild": i[0]})
data = pd.DataFrame(listDicts)
data.sort_values(by = "pos", inplace=True)
data.to_csv("../datasets/sequenceWild.csv", index=False)