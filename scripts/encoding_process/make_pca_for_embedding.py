import pandas as pd
import numpy as np
import sys
from scipy.spatial import distance
from sklearn.decomposition import PCA
from sklearn import preprocessing

def numpy_array_to_array (data):

	array_data = []

	for element in data:
		array_data.append(element)

	return array_data
	
embedding_file = sys.argv[1]
path_output = sys.argv[2]

print("Read embedding data")

#read embedding data
arrays = np.load(embedding_file, allow_pickle=True)
dict_keys = list(arrays.keys())

dataset_embedding = []#dataset

for key in dict_keys:
	data = arrays[key].tolist()
	row_avg = data['avg']

	array_data = numpy_array_to_array(row_avg)
	dataset_embedding.append(array_data)

#get PCA
print("Get PCA from embedding, using 0.95 of variance")

min_max_scaler = preprocessing.MinMaxScaler()
matrixData_std = min_max_scaler.fit_transform(dataset_embedding)

pca = PCA(.95)
pca.fit(matrixData_std)
matrixData_pca = pca.fit_transform(matrixData_std)

header = []

for i in range(pca.n_components_):
    header.append("component_"+str(i+1))

#exportamos el ajuste de los datos transformados, son propiedades ortoganles, la gracia del PCA...
dataComponent = pd.DataFrame(matrixData_pca, columns=header)
dataComponent.to_csv(path_output+"embedding_PCA_representation.csv", index=False)

