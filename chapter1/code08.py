import imtools
from pylab import *
def showImage(im):
    figure()
    subplot(221)
    axis('off')
    imshow(im)
    subplot(222)
    title('Histogram of red color')
    hist(im[:, :, 0].flatten(), bins=256)   #红色通道直方图
    subplot(223)
    title('Histogram of green color')
    hist(im[:, :, 1].flatten(), bins=256)   #绿色通道直方图
    subplot(224)
    title('Histogram of blue color')
    hist(im[:, :, 2].flatten(), bins=256)   #蓝色通道直方图

im=imread('handsome.jpg')   
showImage(im)   #显示图像和直方图
#分别调整r、g、b通道的对比度
red,rcdf=imtools.histeq(im[:,:,0])  
green,gcdf=imtools.histeq(im[:,:,1])
blue,bcdf=imtools.histeq(im[:,:,2])
#将调整后的值赋值给原图像
im[:,:,0]=red
im[:,:,1]=green
im[:,:,2]=blue
showImage(im)   #显示图像和直方图
#绘制cdf曲线
figure()
subplot(311)
plot(rcdf/255)  #重新归一化cdf的值域范围为[0,1]之间
subplot(312)
plot(gcdf/255)  #重新归一化cdf的值域范围为[0,1]之间
subplot(313)
plot(bcdf/255)  #重新归一化cdf的值域范围为[0,1]之间
show()
