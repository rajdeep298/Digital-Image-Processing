import cv2
import numpy as np


def RobertOperatorX(img, x, y):
    maskx = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
    f = maskx[0, 0] * img[x - 1, y - 1] + maskx[0, 1] * img[x - 1, y] + maskx[0, 2] * img[x - 1, y + 1] + maskx[1, 0] * \
        img[x, y - 1] + maskx[1, 1] * img[x, y] + maskx[1, 2] * img[x, y + 1]
    return f


def RobertOperatorY(img, x, y):
    masky = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 0]])
    g = masky[0, 0] * img[x - 1, y - 1] + masky[0, 1] * img[x - 1, y] + masky[0, 2] * img[x - 1, y + 1] + masky[1, 0] * \
        img[x, y - 1] + masky[1, 1] * img[x, y] + masky[1, 2] * img[x, y + 1]
    return g


def RobertOperator(img, rows, cols):
    img2 = np.zeros(img.shape, np.uint8)
    img3 = np.zeros(img.shape, np.uint8)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            img2[i, j] = RobertOperatorX(img, i, j)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            img3[i, j] = RobertOperatorY(img, i, j)

    return img2, img3


# Reading the image
img = cv2.imread("Images/img.png", 0)
rows, cols = img.shape
cv2.imshow("Original Image", img)
cv2.waitKey(0)

# Robert Operator
imgx, imgy = RobertOperator(img, rows, cols)
cv2.imshow("Robert Operator X", imgx)
cv2.imshow("Robert Operator Y", imgy)
cv2.waitKey(0)
cv2.destroyAllWindows()
