import cv2
import numpy as np

img = cv2.imread('page.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('gray', img)

_, global_th = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
cv2.imshow('global_thresholded', global_th)
cv2.imwrite('global_thresholded.jpg', global_th)

local_th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow('local_thresholded', local_th)
cv2.imwrite('local_thresholded.jpg',local_th)
cv2.waitKey(0)

