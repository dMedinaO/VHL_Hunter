import pandas as pd
from pymongo import MongoClient
import numpy as np
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation

listado = list(coleccion.find({"Mutation_type": "Missense"},{"Mutation": 1, "_id": 0}))
for i in listado:
    pos = int(i["Mutation"][3:-1])
    if(pos <= 59):
        coleccion.find_one_and_update({"Mutation": i["Mutation"]},{"$set": {"Surface": "D"}})
    else:
        if(pos <= 103):
            coleccion.find_one_and_update({"Mutation": i["Mutation"]}, {"$set": {"Surface": "B"}})
        else:
            if(pos <= 153):
                coleccion.find_one_and_update({"Mutation": i["Mutation"]}, {"$set": {"Surface": "C"}})
            else:
                if(pos <= 189):
                    coleccion.find_one_and_update({"Mutation": i["Mutation"]}, {"$set": {"Surface": "A"}})