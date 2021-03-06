import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans #导入K均值聚类算法
# datafile= r'../data/air_data.csv' #航空原始数据,第一行为属性标签
# resultfile = r'../tmp/explore111.xls' #数据探索结果表
# data = pd.read_csv(datafile, encoding = 'utf-8') #读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）
# explore = data.describe(percentiles = [], include = 'all').T #包括对数据的基本描述，percentiles参数是指定计算多少的分位数表（如1/4分位数、中位数等）；T是转置，转置后更方便查阅
# print(explore)
# explore['null'] = len(data)-explore['count'] #describe()函数自动计算非空值数，需要手动计算空值数
# explore = explore[['null', 'max', 'min']]
# explore.columns = [u'空值数', u'最大值', u'最小值'] #表头重命名
# print('-----------------------------------------------------------------以下是处理后数据')
# print(explore)
# explore.to_excel(resultfile) #导出结果

import pandas as pd
datafile= '../data/air_data.csv' #航空原始数据,第一行为属性标签
cleanedfile = '../tmp/data_cleaned2.csv'  #数据清洗后保存的文件
data = pd.read_csv(datafile,encoding='utf-8') #读取原始数据，指定UTF-8编码（需要用文本编辑器将数据装换为UTF-8编码）
data = data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()] #票价非空值才保留
#只保留票价非零的，或者平均折扣率与总飞行公里数同时为0的记录。
index1 = data['SUM_YR_1'] != 0
index2 = data['SUM_YR_2'] != 0
index3 = (data['SEG_KM_SUM'] == 0) & (data['avg_discount'] == 0) #该规则是“与”,书上给的代码无法正常运行，修改'*'为'&'
data = data[index1 | index2 | index3] #该规则是“或”
print(data)
# data.to_csv(cleanedfile) #导出结果

def reduction_data(data):
    data = data[['LOAD_TIME', 'FFP_DATE', 'LAST_TO_END', 'FLIGHT_COUNT', 'SEG_KM_SUM', 'avg_discount']]
    # data['L']=pd.datetime(data['LOAD_TIME'])-pd.datetime(data['FFP_DATE'])
    # data['L']=int(((parse(data['LOAD_TIME'])-parse(data['FFP_ADTE'])).days)/30)
    d_ffp = pd.to_datetime(data['FFP_DATE'])
    d_load = pd.to_datetime(data['LOAD_TIME'])
    res = d_load - d_ffp
    data2=data.copy()
    data2['L'] = res.map(lambda x: x / np.timedelta64(30 * 24 * 60, 'm'))
    data2['R'] = data['LAST_TO_END']
    data2['F'] = data['FLIGHT_COUNT']
    data2['M'] = data['SEG_KM_SUM']
    data2['C'] = data['avg_discount']
    data3 = data2[['L', 'R', 'F', 'M', 'C']]
    return data3
data3=reduction_data(data)
print(data3)

def zscore_data(data):
    data = (data - data.mean(axis=0)) / data.std(axis=0)
    data.columns = ['Z' + i for i in data.columns]
    return data
data4 = zscore_data(data3)

inputfile = r'../data/zscoredata.xls' #待聚类的数据文件
k = 5                       #需要进行的聚类类别数
#读取数据并进行聚类分析
data = pd.read_excel(inputfile) #读取数据
#调用k-means算法，进行聚类分析
kmodel = KMeans(n_clusters = k, n_jobs = 4) #n_jobs是并行数，一般等于CPU数较好
kmodel.fit(data) #训练模型
r1 = pd.Series(kmodel.labels_).value_counts()
r2 = pd.DataFrame(kmodel.cluster_centers_)
r = pd.concat([r2, r1], axis=1)
r.columns = list(data.columns) + ['类别数目']
# print(r)
# r.to_excel(classoutfile,index=False)
r = pd.concat([data, pd.Series(kmodel.labels_, index=data.index)], axis=1)
r.columns = list(data.columns) + ['聚类类别']
print(kmodel.cluster_centers_)
print(kmodel.labels_)


def density_plot(data):
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus']=False
    p=data.plot(kind='kde',linewidth=2,subplots=True,sharex=False)
    [p[i].set_ylabel('密度') for i in range(5)]
    [p[i].set_title('客户群%d' %i) for i in range(5)]
    plt.legend()
    plt.show()
    return plt
density_plot(data4)

# clu = kmodel.cluster_centers_
# x = [1,2,3,4,5]
# colors = ['red','green','yellow','blue','black']
# for i in range(5):
#    plt.plot(x,clu[i],label='clustre '+str(i),linewidth=6-i,color=colors[i],marker='o')
# plt.xlabel('L  R  F  M  C')
# plt.ylabel('values')
# plt.show()
