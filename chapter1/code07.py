from pylab import *
import imtools  #查看imtools.py
im = imread('empire.jpg')   #用imread读取的结果是一个array而不是Image对象
height,width,channel=im.shape   #得到图像的高、宽和通道数量
sz=(int(width/2),int(height/2))
im_resized = imtools.imresize(im,sz)
subplot(121)
imshow(im)
subplot(122)
axis([0,width,height,0])    #设置坐标轴与im相同，y方向与常规的坐标轴相反
imshow(im_resized)
show()