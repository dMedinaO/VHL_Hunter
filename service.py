from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import os
import subprocess
driver = webdriver.Chrome(ChromeDriverManager(version="89.0.4389.23").install())
root = "PDB"
main = os.listdir(path = root)
for m in main:
    pdbs = os.listdir(path = root + "/" + m)
    for p in pdbs:
        archivo = p
        driver.get("https://swift.cmbi.umcn.nl/servers/html/hnet.html")
        form = driver.find_elements_by_tag_name("input")[2]
        form.send_keys(os.getcwd() + "/" + root + "/" + m + "/" + archivo)
        driver.find_elements_by_tag_name("input")[3].click()
        response = "Processing .."
        while(response == "Processing .."):
            response = driver.find_element_by_tag_name("body").text
            time.sleep(1)
        output = os.getcwd() + "/HydrogenBonds/" + m + "/" + archivo.replace(".pdb", ".txt")
        f = open(output, "w")
        f.write(response)
        f.close()