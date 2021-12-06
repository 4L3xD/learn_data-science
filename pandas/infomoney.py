from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

html = urlopen("https://api.infomoney.com.br/ativos/ticker?type=json&_=178")
bs = BeautifulSoup(html, 'html.parser')
print(type(bs))

for i in bs:
    print(i)
#print(bs.prettify())

