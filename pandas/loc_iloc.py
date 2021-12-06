import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['São Paulo', 'Rio de Janeiro', 'Mina Gerais', 'Bahia'],
                    columns=['one', 'two', 'three', 'four'])
#print(data['three'])
#print(data[['two', 'one']])
#print(data[:2])
#print(data.loc['São Paulo', ['one', 'three']])
#print(data.iloc[2, [3, 0, 1]])
#print(data.iloc[2])
#print(data.iloc[[1, 2], [3, 0, 1]])
#print(data.loc[:'São Paulo', 'one'])
print(data.iloc[:, :3][data.three > 9])