import cv2
import math
import numpy


img = cv2.imread("8.jpg")
dim = img.shape

#1
angle=45
scale=1

while angle>360:
	angle=angle-360
while angle<0:
	angle+=360

rot=img
for i in range(8):
	dim=rot.shape
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

	rot = cv2.warpAffine(rot,m,
	(math.ceil(dim[0]*abs(math.sin(math.radians(angle)))+dim[1]*abs(math.cos(math.radians(angle)))),
	math.ceil(dim[0]*abs(math.cos(math.radians(angle)))+dim[1]*abs(math.sin(math.radians(angle))))),flags = cv2.INTER_CUBIC)

cv2.imshow("rotated 8 times",rot)
cv2.imwrite("rotated 8 times.jpg",rot)

#2
angle=90
scale=1

while angle>360:
	angle=angle-360
while angle<0:
	angle+=360

rot=img
for i in range(4):
	dim=rot.shape
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

	rot = cv2.warpAffine(rot,m,
	(math.ceil(dim[0]*abs(math.sin(math.radians(angle)))+dim[1]*abs(math.cos(math.radians(angle)))),
	math.ceil(dim[0]*abs(math.cos(math.radians(angle)))+dim[1]*abs(math.sin(math.radians(angle))))),flags = cv2.INTER_CUBIC)

cv2.imshow("rotated 4 times",rot)
cv2.imwrite("rotated 4 times.jpg",rot)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
here we can see that the 90 degree rotated image is much similar to the original image while the 45 degree rotated image 
has degraded a lot.
there 2 main reasons to this, 
	1) 45 degree rotation is a lossy rotation where there is a lot of interpolation required resulting in degraded image, 
	while 90 degree rotation is a lossless rotation
	2) 45 degree is rotated 8 times while 90 degree is rotated only 4 times

another difference in the images are 45 degree rotated image's dimention has increased tremendously while dimention 
remains unchanged for the 90 degree rotated image
"""