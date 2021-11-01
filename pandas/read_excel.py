import pandas as pd

# `pd.read_excel(nomeTabela.xlsx)` para .xlsx
# Ex: `tabela = pd.read_excel("animes.xlsx", sheet_name="Planilha1")`
tabela = pd.read_csv("coronavirus.csv")
print(tabela)
