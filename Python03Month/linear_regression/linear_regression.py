# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 16:38:23 2017

@author: John
"""

from numpy import *
import matplotlib.pyplot as plt

'''
线性回归是对连续型的数据进行预测。这里讨论的是线性回归的例子，对于非线性回归先不做讨论。这部分内容我们用的是正规方程的解法，
理论内容在之前已经解释过了，正规方程为θ = (XT·X)-1·XT·y。值得注意的是这里需要对XT·X求逆矩阵，因此这个方程只有在逆矩阵存在的时候才适用，所以需要在代码中进行判断。
loaddataSet()函数是将文本数据分成特征集和标签。
'''
def loaddataSet(filename):
    numfeat = len(open(filename).readline().split('\t'))-1
    dataMat = [];labelsVec = []
    file = open(filename)
    for line in file.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numfeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelsVec.append(float(curLine[-1]))
    return dataMat,labelsVec

'''
standRegression()是利用正规方程求回归系数sigma，当然在使用正规方程前需要判断其是否有逆矩阵。
这种解法很简单，但是它的缺点我也在之前的理论部分说过了。
'''
def standRegression(xArr,yArr):
    xMat = mat(xArr);yMat = mat(yArr)
    xTx = xMat.T * xMat
    if linalg.det(xTx)==0.0:
        print('this matrix is singular,cannot do inverse\n')
        return
    sigma = xTx.I * (xMat.T * yMat.T)
    return sigma

def standRegression1(xArr,yArr):
    xMat = mat(xArr);
    yMat = mat(yArr);
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0.0:
        print('this')
        return
    sigma = xTx.I *(xMat.T * yMat.T)
    return sigma

'''
下面我们来看拟合的结果，利用PlotLine()函数来画图。注意这个函数的传入参数xMay和yMat需要为矩阵形式
'''
def PlotLine(xMat,yMat,sigma):
    ax = plt.subplot(111)
    ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0])
    xCopy = xMat.copy()
    xCopy.sort(0)
    yHat = xCopy*sigma
    ax.plot(xCopy[:,1],yHat)
    plt.show()
    
    
def lwlr(testPoint,xArr,yArr,k = 1.0):
    xMat = mat(xArr);yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye(m))
    for i in range(m):
        diffMat = testPoint - xMat[i,:]
        weights[i,i] = exp(diffMat * diffMat.T/(-2.0*k**2))
    xTWx = xMat.T * (weights*xMat)
    if linalg.det(xTWx)==0.0:
        print('this matrix is singular,cannot do inverse\n')
        return
    sigma = xTWx.I * (xMat.T * (weights * yMat))
    return testPoint * sigma

def lwlrTest(testArr,xArr,yArr,k = 1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i],xArr,yArr,k)
    return yHat
    
def PlotLine1(testArr,xArr,yArr,k = 1.0):
    xMat = mat(xArr)
    yMat = mat(yArr)
    yHat = lwlrTest(testArr,xArr,yArr,k)
    srtInd = xMat[:,1].argsort(0)
    xsort = xMat[srtInd][:,0,:]
    ax = plt.subplot(111)
    ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0],s = 2,c = 'red')
    ax.plot(xsort[:,1],yHat[srtInd])
    plt.show()

def lwlr(testPoint,xArr,yArr,k = 1.0):
    xMat = mat(xArr);yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye(m))
    for i in range(m):
        diffMat = testPoint - xMat[i,:]
        weights[i,i] = exp(diffMat * diffMat.T/(-2.0*k**2))
    xTWx = xMat.T * (weights*xMat)
    if linalg.det(xTWx)==0.0:
        print('this matrix is singular,cannot do inverse\n')
        return
    sigma = xTWx.I * (xMat.T * (weights * yMat))
    return testPoint * sigma

def lwlr2(testPoint,xArr,yArr,k = 1.0):
    xMat = mat(xArr);yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye(m))
    for i in range(m):
        diffMat = testPoint - xMat[i,:]
        weights[i,i] = exp(diffMat * diffMat.T/(-2.0*k**2))
    xTWx = xMat.T * (weights*xMat)
    if linalg.det(xTWx)==0.0:
        print('')
        return
    sigma = xTWx.I * (xMat.T * (weights * yMat))
    return testPoint * sigma

def lwlrTest(testArr,xArr,yArr,k = 1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i],xArr,yArr,k)
    return yHat

def PlotLine1(testArr,xArr,yArr,k = 1.0):
    xMat = mat(xArr)
    yMat = mat(yArr)
    yHat = lwlrTest(testArr,xArr,yArr,k)
    srtInd = xMat[:,1].argsort(0)
    xsort = xMat[srtInd][:,0,:]
    ax = plt.subplot(111)
    ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0],s = 2,c = 'red')
    ax.plot(xsort[:,1],yHat[srtInd])
    plt.show()

if __name__ == '__main__':
    #传入对应的路径 ，将文本数据分成特征集和标签
    dataMat,labelsVec = loaddataSet('ex0.txt')
    print(dataMat)
    print('33333333')
    print(labelsVec)
    #利用正规方程求回归系数sigma 使用正规方程前需要判断其是否有逆矩阵，
    sigma = standRegression(dataMat, labelsVec)
    print('sigma')
    print(sigma)
    #利用PlotLine()函数画图，当前函数传入的参数xMay yMat 需要为矩阵形式
    PlotLine(mat(dataMat), mat(labelsVec), sigma)
        
    