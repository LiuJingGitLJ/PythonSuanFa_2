
import numpy as np

a1=[[1,2],[3,2],[5,2]];#列表
print('11111----------')
print(a1)
a2=np.array(a1);#将列表转换成二维数组
print('222----------')
print(a2)

a3=np.array(a1);#将列表转化成矩阵
print('3333----------')
print(a3)

a4=np.array(a3);#将矩阵转换成数组
print('44444----------')
print(a4)
a5=a3.tolist();#将矩阵转换成列表

a6=a2.tolist();#将数组转换成列表

