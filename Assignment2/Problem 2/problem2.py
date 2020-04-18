import cv2

img = cv2.imread('ChessBoardGrad.png')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray Image', grayImg)

filtersize = 513
gaussianImg = cv2.GaussianBlur(grayImg, (filtersize, filtersize), 128)
cv2.imshow('Gaussian Image', gaussianImg)

newImg = (grayImg-gaussianImg)
cv2.imshow('Final Image', newImg)
cv2.imwrite('Final.png', newImg)
cv2.waitKey(0)

cv2.destroyAllWindows()