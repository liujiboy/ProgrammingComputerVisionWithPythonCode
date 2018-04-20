from PIL import Image
from pylab import *
im = array(Image.open('empire.jpg').convert('L'),'f') 
print(im.shape, im.dtype)
im = array(Image.open('empire.jpg'))
print(im.shape, im.dtype)
i=100
j=50
k=1
value=im[i,j,k]
print("value\n",value)
im[i,:] = im[j,:]   # set the values of row i with values from row j
print("im[j,:]\n",im[j,:])
print("im[i,:]\n",im[i,:])
im[:,i] = 100   # set all values in column i to 100
print("im[:,i]\n",im[:,i])
print("im[:100,:50].sum()\n",im[:100,:50].sum())   # the sum of the values of the first 100 rows and 50 columns
print("im[50:100,50:100]\n",im[50:100,50:100])    # rows 50-100, columns 50-100 (100th not included)
print("im[i].mean()\n",im[i].mean())     # average of row i
print("im[:,-1]\n",im[:,-1])     # last column
print("im[-2,:]\n",im[-2,:]) # second to last row
print("im[-2]\n",im[-2]) # second to last row