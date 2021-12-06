# pip install pandas
import pandas as pd
from pandas import DataFrame, Series
from pandas.core.indexes.base import Index
import numpy as np

#um dataframe é um método/função do pandas que escreve um dicionário 
df = DataFrame(
    {
        "Tecnologia": ["Python"], #string
        "Versão": [3.10], #float
        "Linguagem de Programação": [True], #bool
        "Área": ["Ciência de dados"], #list/array
        "Subárea": ["Inteligência Artificial"],
    }
)
#print(df)
#print(df.head())

dict = {
            "state": ["SP", "RJ", "MG", "BA"],
            "population": [46.6, 17.4, 21.4, 14.9]
        }

df = DataFrame(dict)
#print(df.head())

df = DataFrame(dict, columns=["state", "population"])
#print(df.head())

df = DataFrame(dict, columns=["state", "population"], index=["Maior população", "Segunda maior população", "Terceira maior população", "Quarta maior população"])
#print(df.head())
#print(df.columns)
#print("population" in df.columns)

largest_population = df.loc["Maior população"]
#print(largest_population)

df["new column"] = "New value"
#print(df)

df["new column"] = np.arange(4.) #** 2
#print(df)
labels = Index(np.arange(3))
#print(labels)

series = Series(["a", "b", "c"], index=labels)
#print(series)

index = Index([-5, -4, -3, -2, -1])
#print(index)

#a = 1
#print(a is 1)
#print(series.index is labels) #True

column = Series(["Selva de Pedra", "Samba"], index=["Maior população", "Terceira maior população"])
df["new column"] = column
#print(df)

df["other new column"] = df.state == "SP"
#print(df) 

#print(df.columns)
del df["other new column"]
#print(df)
#print(df.columns)

"""transpose = df.T"""
#print(transpose)

dict = {
            "States": df["state"][:-1],
            "Population": df["population"]#[:2]
        }
#print(dict)
#print( DataFrame(dict) )
df.index.name = "rank"; df.columns.name = "sensu"
#print(df)

#print(df.values)

df = Series(range(3), index=["a", "b", "c"])
#print(df)

#print(df.index)
#print(df[1:])

obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
#print(obj)
#print(obj.reindex(['a', 'b', 'c', 'd', 'e']))

obj = Series(['blue', 'purple', 'yellow'], index=[0, 3, 4])
#print(obj) 
update_obj = obj.reindex(range(6), method='ffill')
#print(update_obj)

frame = DataFrame(
                    np.arange(9).reshape(3, 3),
                    index=['c', 'a', 'b'],
                    columns=['SP', 'RJ', 'MG']
                )
#print(frame)

reindex_indice = frame.reindex(['a', 'b', 'c'])
#print(reindex_indice)

states = ["São Paulo", "Rio de Janeiro", "Minas Gerais"]
reindex_columns = frame.reindex(columns=states)
#print(reindex_columns)


reindex_loc = frame.loc[['a', 'b', 'c']]
#print(reindex_loc)

frame = frame.drop('c')
#print(frame)

df = DataFrame(np.arange(12).reshape(3, 4), columns=["teste", "teste1", "teste2", "teste4"], index=['a', 'b', 'c'])
#print(df[1:2])
#print(df[["teste", "teste2"]]) #acessa a coluna
#print(df["teste"][1]) #acessa a linha

#print(df[1:2])
#print(df[['teste1', 'teste']])
#print(df[df % 2 != 0])
#print(df['b':'c'])
#print(df[df['teste1'] > 5])

#df[df % 2 != 1] = 0
#print(df)
