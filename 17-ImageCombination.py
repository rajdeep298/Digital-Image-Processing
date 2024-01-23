import cv2 as cv
import numpy as np
leena_img=cv.imread("Images/lena.bin",0)
peeper_img=cv.imread("Images/peppers.bin",0)
j=np.zeros([256,256],np.uint8)
for i in range(256):
    for k in range(256):
        if(k<128):
            j[i,k]=leena_img[i,k]
        else:
            j[i,k]=peeper_img[i,k]
cv.imshow("combined image",j)

cv.waitKey(0)