import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import json

import requests

from urllib.request import Request, urlopen

url = Request('https://opensea.io/explore-collections', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(url)

bs = BeautifulSoup(webpage, 'html.parser')
#print(bs.prettify())

cats = bs.find_all('li', {'class': 'Menureact__StyledListMenuItem-sc-1j0z9gq-3 hlufrI'})
#print(cats)
for i in cats:
    a = i.findChildren('a')
    for b in a:
        print(b.text)