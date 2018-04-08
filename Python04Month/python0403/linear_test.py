# -*- coding: utf-8 -*-


from numpy import  *
import matplotlib.pyplot as plt

'''
将文本数据分成特征集和标签

'''

def loaddataSet(filename):
    numfeat1 = len(open(filename).readline().split('\t'))-1
    dataMat = [];
    labelsVec = [];
    file = open(filename)
    for line in file.readline():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numfeat1):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelsVec.append(float(curLine[-1]))
    return dataMat,labelsVec

'''
standRegression()利用正规方程求回归系数sigma,当然在使用正规方程前需要判断是否有逆矩阵
'''

def standRegression(xArr,yArr):
    xMat = mat(xArr);
    yMat = mat(yArr);
    xTx = xMat.T * xMat
    if linalg.det(xTx)==0.0:
        print('this ')
        return
    sigma = xTx.I * (xMat.T *yMat.T)
    return sigma

'''
获取拟合的结果 利用plotline()画图
'''
def PlotLine(xMat,yMat,sigma):
    ax = plt.subplot(111)
    ax.scatter(xMat[:,1].flattern().A[0], yMat.T[:, 0].flatten().A[0])
    xCopy = xMat.copy()
    xCopy.sort(0)
    yHat = xCopy*sigma
    ax.plot(xCopy[:,1],yHat)
    plt.show()

def lwlr(testPoint,xArr,yArr,k = 1.0):
    xMat = mat(xArr);
    yMat = mat(yArr).T;
    m = shape(xMat)[0]
    weights = mat(eye(m))
    for i in range(m):
        diffMat = testPoint - xMat[i,:]

