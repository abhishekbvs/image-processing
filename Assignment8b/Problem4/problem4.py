import numpy as np
import cv2

def kmeans(k,img):
    Z = img.reshape((-1,3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret,label,center=cv2.kmeans(Z,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    cv2.imshow('k='+str(k),res2)
    cv2.imwrite('k='+str(k)+'.jpg',res2)


if __name__ =='__main__':
    img = cv2.imread('building.png')
    kmeans(3,img)
    kmeans(5,img)
    kmeans(8,img)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()


    