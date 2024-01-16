import cv2
import matplotlib.pyplot as plt
import numpy as np

# Reading the image
img = cv2.imread("Images/img.png", cv2.IMREAD_GRAYSCALE)

# # Histogram Equalization
# equ = cv2.equalizeHist(img)
#
# # Plotting the graphs
# plt.figure(figsize=(8, 8))  # This is used to change the size of the figure/plot
#
# plt.subplot(2, 2, 1)  # This is used to plot multiple plots in the same figure
# # The first 2 is for the number of rows, the second 2 is for the number of columns and the third 1 is for the
# # position of the plot
# plt.imshow(img, cmap="gray")
# plt.title("Original Image")
#
# plt.subplot(2, 2, 2)
# plt.imshow(equ, cmap="gray")
# plt.title("Histogram Equalized Image")
#
# plt.show()  # This is used to show the figure/plot

#or it can be done as follows
pixels = img.ravel() # This is used to convert the 2D array into 1D array
length = len(pixels)

#Initializing the arrays for Histogram and Cumulative Frequency
h = np.zeros(256, np.uint64)
f = np.zeros(256, np.uint64)

#Calculating the Histogram
for i in range(256):
    for j in pixels:
        if i == j:
            h[i] = h[i] + 1

#Calculating the Cumulative Frequency
cf=0
for i in range(0,256):
    cf = cf + (h[i] / length)
    p = cf * 255
    f[i] = p

#Create a new image with equalized histogram
img2 = np.zeros(img.shape, np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img2[i, j] = f[img[i, j]]


#Display the new image
cv2.imshow("hist_equi", img2)
cv2.imshow("original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

