import cv2
import numpy as np


# Mean Filter
def MeanFilter(img, rows, cols):
    # Creating the mask
    mask = np.ones([3, 3], dtype=np.uint8)
    mask = mask / 9
    # Performing convolution
    img_new = np.zeros(img.shape, dtype=np.uint8)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            temp = img[i - 1, j - 1] * mask[0, 0] + img[i - 1, j] * mask[0, 1] + img[i - 1, j + 1] * mask[0, 2] + img[
                i, j - 1] * mask[1, 0] + img[i, j] * mask[1, 1] + img[i, j + 1] * mask[1, 2] + img[i + 1, j - 1] * mask[
                       2, 0] + img[i + 1, j] * mask[2, 1] + img[i + 1, j + 1] * mask[2, 2]
            img_new[i, j] = temp
    return img_new.astype(np.uint8)


# Weighted Average Filter
def WeightedAverageFilter(img, rows, cols):
    # Creating the mask
    mask = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
    mask = mask / 16
    # Performing convolution
    img_new = np.zeros(img.shape, dtype=np.uint8)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            temp = img[i - 1, j - 1] * mask[0, 0] + img[i - 1, j] * mask[0, 1] + img[i - 1, j + 1] * mask[0, 2] + img[
                i, j - 1] * mask[1, 0] + img[i, j] * mask[1, 1] + img[i, j + 1] * mask[1, 2] + img[i + 1, j - 1] * mask[
                       2, 0] + img[i + 1, j] * mask[2, 1] + img[i + 1, j + 1] * mask[2, 2]
            img_new[i, j] = temp
    return img_new.astype(np.uint8)



# Median Filter
def MedianFilter(img, rows, cols):
    # Performing convolution
    img_new = np.zeros(img.shape, dtype=np.uint8)
    img = np.array(img, dtype=np.uint8)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            temp = [img[i - 1, j - 1], img[i - 1, j], img[i - 1, j + 1], img[i, j - 1], img[i, j], img[i, j + 1],
                    img[i + 1, j - 1], img[i + 1, j], img[i + 1, j + 1]]
            img_new[i, j] = np.median(temp)
    return img_new.astype(np.uint8)

# Max Filter
def MaxFilter(img, rows, cols):
    # Performing convolution
    img_new = np.zeros(img.shape, dtype=np.uint8)
    img = np.array(img, dtype=np.uint8)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            temp = [img[i - 1, j - 1], img[i - 1, j], img[i - 1, j + 1], img[i, j - 1], img[i, j], img[i, j + 1],
                    img[i + 1, j - 1], img[i + 1, j], img[i + 1, j + 1]]
            img_new[i, j] = np.max(temp)
    return img_new.astype(np.uint8)

# Min Filter
def MinFilter(img, rows, cols):
    # Performing convolution
    img_new = np.zeros(img.shape, dtype=np.uint8)
    img = np.array(img, dtype=np.uint8)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            temp = [img[i - 1, j - 1], img[i - 1, j], img[i - 1, j + 1], img[i, j - 1], img[i, j], img[i, j + 1],
                    img[i + 1, j - 1], img[i + 1, j], img[i + 1, j + 1]]
            img_new[i, j] = np.min(temp)
    return img_new.astype(np.uint8)


# Reading the image
img = cv2.imread("Images/img.png", 1)

rows,cols= img.shape
# Displaying the image
img_new = MeanFilter(img, rows, cols)
cv2.imshow("Original Image", img)
cv2.imshow("Mean Filtered Image", img_new)

img_new = WeightedAverageFilter(img, rows, cols)
cv2.imshow("Weighted Average Filtered Image", img_new)

img_new = MedianFilter(img,rows,cols)
cv2.imshow("Median Filtered Image", img_new)

img_new = MaxFilter(img,rows,cols)
cv2.imshow("Max Filtered Image", img_new)

img_new = MinFilter(img,rows,cols)
cv2.imshow("Min Filtered Image", img_new)

cv2.waitKey(0)
cv2.destroyAllWindows()
