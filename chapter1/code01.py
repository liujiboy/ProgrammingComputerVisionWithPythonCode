from PIL import Image
from pylab import * #import pylab中的所有模块、函数
pil_im = Image.open('empire.jpg')
pil_im_gray=Image.open('empire.jpg').convert('L') #将图像变为灰度图
figure()    #创建窗口
subplot(131)    #窗口划分为1行3列，在第1列绘图
imshow(pil_im)
subplot(132)    #在第2列绘图
imshow(pil_im_gray,cmap='gray') #图像以gray方式显示，请试试删除cmap参数，看看有什么区别
subplot(133)    #在第3列绘图
#从pil_im中剪切一块，旋转后粘贴到pil_im上，最后显示pil_im
box = (100,100,400,400)
region = pil_im.crop(box)
region = region.transpose(Image.ROTATE_180)
pil_im.paste(region,box)
imshow(pil_im)
axis('off') #第3列不显示axis
show()  #显示窗口