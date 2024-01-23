import cv2
import numpy as np

# Reading the image
lena_img=cv2.imread("Images/lena.bin", 0)
peepers_img=cv2.imread("Images/peppers.bin", 0)

#Resize
lena_img=cv2.resize(lena_img, (256, 256))
peepers_img=cv2.resize(peepers_img, (256, 256))

#Display
cv2.imshow("leena", lena_img)
cv2.imshow("peeper", peepers_img)
cv2.waitKey(0)

#Combining
j=np.zeros([256,256],np.uint8)
for i in range(256):
    for k in range(256):
        if(k<128):
            j[i,k]=lena_img[i,k]
        else:
            j[i,k]=peepers_img[i,k]
cv2.imshow("combined image",j)
cv2.waitKey(0)
cv2.destroyAllWindows()