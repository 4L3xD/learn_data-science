import pandas as pd

tuples = [
   ('WEGE3', 'mín'), ('WEGE3', 'max'),
   ('MGLU3', 'mín'), ('MGLU3', 'max'),
   ('AMER3', 'mín'), ('AMER3', 'máx')
]
#ITUB4

index = pd.MultiIndex.from_tuples(tuples)

#Primeiro campo do array representa a primeira coluna
#Segundo campo representa a segunda coluna
values = [[0.0, 0.1], [0.2, 0.3], [0.4, 0.5],
        [0.6, 0.7], [0.8, 0.9], [0.10, 1.0]]

df = pd.DataFrame(values, columns=['17/11/2021', '18/11/2021'], index=index)
#print(df)


#LOC
#Adiciona coluna
# : índice, coluna
df.loc[:, 'Nova Coluna'] = [1, 2, 3, 4, 5, 6]
#print(df)
#Acessa aos valores de um índice categórico
#print(df.loc['WEGE3'])
#print(df.loc['WEGE3', 'max'])
#formatação de tabela
#print(df.loc[[('WEGE3', 'max')]])

#Coluna
#print(df.iloc[0])
#Índice 
#print(df.iloc[[0]])


#Acessa 
#print(df)
