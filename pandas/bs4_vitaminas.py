from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import json

html = urlopen("https://www.tuasaude.com/alimentos-ricos-em-vitaminas/")
bs = BeautifulSoup(html, 'html.parser')

#print(bs.prettify())
linhas = bs.find_all('div', {'class': 'table-responsive'})

fontes_vitaminas = {}
for vit in linhas:
    for i in range(0, 42, 3):
        vitamina = vit.findChildren("td")[i].text
        fontes_vitaminas[vitamina] = vit.findChildren("td")[i + 1].text

with open('vitaminas.json', 'w', encoding ='utf8') as json_file:
    json.dump(fontes_vitaminas, json_file, ensure_ascii = False, indent=2)
