# pip install openpyxl
import pandas as pd

df = pd.DataFrame(
    {
        "Tecnologia": ["Python"], #string
        "Versão": [3.10], #float
        "Linguagem de Programação": [True], #bool
        "Área": ["Ciência de dados"], #list/array
        "Subárea": ["Inteligência Artificial"],
    }
)

df.to_excel("data_science.xlsx", sheet_name="Ciência de Dados", index=False)
