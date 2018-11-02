# %matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
def imag_tile(img, n, m=1):
    """
    The image "img" will be repeated n times in 
    vertical and m times in horizontal direction.
    """
    if n == 1:
        tiled_img = img
    else:
        lst_imgs = []
        for i in range(n):
             lst_imgs.append(img)  
        tiled_img = np.concatenate(lst_imgs, axis=1 )
    if m > 1:
        lst_imgs = []
        for i in range(m):
             lst_imgs.append(tiled_img)  
        tiled_img = np.concatenate(lst_imgs, axis=0 )
          
    return tiled_img
basic_pattern = mpimg.imread('imag_tile_explanation.png')
decorators_img = imag_tile(basic_pattern, 3, 3)
print decorators_img
plt.axis("off")
plt.imshow(decorators_img)
cropped = basic_pattern[90:150, 50:120]
# print(at_img.shape)
mpimg.imsave('/home/halk/Pictures/decorators_with_at.png', cropped)

mpimg.imsave('/home/halk/Pictures/decorators_with_at1.png', decorators_img)
