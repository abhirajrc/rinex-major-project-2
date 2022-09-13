import cv2
import numpy as np

n_down_sampling = 2 # no. of downsampling steps
n_bilateral_filtering = 7 # no. of bilateral filtering steps
img_rgb = cv2.imread("th-298586715.jpg") #reads the image
print(img_rgb.shape) #prints the dimensions of the image

img_rgb = cv2.resize(img_rgb,(600,600)) #resizing the image to get best results

#Down sampling image using Gaussian pyramid
img_color = img_rgb
for _ in range(n_down_sampling):
    img_color = cv2.pyrDown(img_color)

#Applying small bilateral filter repeatedly instead of one large filter
    for _ in range(n_bilateral_filtering):
        img_color = cv2.bilateralFilter(img_color,d=9,sigmaColor=9,sigmaSpace=7)

#Unsampling image to original size
        for _ in range(n_down_sampling):
            img_color = cv2.pyrUp(img_color)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
            img_blur = cv2.medianBlur(img_gray,7)
            img_edge = cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                                             cv2.THRESH_BINARY,blockSize=9,C=2)
            

#converting back to color image, bit-AND with color image
            img_edge = cv2.cvtColor(img_edge,cv2.COLOR_GRAY2RGB) #converts an image from one colorspace to another
            img_cartoon = cv2.bitwise_and(img_color, img_edge) #applies bitwise and
            stack = np.hstack([img_rgb,img_cartoon]) #stacks the image
            cv2.imshow('Cartoonized Image',stack) #displays the images
            cv2.waitKey(0) #display the window indefinitely
