# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

# 通过ndarray构建DataFrame
array = np.random.randn(5, 4)
print(array)

df_obj = pd.DataFrame(array)
print(df_obj.head())
print("-----------------")
# 通过dict构建DataFrame

dict_data = {'A': 1.,
             'B': pd.Timestamp('20161217'),
             'C': pd.Series(1,index=list(range(4)),dtype='float32'),
             'D': np.array([3] * 4,dtype='int32'),
             'E': pd.Categorical(["Python","Java","C++","C#"]),
             'F': 'ChinaHadoop'}
df_obj2 = pd.DataFrame(dict_data)
print(df_obj2.head())
#通过列表索引获取列表数据(Series 类型)
print("--------AAAAAAA---------")
print(df_obj2['A'])
print("--------TTTTTTT---------")
print(type(df_obj2['A']))

# 增加列数据，类似 字典里增加key-value
print('---------增加列------')
df_obj2['G'] = df_obj2['D'] + 4

#删除列
print('shanchu lie')
del(df_obj2['G'])
print(df_obj2.head())


# 索引对象Index
# Series和DataFrame中的索引都是Index对象
# 不可变 保证了数据的安全性，常见的Index种类，Index，Int64Index，MultiIndex '层级'索引 DatetimeIndex


