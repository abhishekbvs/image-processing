import cv2
import numpy as np

img = cv2.imread('Fig09_16.tif', cv2.IMREAD_UNCHANGED)
kernel = np.ones((5,5), np.uint8)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('Input', img) 
cv2.imshow('Outline', gradient) 

cv2.imwrite('Outline.jpg', gradient) 

cv2.waitKey(0)
cv2.destroyAllWindows()