import cv2
import math
import numpy

angle=45
scale=10

img = cv2.imread("block.png")
dim = img.shape

while angle>360:
	angle=angle-360
while angle<0:
	angle+=360

m = cv2.getRotationMatrix2D((0,0),angle,scale)

if angle>90 and angle<270:
	m[0][2] += dim[1]*abs(math.cos(math.radians(angle)))
if angle>180:
	m[0][2] += dim[0]*abs(math.sin(math.radians(angle)))
if angle<180:
	m[1][2] += dim[1]*abs(math.sin(math.radians(angle)))
if angle>90 and angle<270:
	m[1][2] += dim[0]*abs(math.cos(math.radians(angle)))

m[0][2]*=scale
m[1][2]*=scale

#1
rotnn = cv2.warpAffine(img,m,
	(math.ceil(dim[0]*abs(math.sin(math.radians(angle)))+dim[1]*abs(math.cos(math.radians(angle))))*10,
	math.ceil(dim[0]*abs(math.cos(math.radians(angle)))+dim[1]*abs(math.sin(math.radians(angle))))*10),flags = cv2.INTER_NEAREST)

#2
rotbl = cv2.warpAffine(img,m,
	(math.ceil(dim[0]*abs(math.sin(math.radians(angle)))+dim[1]*abs(math.cos(math.radians(angle))))*10,
	math.ceil(dim[0]*abs(math.cos(math.radians(angle)))+dim[1]*abs(math.sin(math.radians(angle))))*10),flags = cv2.INTER_LINEAR)

#3
rotbc = cv2.warpAffine(img,m,
	(math.ceil(dim[0]*abs(math.sin(math.radians(angle)))+dim[1]*abs(math.cos(math.radians(angle))))*10,
	math.ceil(dim[0]*abs(math.cos(math.radians(angle)))+dim[1]*abs(math.sin(math.radians(angle))))*10),flags = cv2.INTER_CUBIC)

cv2.imshow("rotated nearest",rotnn)
cv2.imshow("rotated bilinear",rotbl)
cv2.imshow("rotated bicubic",rotbc)
cv2.imwrite("rotated nearest.jpg",rotnn)
cv2.imwrite("rotated bilinear.jpg",rotbl)
cv2.imwrite("rotated bicubic.jpg",rotbc)
cv2.waitKey(0)
cv2.destroyAllWindows()