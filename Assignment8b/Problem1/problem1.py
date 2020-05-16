import cv2 
import numpy as np

img = cv2.imread('noisy_leaf.jpg', cv2.IMREAD_GRAYSCALE)  
cv2.imshow('gray', img)
blur = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('blur', img)
_,threshold = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 
cv2.imshow('otsus thresholded', threshold)
cv2.imwrite('otsus_thresholded.jpg',threshold)
cv2.waitKey(0)