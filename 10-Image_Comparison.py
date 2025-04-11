import cv2
import numpy as np

# Reading the image
img1 = cv2.imread("Images/img.png", 1)
img2 = cv2.imread("Images/Tom_Jerry.jpg", 1)
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Comparison
compare = np.abs(img1 - img2)
cv2.imshow("Original Image 1", img1)
cv2.imshow("Original Image 2", img2)
cv2.imshow("Compared Image", compare)
cv2.waitKey(0)
