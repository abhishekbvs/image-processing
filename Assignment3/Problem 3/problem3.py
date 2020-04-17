import cv2
import numpy as np

img = cv2.imread('Fig09_11.tif',cv2.IMREAD_UNCHANGED)
kernel = np.ones((5,5), np.uint8)
kernel2 = np.ones((7,7), np.uint8)
kernel3 = np.array((
	[0, 1, 0],
	[1, 1, 1],
	[0, 1, 0]),dtype='uint8')

img_opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img_closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

img_erosion = cv2.erode(img, kernel3, iterations=1)
img_dilation = cv2.dilate(img_erosion, kernel3, iterations=1)
img_opening3 = cv2.morphologyEx(img_dilation, cv2.MORPH_OPEN, kernel2)
img_closing2 = cv2.morphologyEx(img_dilation, cv2.MORPH_CLOSE, kernel)
img_opening2 = cv2.morphologyEx(img_closing2, cv2.MORPH_OPEN, kernel3)


opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Input', img) 
cv2.imshow('Opening', img_opening)
cv2.imshow('Closing', img_closing)
cv2.imshow('Erosion&Dilation', img_dilation)
cv2.imshow('Erode&Dilate&Close',img_closing2)
cv2.imshow('Processed',img_closing2)
cv2.imshow('Improved', close) 


cv2.imwrite('Input.jpg', img) 
cv2.imwrite('Opening.jpg', img_opening)
cv2.imwrite('Closing.jpg', img_closing)
cv2.imwrite('Erosion&Dilation.jpg', img_dilation)
cv2.imwrite('Erode&Dilate&Close.jpg',img_closing2)
cv2.imwrite('Processed.jpg',img_closing2)
cv2.imwrite('Improved.jpg', close) 

cv2.waitKey(0)
cv2.destroyAllWindows()