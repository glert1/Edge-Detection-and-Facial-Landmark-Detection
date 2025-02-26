import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
 
img = cv.imread('/your image path', cv.IMREAD_GRAYSCALE)
canny_edges = cv.Canny(img,100,200)
laplacian_edge = cv.Laplacian(img,cv.CV_64F)
sobelY_edge = cv.Sobel(img,cv.CV_64F,0,1, ksize=5)

 
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(canny_edges,cmap = 'gray')
plt.title('Canny'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(laplacian_edge,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobel_edge,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
 
plt.show()