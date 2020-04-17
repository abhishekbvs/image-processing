import cv2 
import numpy as np

img = cv2.imread('Fig09_7.tif', cv2.IMREAD_UNCHANGED)
kernel = np.ones((5,5), np.uint8)
kernel2 = np.ones((2,2), np.uint8)

img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel2, iterations=1) 
img_opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img_closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

img_dilation2 = cv2.dilate(img, kernel, iterations=1) 
img_erosion2 = cv2.erode(img_dilation2, kernel, iterations=1)

cv2.imshow('Input', img) 

cv2.imshow('Dilation', img_dilation) 
cv2.imshow('Dilation&Erosion', img_erosion2) 
cv2.imshow('Processed2', img_dilation + img_closing - img_erosion + img_opening) 
cv2.imshow('Processed1', img_closing - img_erosion + img_opening)
 
cv2.imwrite('Dilation.jpg', img_dilation) 
cv2.imwrite('Dilation&Erosion.jpg', img_erosion2) 
cv2.imwrite('Processed2.jpg', img_dilation + img_closing - img_erosion + img_opening) 
cv2.imwrite('Processed1.jpg', img_closing - img_erosion + img_opening) 

cv2.waitKey(0)
cv2.destroyAllWindows()