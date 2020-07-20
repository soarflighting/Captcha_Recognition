import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def convert2gray(img):
    if len(img.shape)>2:
        r,g,b =img[:,:,0],img[:,:,1],img[:,:,2]
        gray = 0.2989*r+0.5870*g+0.1140*b
        return gray
    else:
        return img

if __name__ == '__main__':
    img = mpimg.imread("../start.jpg")
    plt.imshow(img,cmap='Greys_r')
    print(img.shape)
    plt.show()
    gray_img = convert2gray(img)
    plt.imshow(gray_img,cmap='Greys_r')
    print(gray_img.shape)
    plt.show()