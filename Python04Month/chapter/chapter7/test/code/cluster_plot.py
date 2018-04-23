#-*- coding: utf-8 -*-
#画出特征雷达图，代码接KMeans_cluster.py

import numpy as np
import matplotlib.pyplot as plt
<<<<<<< HEAD

labels = data.columns #标签
k = 5 #数据个数
=======
import pandas as pd
from sklearn.cluster import KMeans #导入K均值聚类算法
datafile = '../../demo/tmp/zscoreddata.xls' #航空原始数据,第一行为属性标签

data = pd.read_excel(datafile, encoding = 'utf-8') #读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）

labels = data.columns #标签
k = 5 #数据个数

kmodel = KMeans(n_clusters = k, n_jobs = 4) #n_jobs是并行数，一般等于CPU数较好
kmodel.fit(data) #训练模型

>>>>>>> 9e3625d79b9f64576d417be14b9b3f60797aacdd
plot_data = kmodel.cluster_centers_
color = ['b', 'g', 'r', 'c', 'y'] #指定颜色

angles = np.linspace(0, 2*np.pi, k, endpoint=False)
plot_data = np.concatenate((plot_data, plot_data[:,[0]]), axis=1) # 闭合
angles = np.concatenate((angles, [angles[0]])) # 闭合

fig = plt.figure()
ax = fig.add_subplot(111, polar=True) #polar参数！！
for i in range(len(plot_data)):
  ax.plot(angles, plot_data[i], 'o-', color = color[i], label = u'客户群'+str(i), linewidth=2)# 画线

ax.set_rgrids(np.arange(0.01, 3.5, 0.5), np.arange(-1, 2.5, 0.5), fontproperties="SimHei")
ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
plt.legend(loc = 4)
plt.show()