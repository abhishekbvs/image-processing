import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.exposure import rescale_intensity

def convolve(image, kernel):
	(iH, iW) = image.shape[:2]
	(kH, kW) = kernel.shape[:2]
	pad = (kW - 1) // 2
	image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
		cv2.BORDER_REPLICATE)
	output = np.zeros((iH, iW), dtype="float32")
	for y in np.arange(pad, iH + pad):
		for x in np.arange(pad, iW + pad):
			roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
			k = (roi * kernel).sum()
			output[y - pad, x - pad] = k

	output = rescale_intensity(output, in_range=(0, 255))
	output = (output * 255).astype("uint8")
	return output

img1 = cv2.imread('ChessBoardGrad.png')
img2 = cv2.imread('Lenna.png')

#Laplacian kernel

laplacian = np.array((
	[0, 1, 0],
	[1, -4, 1],
	[0, 1, 0]), dtype="int")

# Sobel kernel in x direction

sobelX = np.array((
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]), dtype="int")

# Sobel kernel in y  direction

sobelY = np.array((
	[-1, -2, -1],
	[0, 0, 0],
	[1, 2, 1]), dtype="int")

kernelBank = (
	("laplacian", laplacian),("sobel_x", sobelX),("sobel_y", sobelY),
)

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

for (kernelName, kernel) in kernelBank:
    
    convoleOutput = convolve(gray1, kernel)
    opencvOutput = cv2.filter2D(gray1, -1, kernel)
    cv2.imshow("original", gray1)
    cv2.imshow("{} - convole".format(kernelName), convoleOutput)
    cv2.imshow("{} - opencv".format(kernelName), opencvOutput)
    cv2.imwrite(kernelName+"ChessBoardGrad.png", convoleOutput)

    print("[INFO] applying {} kernel".format(kernelName))
    convoleOutput = convolve(gray2, kernel)
    opencvOutput = cv2.filter2D(gray2, -1, kernel)
    cv2.imshow("original", gray2)
    cv2.imshow("{} - convole".format(kernelName), convoleOutput)
    cv2.imshow("{} - opencv".format(kernelName), opencvOutput)
    cv2.imwrite(kernelName+"Lenna.png", convoleOutput)

    
    

#Canny

edges1 = cv2.Canny(img1,100,200)
cv2.imshow('Edges',edges1)
cv2.imwrite('CannyChessBoardGrad.png', edges1)

edges2 = cv2.Canny(img2,100,200)
cv2.imshow('Edges',edges2)
cv2.imwrite('CannyLenna.png', edges2)


cv2.waitKey(0)
cv2.destroyAllWindows()