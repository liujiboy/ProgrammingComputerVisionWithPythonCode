from pca import pca
from pylab import *
import numpy as np
def showDataAndAxis(data):
    Vt, S, mean_X=pca(data)
    figure()
    subplot(121)
    plot(data[:,0],data[:,1],'co')
    principalDirection1=array([[0,0],Vt[0]]) #第1主成分方向
    principalDirection2=array([[0,0],Vt[1]]) #第2主成分方向
    plot(principalDirection1[:,0],principalDirection1[:,1],'r',label='first principal direction')
    plot(principalDirection2[:,0],principalDirection2[:,1],'g',label='second principal direction')
    axis('equal')
    legend()
    title('origin data')
    subplot(122)
    newData=dot(data,Vt[:1].T)
    bar(arange(newData.shape[0]),newData) #用条形图显示投影后的一维数据
    xticks(arange(newData.shape[0]))
    xlabel('data index')
    ylabel('first principal value')
    title('projected data')
data=array([[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7]]) #直线数据
showDataAndAxis(data)
data=np.random.randn(20,2) #随机数据
showDataAndAxis(data)
degree=linspace(0,2*pi,20)
x=2*np.cos(pi/3-degree)
y=4*np.sin(degree)
data=vstack((x,y))  #椭圆数据
data=data.T
showDataAndAxis(data)
show()