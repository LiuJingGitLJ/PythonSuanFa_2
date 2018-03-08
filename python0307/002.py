# -*- coding: utf-8 -*-

import pandas as pd
#Series 索引
ser_obj = pd.Series(range(5), index = ['a', 'b', 'c', 'd', 'e'])
print(ser_obj.head())

# 行索引
print(ser_obj['a'])
print(ser_obj[0])

#切片索引
print(ser_obj[1:3])
print(ser_obj['b':'d'])

#不连续索引
print('不连续索引---')
print(ser_obj[[0, 2, 4]])
print(ser_obj[['a', 'e']])

#布尔索引
print('布尔索引----')
ser_bool = ser_obj > 2
print(ser_bool)
print(ser_obj[ser_bool])
print(ser_obj[ser_obj > 2])

#三种索引方式 loc
#标签标引 loc
# Series
print('标签标引 loc----')
print(ser_obj['b':'d'])
print(ser_obj.loc['b':'d'])

#Pandas的数据操作
#索引操作总结 Pandas的索引可以归纳为3种， .loc 标签索引， .iloc 位置索引 .ix标签与位置混合索引 先按标签索引尝试操作，然后再按位置索引尝试操作

#注意：DataFrame索引时可以将其看作Ndarray操作 标签的切片索引是包含末尾位置的


