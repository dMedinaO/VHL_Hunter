#Script para importar la data presente en la carpeta Datasets a la base de datos Mongodb. 
import pandas as pd
import pymongo
from pymongo import MongoClient
import numpy as np
import json
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from Bio import SeqIO
import pandas as pd
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Seq import MutableSeq

def getPaperTitle(driver, id):
    #Webscrapping para obtener el nombre de los artículos. 
    url = "https://pubmed.ncbi.nlm.nih.gov/" + id
    driver.get(url) 
    get_title = driver.title 
    return get_title.replace(" - PubMed", "")
#Funciones para obtener la proteína a partir de la mutación señalada. 
def missense(mutacion):
    temp = mutacion.replace("p.","")
    wt = temp[0]
    mut = temp[-1]
    pos = int(temp.replace(wt,"").replace(mut,""))
    seq = (pvhl[:pos-1] + mut + pvhl[pos:])
    return seq
def nonsense(mutacion):
    temp = mutacion.replace("p.","")
    wt = temp[0]
    pos = int(temp.replace(wt,"").replace("X",""))
    seq = pvhl[:pos-1]
    return seq
def insertion_nt(mutacion):
    temp = mutacion.replace("c.", "").split("ins")
    pos = int(temp[0])
    seq = cds_vhl[:pos-1] + temp[1] + cds_vhl[pos-1:]
    while(len(seq) %3 != 0):
        seq += "N"
    protein = str(Seq(str(seq)).translate(to_stop=True))
    return seq, protein
def insertion_aa(mutacion):
    temp = mutacion.replace("p.", "").split("ins")
    pos = int(temp[0])
    seq = pvhl[:pos-1] + temp[1] + pvhl[pos-1:]
    return seq
def range_deletion_nt(mutacion):
    temp = mutacion.replace("c.", "").replace("del", "").split("_")
    ini = int(temp[0])
    fin = int(temp[1])
    seq = cds_vhl[:ini-1]+cds_vhl[fin:]
    while(len(seq) %3 != 0):
        seq += "N"
    protein = str(Seq(str(seq)).translate(to_stop=True))
    return seq, protein
def range_deletion_aa(mutacion):
    temp = mutacion.replace("p.", "").replace("del","").split("_")
    pos = int(temp[0])
    pos2 = int(temp[1])
    seq = pvhl[:pos-1] + pvhl[pos2-1:]
    return seq
def single_deletion_nt(mutacion):
    temp = mutacion.replace("c.", "").replace("del", "")
    pos = int(temp)
    seq = cds_vhl[:pos-1] + cds_vhl[pos:]
    while(len(seq) %3 != 0):
        seq += "N"
    protein = str(Seq(str(seq)).translate(to_stop=True))
    return seq, protein
def single_deletion_aa(mutacion):
    temp = mutacion.replace("p.", "").replace("del","")
    pos = int(temp[0])
    seq = pvhl[:pos-1] + pvhl[pos-1:]
    return seq
def multiple_missense(seqInput, mutacion):    
    mutacion = mutacion.replace("p.","")
    wt = mutacion[0]
    mut = mutacion[-1]
    pos = int(mutacion.replace(wt,"").replace(mut,""))
    seq = str((seqInput[:pos-1] + mut + seqInput[pos:]))
    return seq
cds_vhl = str(list(SeqIO.parse("../Secuencias/VHL_cds.fna", "fasta"))[0].seq)
pvhl = str(list(SeqIO.parse("../Secuencias/pvhl.fna", "fasta"))[0].seq)
driver = webdriver.Chrome() 
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
#Se comienza con las mutaciones simples, alojadas en Single_Mutations.csv. 
muts = np.array(pd.read_csv("../Datasets/ProcesedData/Single_Mutations.csv", sep = "\t"))
arreglo = []
mutaciones = []
types = []
for i in range(muts.shape[0]):
    #Este ciclo es para corroborar la integridad de la información. 
    mutacion = ""
    mutacion += '{"Mutation": "' + str(muts[i,0]) + '", "Mutation_type": "' + str(muts[i,1]) + '", '
    if(str(muts[i,2]) != "nan"):
        mutacion += '"VHL_type": "' + str(muts[i,2]) + '", '
    if(str(muts[i,3]) != "nan"):
        mutacion += '"Disease": ' + str(muts[i,3]) + ', '
    mutacion += '"Pubmed_ID": ' + str(muts[i, 4]) + '}'
    if(muts[i,0] not in mutaciones):
        mutaciones.append(muts[i,0])
        types.append(muts[i,1])
    diccionario = json.loads(mutacion)
    arreglo.append(diccionario)
