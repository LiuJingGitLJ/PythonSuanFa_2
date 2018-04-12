# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

print(np.arange(2, 10))
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(2, 9)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': range(4, 7)})

print('\n df1 print')
print(df1)

print('\n df2 print')
print(df2)

print(pd.merge(df1,df2))

print(pd.merge.__doc__)