import pandas as pd

#um dataframe é um método/função do pandas que escreve um dicionário 
df = pd.DataFrame(
    {
        "Tecnologia": ["Python"], #string
        "Versão": [3.10], #float
        "Linguagem de Programação": [True], #bool
        "Área": ["Ciência de dados"], #list/array
        "Subárea": ["Inteligência Artificial"],
    }
)

print(df)