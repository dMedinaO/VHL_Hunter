import pandas as pd
import os
import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
main = os.listdir("csv")
_1lm8 = pd.read_csv("1lm8.csv", sep = ";")
_1lm8NumberHbonds = len(_1lm8.values)
_1lm8EnergyHbonds = _1lm8.weight.sum()
sdm = pd.read_csv("sdm/chain_v_sdm.csv", sep=",")[["Mutation", "Predicted_ddg"]]
df = pd.DataFrame(columns = ["Mutation", "dHbonds", "dEnergy", "Predicted_ddg"])
for filename in main:
    mut = filename.replace(".csv", "").replace("1lm8_V_", "")
    query = "Mutation == '" + mut + "'"
    ddg = float(sdm.query(query).Predicted_ddg)
    ruta = "csv/" + filename
    data = pd.read_csv(ruta, sep = ";")
    dHbonds = _1lm8NumberHbonds - len(data.values)
    dEnergy = round(_1lm8EnergyHbonds - data.weight.sum(), 3)
    row = {"Mutation": mut, "dHbonds": dHbonds, "dEnergy": dEnergy, "Predicted_ddg": ddg}
    df = df.append(row, ignore_index = True)
df.to_csv("DatasetDDG.csv", index=False)