import numpy as np; import pandas as pd

#duplica os valores na ordem do índice
#values = pd.Series(['apple', 'orange', 'apple', 'apple'] * 2)
#print(values)

#print(pd.value_counts(values))
values = pd.Series([0, 1, 0, 0] *2)
#dim = pd.unique(values)
#print(dim)
#print(dim.take(values))
dim = pd.Series(['apple', 'orange'])
print(dim.take(values))