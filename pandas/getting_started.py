# https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html
import pandas as pd
from pandas.core.indexes.base import Index

df = pd.DataFrame(
    {
        "Fruta doce": ["caqui", "amora", "jaca", "banana"],
        "Fruta azeda": ["carambola", "caju", "abacaxi", "limão"]
    }
)

#print(df[["Fruta doce"]].shape)
#print(df[df["Fruta azeda"] == "limão"])
#print(df.loc[df["Fruta doce"] == "maçã", "Fruta doce"])
#print(df.iloc[2:4, 1:3])

##Aprofundar!
df.iloc[0:2, 1] = "?"
#print(df)

df2 = pd.DataFrame(
    {
        "Exótica": ["lichia", "fruta pão", "pitaya", "romã"],
        "Tropical": ["kiwi", "maracujá", "mamão", "coco"]
    }
)

df3 = pd.concat([df, df2], axis=1)
#df3 = pd.concat([df, df2], axis=0)
#print(df3.sort_values("Exótica"))

df4 = pd.merge(df, df2, how="left", left_on="Fruta doce", right_on="Exótica")
print(df4)
##Criação de coluna
df["Fruta exótica"] = df2["Exótica"]
#print(df)

gude = pd.DataFrame({
    "azul": [10, 15, 20, 30],
    "verde": [5, 10, 25, 45]
})

gude["diferença"] = (gude["azul"] - gude["verde"])
#print(gude)
gude = gude.rename(
    columns={
        "verde": "verdes",
        "azul": "azuis"
    }
)
#print(gude)

tec = pd.DataFrame({
    "setor": ["infoSec", "infra", "ia", "dev"],
    "colaboradores": [2, 1, 2, 4],
    "idade": [26, 40, 23, 28],
    "especialização": ["pentest", "cloud", "regressão", "backend"],
    "gênero": ["feminino", "masculino", "feminino", "feminino"]
})

#print(tec[["gênero", "idade"]].groupby("gênero").mean())
#print(tec.groupby("gênero")["colaboradores"].mean())
#print(tec.groupby(["gênero", "setor"])["colaboradores"].mean())

#print(tec["colaboradores"].value_counts())

#print(tec.groupby("gênero")["gênero"].count())
#print(tec.sort_values(by="colaboradores"))

#transforma linhas de uma coluna em diferentes colunas
#print(tec.pivot(columns="setor"))