bd = []
for i in range(len(mutaciones)):
    #Se genera un arreglo de diccionarios con la información alojada en Single_Mutations.csv
    documento = '{"Mutation": "' + mutaciones[i] + '", '
    if(" (nt)" in types[i]):
        documento = documento + '"Molecule": "DNA", '
    else:
        documento = documento + '"Molecule": "Protein", '
    documento += '"Mutation_type": "' + types[i].replace(" (nt)", "").replace(" (aa)", "").replace("_", " ") + '", '
    documento += '"Case": ['
    for j in arreglo:
        if(j["Mutation"] == mutaciones[i]):
            documento += "{"
            try: 
                documento += '"VHL_type": "' + j["VHL_type"] + '"'
            except:
                documento = documento
            try:
                documento += '"Disease": ' + str(j["Disease"])
            except:
                documento = documento
            try:
                referencias = list(j["Pubmed_ID"])
                listreferencias = []
                referencia = {}
                #Para las referencias interesa guardar el id (final del link) y el título del paper. 
                for r in referencias:
                    referencia["Id"] = r
                    referencia["Title"] = getPaperTitle(driver, r).replace('"', '')
                    listreferencias.append(referencia)
                stringReferencias = str(listreferencias)
                documento += '"Reference": ' + stringReferencias
            except:
                documento = documento
            documento += "}"
    documento += ']}'
    documento = documento.replace('{}', "").replace("}{", "}, {").replace("'", '"').replace('""', '", "').replace(']"','], "')
    diccionario = json.loads(documento)
    #Se insertan las secuencias de proteína y DNA según corresponda. 
    if(diccionario["Molecule"] == "Protein" and diccionario["Mutation_type"] == "Missense"):
        proteina_mutada = missense(diccionario["Mutation"])
        diccionario["Protein_sequence"] = proteina_mutada
    if(diccionario["Molecule"] == "Protein" and diccionario["Mutation_type"] == "Insertion"):
        proteina_mutada = insertion_aa(diccionario["Mutation"])
        diccionario["Protein_sequence"] = proteina_mutada
    if(diccionario["Molecule"] == "Protein" and diccionario["Mutation_type"] == "Range Deletion"):
        proteina_mutada = range_deletion_aa(diccionario["Mutation"])
        diccionario["Protein_sequence"] = proteina_mutada
    if(diccionario["Molecule"] == "Protein" and diccionario["Mutation_type"] == "Silent"):
        proteina_mutada = pvhl
        diccionario["Protein_sequence"] = proteina_mutada
    if(diccionario["Molecule"] == "Protein" and diccionario["Mutation_type"] == "Single Deletion"):
        proteina_mutada = single_deletion_aa(diccionario["Mutation"])
        diccionario["Protein_sequence"] = proteina_mutada
    if(diccionario["Molecule"] == "Protein" and diccionario["Mutation_type"] == "Nonsense"):
        proteina_mutada = nonsense(diccionario["Mutation"])
        diccionario["Protein_sequence"] = proteina_mutada
    if(diccionario["Molecule"] == "DNA" and diccionario["Mutation_type"] == "Single Deletion"):
        dna_mutado, proteina_mutada = single_deletion_nt(diccionario["Mutation"])
        diccionario["Protein_sequence"] = proteina_mutada
        diccionario["DNA_sequence"] = dna_mutado
    if(diccionario["Molecule"] == "DNA" and diccionario["Mutation_type"] == "Range Deletion"):
        dna_mutado, proteina_mutada = range_deletion_nt(diccionario["Mutation"])
        diccionario["Protein_sequence"] = proteina_mutada
        diccionario["DNA_sequence"] = dna_mutado
    if(diccionario["Molecule"] == "DNA" and diccionario["Mutation_type"] == "Insertion"):
        dna_mutado, proteina_mutada = insertion_nt(diccionario["Mutation"])
        diccionario["Protein_sequence"] = proteina_mutada
        diccionario["DNA_sequence"] = dna_mutado
    print(diccionario)
    bd.append(diccionario)
