import cv2
import random
import numpy as np

def addSaltPepperNoise(img, n):
    row, col = img.shape
    for i in range(1, n + 1):  # Pick random number of pixels to change into white
        x = random.randint(0, row - 1)
        y = random.randint(0, col - 1)
        img[x, y] = 255
    for i in range(1, n + 1):  # Pick random number of pixels to change into black
        x = random.randint(0, row - 1)
        y = random.randint(0, col - 1)
        img[x, y] = 0
    return img

def addGaussianNoise(img, mean, sigma):
    row, col = img.shape
    gauss = np.zeros((row, col))
    cv2.randn(gauss, mean,sigma)
    gauss=(gauss**0.7).astype(np.uint8)
    noisy = img + gauss
    return noisy

# Reading the image
img = cv2.imread("Images/img.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original Image", img)
cv2.waitKey(0)

# Specify the number of noises
num_noises = 500  # You can adjust this number based on your requirement

# Adding salt and pepper noise
img1 = addSaltPepperNoise(img.copy(), num_noises)

cv2.imshow("Image with Salt Pepper Noise", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Adding Gaussian Noise
img2 = addGaussianNoise(img.copy(), 127, 40)
cv2.imshow("Image with Gaussian Noise", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
