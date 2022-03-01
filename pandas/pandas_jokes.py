import pandas as pd
import numpy as np

nome = input('Nome: ')
num_doc = input('Nº documento: ')
nascimento = input('Data de nascimento: ')
nacionalidade = input('Nacionalidade: ')
pais = input('País de residência: ')

cadastro = pd.Series(
    [nome, num_doc, nascimento, nacionalidade, pais], index=['nome', 'num_doc', 'nascimento', 'nacionalidade', 'pais']
    )
print(cadastro)