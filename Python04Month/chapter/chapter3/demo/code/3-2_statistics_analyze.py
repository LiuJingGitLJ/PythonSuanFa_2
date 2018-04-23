#-*- coding: utf-8 -*-
#餐饮销量数据统计量分析
from __future__ import print_function
import pandas as pd

catering_sale = '../data/catering_sale.xls' #餐饮数据
print(catering_sale)
data = pd.read_excel(catering_sale, index_col = u'日期') #读取数据，指定“日期”列为索引列
data = data[(data[u'销量1'] > 400)&(data[u'销量1'] < 5000)] #过滤异常数据
statistics = data.describe() #保存基本统计量

statistics.loc['range'] = statistics.loc['max']-statistics.loc['min'] #极差
statistics.loc['var'] = statistics.loc['std']/statistics.loc['mean'] #变异系数
statistics.loc['dis'] = statistics.loc['75%']-statistics.loc['25%'] #四分位数间距

print(statistics)

cateing_sale2 = '../data/catering_sale.xls' #餐饮数据
print(cateing_sale2)

data1 = pd.read_excel(cateing_sale2, index_col= u'日期') #读取数据， 指定日期列 为索引列
data1 = data[(data[u'销量1'] > 400)&(data[u'销量1'] < 5000)]
statistics1 = data.describe() #保存基本统计

statistics.loc['range'] = statistics.loc['max']-statistics.loc['min'] #极差
