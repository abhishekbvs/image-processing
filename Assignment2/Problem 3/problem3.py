import cv2 
import numpy as np 
  
def pixelVal(pix, r1, s1, r2, s2): 
    if (0 <= pix and pix <= r1): 
        return (s1 / r1)*pix 
    elif (r1 < pix and pix <= r2): 
        return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1 
    else: 
        return ((255 - s2)/(255 - r2)) * (pix - r2) + s2 
  

img = cv2.imread('logndlinear.jpg') 
r1 = 70
s1 = 0
r2 = 140
s2 = 255
  
pixelVal_vec = np.vectorize(pixelVal) 
contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2)

c = 255/(np.log(1 + np.max(img))) 
log_transformed = c * np.log(1 + img)
log_transformed = np.array(log_transformed, dtype = np.uint8) 

cv2.imshow('contrast_stretch',contrast_stretched) 
cv2.imwrite('contrast_stretch.jpg', contrast_stretched) 

cv2.imwrite('log_transformed.jpg', log_transformed)
cv2.imshow('log_transformed',log_transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()