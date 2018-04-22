from pylab import *
def pca(X):
    """ Principal Component Analysis
    input: X, 每行对应一个数据
    return: 投影矩阵（每行对应一个主成分方向），方差（与主成分对应），均值 """
    # 行数对应num_data，列数对应dim
    num_data, dim = X.shape
    # 将数据以均值为中心对齐
    mean_X = X.mean(axis=0)
    X = X - mean_X
    if dim>num_data:
        # 用协方差求解PCA
        M = dot(X,X.T) # 计算协方差
        e,EV = linalg.eigh(M) # 求特征值和特征向量
        #以下部分的含义请参考PCA算法
        tmp = dot(X.T,EV).T  
        Vt = tmp[::-1] 
        S = sqrt(e)[::-1] 
        for i in range(Vt.shape[1]): 
            Vt[:,i] /= S
    else:
        #当dim<num_data时可以采用SVD求解PCA
        U, S, Vt = linalg.svd(X) #X=U*diag(S)*V^t
        Vt = Vt[:num_data]
    # 返回投影矩阵，方差和均值
    return Vt, S, mean_X