#Se insertan las mutaciones simples en la base de datos VHL_Hunter
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
coleccion.delete_many({})
coleccion.insert_many(bd, ordered = True)
print("Mutaciones simples importadas")
#Se trabaja con el archivo ClinicalRisk.csv, el cual tiene la información de riesgo clínico para RCC. 
ClinicalRisk = pd.read_csv("../Datasets/ProcesedData/ClinicalRisk.csv", sep = "\t")[["MUTATION", "RISK"]]
con = MongoClient('localhost',27017)
db = con.VHL_Hunter
coleccion = db.Mutation
listRisks = []
for ii, i in enumerate(ClinicalRisk["MUTATION"]):
    res = list(coleccion.find({"Mutation": i}))
    if(len(res) == 1):#Si existe la mutación, se actualiza su campo Risk. 
        coleccion.update_one({"Mutation": i}, {"$set": {"Risk": ClinicalRisk["RISK"][ii]}})
    else:#Si no existe la mutación en la bd, se crea una nueva mutacion y se llena con el campo Risk. 
        dato = '{"Mutation": "' + i + '", "Molecule": "Protein", "Mutation_type": "Missense", "Risk": "'+ ClinicalRisk["RISK"][ii] + '"}'
        diccionario = json.loads(dato)
        proteina_mutada = missense(diccionario["Mutation"])
        diccionario["Protein_sequence"] = proteina_mutada#Por suerte, todas las mutaciones de la bd de riesgo clínico son missense. 
        listRisks.append(diccionario)
    print(diccionario)
coleccion.insert_many(listRisks, ordered = True)
print("Mutaciones riesgo clínico importadas")
#Se trabaja con mutaciones multiple missense. 
complejas = np.array(pd.read_csv("../Datasets/ProcesedData/Multiple_Missense.csv", sep = "\t"))
arreglo = []
mutaciones = []
for i in range(complejas.shape[0]):#Se comprueba la integridad de la información. 
    mutacion = ""
    mutacion += '{"Mutations": ' + str(complejas[i,0]) + ', "Mutation_types": ' + str(complejas[i,1]) + ', '
    if(str(complejas[i,2]) != "nan"):
        mutacion += '"VHL_type": "' + str(complejas[i,2]) + '", '
    if(str(complejas[i,3]) != "nan"):
        mutacion += '"Disease": ' + str(complejas[i,3]) + ', '
    mutacion += '"Pubmed_ID": ' + str(complejas[i, 4]) + '}'
    diccionario = json.loads(mutacion)
    if(complejas[i,0] not in mutaciones):
        mutaciones.append(complejas[i,0])
    arreglo.append(diccionario)
bd = []
for i in range(len(mutaciones)):#Se generan los diccionarios con las mutaciones
    documento = '{"Mutations": ' + mutaciones[i] + ', '
    documento += '"Mutation_type": "Multiple Missense"'
    documento += '"Case": ['
    for j in arreglo:
        if(str(j["Mutations"]).replace("'", '"') == mutaciones[i]):
            documento += "{"
            try: 
                documento += '"VHL_type": "' + j["VHL_type"] + '"'
            except:
                documento = documento
            try:
                documento += '"Disease": ' + str(j["Disease"])
            except:
                documento = documento
            try:
                referencias = list(j["Pubmed_ID"])
                listreferencias = []
                referencia = {}
                for r in referencias:
                    referencia["id"] = r
                    referencia["title"] = getPaperTitle(driver, r)
                    listreferencias.append(referencia)
                stringReferencias = str(listreferencias)
                documento += '"Reference": ' + stringReferencias
            except:
                documento = documento
            documento += "}"
    documento += ']}'
    documento = documento.replace('{}', "").replace("}{", "}, {").replace("'", '"').replace('""', '", "').replace(']"','], "')
    diccionario = json.loads(documento)
    mutated = pvhl
    for m in diccionario["Mutations"]:
        #Se genera la proteína mutada. 
        mutated = multiple_missense(mutated, m)
    diccionario["Protein_sequence"] = mutated
    print(diccionario)
    bd.append(diccionario)
coleccion.insert_many(bd, ordered = True)
print("Mutaciones dobles importadas")