import cv2
import matplotlib.pyplot as plt

# Reading the image
img = cv2.imread("Images/img.png", cv2.IMREAD_GRAYSCALE)

# Histogram Equalization
equ = cv2.equalizeHist(img)

# Plotting the graphs
plt.figure(figsize=(8, 8))  # This is used to change the size of the figure/plot

plt.subplot(2, 2, 1)  # This is used to plot multiple plots in the same figure
# The first 2 is for the number of rows, the second 2 is for the number of columns and the third 1 is for the
# position of the plot
plt.imshow(img, cmap="gray")
plt.title("Original Image")

plt.subplot(2, 2, 2)
plt.imshow(equ, cmap="gray")
plt.title("Histogram Equalized Image")

plt.show()  # This is used to show the figure/plot

