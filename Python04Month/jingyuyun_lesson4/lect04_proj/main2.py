# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot') #设置图片显示的主题样式

#解决matplotlib 显示中文问题
plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体

plt.rcParams['axes.unicode_minus'] = False #解决保存图像是负号 '-' 显示为方块的问题

dataset_path = './dataset/Mountains.csv'

def preview_data(data):
    '''
    数据预览
    :param data:
    :return:
    '''

    print(data.head())
    print(data.info())

def proc_success(val):
    '''
    处理 'Ascents bef. 2004'
    :param val:
    :return:
    '''
    if '>' in str(val):
        return 200
    elif 'Many' in str(val):
        return 160
    else:
        return val

def run_main():
    '''
    主函数
    :return:
    '''
    data = pd.read_csv(dataset_path)
    preview_data(data)

    #数据重构
    #重命名列名
    data.rename(columns={'Height(m)':'Height', 'Ascents bef .2004':'Success',
                         'Failed attempts bef. 2004': 'Failed'}, inplace=True)

    #数据清洗
    data['Failed'] = data['Failed'].fillna(0).astype(int)
    data['Success'] = data['Success'].apply(proc_success)
    data['Success'] = data['Success'].fillna(0).astype(int)
    data = data[data['First ascent'] != 'unclimbed']
    data['First ascent'] = data['First ascent'].astype(int)

    #可视化数据
    plt.hist(data['First ascent'].astype(int), bins=20)
    plt.ylabel('高峰数量')
    plt.xlabel('年份')

