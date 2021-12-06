from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

html = urlopen("https://cursosextensao.usp.br/course/view.php?id=2721")
bs = BeautifulSoup(html, 'html.parser')

#print(bs.prettify())
linhas = bs.find_all('a', {'class': 'aalink'})

curso = {}
for i in linhas:
    aula = i.text
    curso[aula] = i.attrs['href']

df = pd.DataFrame(curso, index=np.arange(4))
print(df)

"""for i in linhas:
    filhas = i.findChildren("span")
    print(filhas[0])
    #print(filhas[1])
    #print(filhas[2])"""