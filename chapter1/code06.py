from PIL import Image 
from numpy import *
from pylab import *
im = array(Image.open('empire.jpg').convert('L')) #convert to gray image
im2 = 255 - im #invert image
im3 = (100.0/255) * im + 100 #clamp to interval 100...200 
im4 = 255.0 * (im/255.0)**2 #squared
subplot(221)
title('origin image')
axis('off')
imshow(im,cmap='gray')
subplot(222)
title('inverted image')
axis('off')
imshow(im2,cmap='gray')
subplot(223)
title('clamped image')
axis('off')
imshow(im3,cmap='gray')
subplot(224)
title('squared image')
axis('off')
imshow(im4,cmap='gray')
show()