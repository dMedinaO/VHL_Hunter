import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("../datasets/SubstitutionPosition.csv", sep = ",")
a = np.array(data.sum(axis = 0))
df = pd.DataFrame(columns = np.arange(1, 214, 1))
df.loc[0] = a
df.to_csv("../datasets/hist-pos.csv", sep = ",", index = False)