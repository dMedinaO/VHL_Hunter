import numpy as np
import json
import pymongo
from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
def mainSearch(field, query):
    #Utilizado para contar en el objeto principal
    categories = []
    for document in query:
        try: 
            if(document[field] not in categories):
                categories.append(document[field])
        except: 
            pass
    datos = []
    for i in categories:
        datos.append([i, 0])
    datos = np.array(datos, dtype = "O")
    query = coleccion.find({})
    for document in query:
        try: 
            index = np.where(datos == document[field])[0]
            datos[index,1] += 1
        except:
            pass
    dataframe = pd.DataFrame(datos, columns = [field, "frecuency"])
    return(dataframe)

def objectSearch(objName, field, query):
    #Utilizado para contar dentro de objetos
    categories = []
    for document in query:
        try: 
            for diseases in document[objName]:
                if(diseases[field] not in categories):
                    categories.append(diseases[field])
        except: 
            pass
    datos = []
    for i in categories:
        datos.append([i, 0])
    datos = np.array(datos, dtype = "O")
    query = coleccion.find({})
    for document in query:
        try: 
            for diseases in document[objName]:
                index = np.where(datos == diseases[field])[0]
                datos[index,1] += 1
        except:
            pass
    dataframe = pd.DataFrame(datos, columns = [field, "frecuency"])
    return(dataframe)
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutations
query = coleccion.find({})
mutationType = mainSearch("Mutation_type", query).sort_values(by = "frecuency", ascending = False)
mutationType.to_csv("../Resultados/mutation_type.csv", sep = "\t", index = False)
query = coleccion.find({})
vhlType = mainSearch("VHL_type", query).sort_values(by = "frecuency", ascending = False)
vhlType.to_csv("../Resultados/vhl_type.csv", sep = "\t", index = False)
query = coleccion.find({})
disease = objectSearch("Disease", "Effect", query).sort_values(by = "frecuency", ascending = False)
disease.to_csv("../Resultados/disease.csv", sep = "\t", index = False)
query = coleccion.find({})
site = objectSearch("Disease", "Site", query).sort_values(by = "frecuency", ascending = False)
site.to_csv("../Resultados/sites.csv", sep = "\t", index = False)
plt.rcParams['figure.figsize'] = (32,20)
plt.subplot(1,2,1)
plt.title("Mutation types")
plt.barh(mutationType.Mutation_type, mutationType.frecuency)
plt.subplot(1,2,2)
plt.title("VHL types")
plt.bar(vhlType.VHL_type, vhlType.frecuency)
plt.show()