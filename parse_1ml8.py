from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import os
import time
import pandas as pd
def get_edges_from_line(line_hbond_file):
    data_values = line_hbond_file.split("      ")
    node1_chain = data_values[0][data_values[0].find(")") + 1]
    node2_chain = data_values[1][data_values[1].find(")") + 1]
    node1 = data_values[0].split(" ")
    node1 = [value for value in node1 if str(value)!= "" and "(" not in str(value) and ")" not in str(value)]
    node2 = data_values[1].split(" ")
    node2 = [value for value in node2 if str(value)!= "" and "(" not in str(value) and ")" not in str(value)]
    pos = data_values[2].find("Val=")
    weight = float(data_values[2][pos: pos+12].replace("Val=", ""))
    aa_node1 = node1[1]
    aa_node2 = node2[-2]
    num_node1 = node1[2]
    num_node2 = node2[-1]
    if(int(num_node1) < int(num_node2)):
        node1 = aa_node1 + "-" + str(num_node1)
        node2  = aa_node2 + "-" + str(num_node2)
    else:
        node2 = aa_node1 + "-" + str(num_node1)
        node1 = aa_node2 +"-" + str(num_node2)
    if(node1_chain == "V" and node2_chain == "V"):
        return node1, node2, weight
    else:
        return False, False, False
driver = webdriver.Chrome(ChromeDriverManager(version="89.0.4389.23").install())
archivo = "1lm8.pdb"
driver.get("https://swift.cmbi.umcn.nl/servers/html/hnet.html")
form = driver.find_elements_by_tag_name("input")[2]
form.send_keys(os.getcwd() + "/" + archivo)
driver.find_elements_by_tag_name("input")[3].click()
response = "Processing .."
while(response == "Processing .."):
    response = driver.find_element_by_tag_name("body").text
    time.sleep(1)
driver.close()
output = os.getcwd() + "/" + archivo.replace(".pdb", ".txt")
f = open(output, "w")
f.write(response)
f.close()

df = pd.DataFrame(columns = ["node1", "node2", "weight"])
file_open = open(output, "r")
line = file_open.readline()
while line:
    if(str(line[0:2]) == "  "):
        line = line.replace("\n", "")
        node1, node2, weight = get_edges_from_line(line)
        if(node1 != False):
            if "HOH" not in node1 and "HOH" not in node2:
                q = "node1 == '" + node1 + "' and node2 == '" + node2 + "'"
                query = df.query(q)
                if(len(query) == 0):
                    df  = df.append({"node1": node1, "node2": node2, "weight": weight}, ignore_index = True)
                else:
                    df.loc[int(query.index[0]), "weight"] = df.loc[int(query.index[0]), "weight"] + weight
    line = file_open.readline() 
file_open.close()
df.to_csv("1lm8.csv", sep = ";", index = False)