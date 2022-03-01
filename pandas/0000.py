import pandas as pd 
import numpy as np

a = pd.Series([1, 2, 3, 4])
print(a[0])
print(a[[0, 3]])
print(a[a < 2])
print(a * 2)
print(np.exp(a))
print(2 in a)
print(a.index)

b = pd.Series([6, 7, 8, 9])
c = a + b #somando duas séries
c.name = 'numeros'
c.index.name = 'nums'
print(c)
c.index = ['a', 'b', 'c', 'd']
print(c) 