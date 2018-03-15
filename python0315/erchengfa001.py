'''

2 scipy库中的leastsq函数

当然，最小二乘法本身实现起来也是不难的，就如我们上面所说的不断调整参数，然后令误差函数Err不断减小就行了。我们将在下一次博客中详细说明如何利用梯度下降法来完成这个目标。

而在本篇博客中，我们介绍一个scipy库中的函数，叫leastsq，它可以省去中间那些具体的求解步骤，只需要输入一系列样本点，给出待求函数的基本形状（如我刚才所说，二元二次函数就是一种形状——f(x,y)=w0x^2+w1y^2+w2xy+w3x+w4y+w5，在形状给定后，我们只需要求解相应的系数w0~w6），即可得到相应的参数。至于中间到底是怎么求的，这一部分内容就像一个黑箱一样。
2-1 函数形为y=kx+b

这一次我们给出函数形y=kx+b。这种情况下，待确定的参数只有两个：k和b。

此时给出7个样本点如下：

则使用leastsq函数求解其拟合直线的代码如下：
'''


###最小二乘法试验###
import numpy as np
from scipy.optimize import leastsq

###采样点(Xi,Yi)###
Xi=np.array([8.19,2.72,6.39,8.71,4.7,2.66,3.78])
Yi=np.array([7.01,2.78,6.47,6.71,4.1,4.23,4.05])

###需要拟合的函数func及误差error###
def func(p,x):
    k,b=p
    return k*x+b

def error(p,x,y,s):
    print (s)
    return func(p,x)-y #x、y都是列表，故返回值也是个列表

#TEST
p0=[100,2]
#print( error(p0,Xi,Yi) )

###主函数从此开始###
s="Test the number of iteration" #试验最小二乘法函数leastsq得调用几次error函数才能找到使得均方误差之和最小的k、b
Para=leastsq(error,p0,args=(Xi,Yi,s)) #把error函数中除了p以外的参数打包到args中
k,b=Para[0]
print("k=",k,'\n',"b=",b)

###绘图，看拟合效果###
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
plt.scatter(Xi,Yi,color="red",label="Sample Point",linewidth=3) #画样本点
x=np.linspace(0,10,1000)
y=k*x+b
plt.plot(x,y,color="orange",label="Fitting Line",linewidth=2) #画拟合直线
plt.legend()
plt.show()

'''
我把里面需要注意的点提点如下：

1、p0里放的是k、b的初始值，这个值可以随意指定。往后随着迭代次数增加，k、b将会不断变化，使得error函数的值越来越小。

2、func函数里指出了待拟合函数的函数形状。

3、error函数为误差函数，我们的目标就是不断调整k和b使得error不断减小。这里的error函数和神经网络中常说的cost函数实际上是一回事，只不过这里更简单些而已。

4、必须注意一点，传入leastsq函数的参数可以有多个，但必须把参数的初始值p0和其它参数分开放。其它参数应打包到args中。

5、leastsq的返回值是一个tuple，它里面有两个元素，第一个元素是k、b的求解结果，第二个元素我暂时也不知道是什么意思，先留下来。
'''