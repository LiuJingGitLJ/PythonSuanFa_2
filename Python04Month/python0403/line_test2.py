#!/usr/bin/python
# coding:utf-8

import matplotlib.pyplot as plt
import pandas as  pd
from sklearn.linear_model import LinearRegression

# 从 csv 文件中读取数据，分别为：X列表和对应的Y列表

def get_data(filename):
    # 1.用pandas读取csv
    data = pd.read_csv(filename)

    #构造X列表和Y列表
    X_parameter = []
    Y_parameter = []

    for single_square_feet,single_price_value in zip(data['square_feet'],data['price']):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append(float(single_price_value))

    return X_parameter,Y_parameter

#线性回归分析 其中predict_square_feet 为要预测的平方英尺数 函数返回对应的房价
#note_lj 当前函数所反应的具体问题 函数表示的是什么 很重要

def liner_model_main(X_parameter,Y_parmeter,predict_square_feet):
    # 1、构造回归对象
    regr = LinearRegression()
    regr.fit(X_parameter,Y_parmeter)

    #2、获取预测值
    predict_outcom = regr.predict(predict_square_feet)

    #3、构造返回字典
    predictions = {}

    #3.1 截距值
    predictions['intercept'] = regr.intercept_
    # 回归系数 斜率值
    predictions['coefficient'] = regr.coef_
    # 预测值
    predictions['predict_value'] = predict_outcom

    return predictions


# 绘出图像

def show_linear_line(X_parmenter,Y_parameter):
    #1、构造回归对象
    regr = LinearRegression()
    regr.fit(X_parmenter,Y_parameter)

    # 绘出已知数据散点图
    plt.scatter(X_parmenter,Y_parameter,color = 'blue')

    # 绘出预测直线
    plt.plot(X_parmenter,regr.predict(X_parmenter),color = 'red', linewidth = 4)

    plt.title('Predict the house price')
    plt.xlabel('square feet')
    plt.show()

def show_linear_line1(X_parmenter,Y_parameter):
    # 构造回归对象
    regr = LinearRegression()
    regr.fit(X_parmenter,Y_parameter)

    # 绘出已知数据散点图
    plt.scatter(X_parmenter,Y_parameter,color = 'blue')

    #绘出预测直线
    plt.plot(X_parmenter,regr.predict(X_parmenter),color = 'red',linewidth = 4)

    plt.title('Predict the house price')
    plt.xlabel('square feet')
    plt.show()


def main():

    # 读取数据
    X,Y = get_data('./price_info.csv')

    # 2.获取 预测值，预测700平方英尺大小的房价
    predict_square_feet = 10000
    result = liner_model_main(X,Y,predict_square_feet)
    for key,value in result.items():
        print ('{0}:{1}'.format(key, value))

    # 绘图
    show_linear_line(X,Y)

if __name__ == '__main__' :
    main()

