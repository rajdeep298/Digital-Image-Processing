import cv2
import numpy as np

# Reading the image
img = cv2.imread("Images/img.png", 0)

# Thresholding the image
threshold = np.zeros(img.shape, dtype=np.uint8)
m = img.max() // 2
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if (img[i, j] > m):
            threshold[i, j] = 255
        else:
            threshold[i, j] = 0
cv2.imshow("Original Image", img)
cv2.imshow("Thresholded Image", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
