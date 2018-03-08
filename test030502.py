#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 不带参数的函数
def printLine():
    # 输出一条横线
    print("--------------------------------------------");
    # 没有返回值
    # return;


printLine();


# 带参数的函数
def printInfo(name, age):
    print("name is: ", name, "; age is: ", age);
    # 没有返回值
    return;


# 正确调用
printInfo("KEN", 18);
printInfo(age=18, name="KEN");

# 错误调用
#printInfo("KEN");


# 默认参数的函数
def printInfo(name, age=20):
    print("name is: ", name, "; age is: ", age);
    # 没有返回值
    return;


# 正确调用
printInfo("KEN");


# 可变长参数的函数--数组形式
def printInfo(name, *args):
    # 打印任何传入的字符串
    print("name is: ", name);
    printLine();
    for arg in args:
        print(arg);
    # 没有返回值
    return;


# 正确调用
printInfo("KEN", 20, "男", 178, "70KG", 'abc');


# 可变长参数的函数--kv方式
def printInfo(name, **kvArgs):
    # 打印任何传入的字符串
    print("name is: ", name);
    printLine();
    for k in kvArgs:
        print(k, "is: ", kvArgs[k]);
    # 没有返回值
    return;


# 正确调用
printInfo("KEN", age=20, sex="男", height="178", weight="70KG");

# 错误调用
#printInfo("KEN", 20, "男");


# 有返回值的函数
def maxValue(*args):
    rValue = args[0];
    for var in args:
        if rValue < var:
            rValue = var;
    return rValue;


r = maxValue(4, 5, 2, 6, 7, 1);
print(r);

sumValue = lambda arg1, arg2: arg1 + arg2;
r = sumValue(1, 5)
print(r)

import numpy;
from pandas import DataFrame;

df = DataFrame({
    'key1': ['a', 'a', 'b', 'b', 'a'],
    'key2': ['one', 'two', 'one', 'two', 'one'],
    'data1': numpy.random.randn(5),
    'data2': numpy.random.randn(5)
});

df.groupby('key1')['data1', 'data2'].agg(lambda arr: arr.max() - arr.min())
