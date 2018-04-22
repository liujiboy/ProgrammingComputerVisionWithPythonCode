from pca import pca
from pylab import *
data=array([[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3]])
Vt, S, mean_X=pca(data)
print('投影矩阵：\n',Vt)
print('方差：\n',S)
print('将data投影到方差最大的1个方向（Vt的第1行）')
print(dot(data,Vt[:1].T))