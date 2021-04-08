import pandas as pd
import os
import tqdm
#Caso 1: El puente de hidrógeno está en la mutada pero no en la original
#Caso 2: El puente de hidrógeno está en la original pero no en la mutada
#Caso 3: El puente de hidrógeno está en la mutada y la original con el mismo valor
#Caso 4: El puente de hidrógeno está en la mutada y en la original, pero con menor valor en la mutada
#Caso 5: El puente de hidrógeno está en la mutada y en la original, pero con mayor valor en la mutada
_1lm8 = pd.read_csv("1lm8.csv", sep = ";")
dirtables = "csv"
main = os.listdir(path = dirtables)
for filename in tqdm.tqdm(main):
    dfmut = pd.read_csv("csv/" + filename, sep = ";")
    Diff = pd.DataFrame(columns = ["node1", "node2", "weight", "case", "original_weight"])
    for ii, i in enumerate(dfmut.values):
        q = "node1 == '" + i[0] + "' and node2 == '" + i[1] + "' and weight == " + str(i[2])
        query = _1lm8.query(q)
        if(len(query) !=0):
            Diff = Diff.append({"node1": i[0], "node2": i[1], "weight": i[2], "case": 3, "original_weight": i[2]}, ignore_index = True)
        else:
            q = "node1 == '" + i[0] + "' and node2 == '" + i[1] + "'"
            query = _1lm8.query(q)
            if(len(query) !=0):
                if(float(query.weight) > i[2]):
                    Diff = Diff.append({"node1": i[0], "node2": i[1], "weight": i[2], "case": 4, "original_weight": float(query.weight)}, ignore_index = True)
                else:
                    Diff = Diff.append({"node1": i[0], "node2": i[1], "weight": i[2], "case": 5, "original_weight": float(query.weight)}, ignore_index = True)
            if(len(query) == 0):
                Diff = Diff.append({"node1": i[0], "node2": i[1], "weight": i[2], "case": 1}, ignore_index = True)
    for ii, i in enumerate(_1lm8.values):
        q = "node1 == '" + i[0] + "' and node2 == '" + i[1] + "'"
        query = dfmut.query(q)
        if(len(query) == 0):
            Diff = Diff.append({"node1": i[0], "node2": i[1], "weight": i[2], "case": 2, "original_weight": i[2]}, ignore_index = True)
    Diff.to_csv("DiffCsv/" + filename, sep = ";", index = False)