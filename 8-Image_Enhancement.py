import cv2
import numpy as np

img = cv2.imread("Images/img.png", 1)
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Brightness Enhancement
brightnessEnhancement = 100
img = img + brightnessEnhancement
cv2.imshow("Brighten Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Brightness Reduction
brightnessReduction = 100
img = img - brightnessReduction
cv2.imshow("Darken Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Contrast Manipulation
alpha = 1.5  # Contrast control (1.0-3.0), 1.0 means no change, more than 1.0 means more contrast
beta = 0  # Brightness control (0-100), 0 means no change, more than 0 means more brightness
img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
cv2.imshow('Contrast Manipulated Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Grey Level Slicing without Background
img = cv2.imread("Images/img.png", 0)
low_threshold = 80
high_threshold = 200
new_img = np.zeros(img.shape, np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if ((img[i, j] > low_threshold) and (img[i, j] <= high_threshold)):
            new_img[i, j] = 255
        else:
            new_img[i, j] = 0

# Display the image
cv2.imshow("Output Image", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
