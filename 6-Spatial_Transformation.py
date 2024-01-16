import cv2
import numpy as np

# image negative
img = cv2.imread("Images/img.png", 1)
imageNegative = 255 - img
cv2.imshow("Original Image", img)
cv2.imshow("Negative Image", imageNegative)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Log Transformation

# Performing Log Transformation
img = cv2.imread("Images/img.png", 1)
LogTransformation = np.log(img)
# Scaling to (0-255)
LogTransformation = (LogTransformation / np.max(LogTransformation)) * 255
# Converting into uint8
LogTransformation = np.array(LogTransformation, dtype=np.uint8)
cv2.imshow("Original Image", img)
cv2.imshow("Log Transformation Image", LogTransformation)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Power Law Transformation
img = cv2.imread("Images/img.png", 1)
n = float(input("Enter Gamma Value (0-1):"))
PowerLawTransformation = np.power(img, n)
# Scaling to (0-255)
PowerLawTransformation = (PowerLawTransformation / np.max(PowerLawTransformation)) * 255
# Converting into uint8
PowerLawTransformation = np.array(PowerLawTransformation, dtype=np.uint8)
cv2.imshow("Original Image", img)
cv2.imshow("Power Law Transformation Image", PowerLawTransformation)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Piecewise Linear Transformation
def PieceWiseLinearTransformation(pix, r1, s1, r2, s2):
    if (0 <= pix and pix <= r1):
        return (s1 / r1) * pix
    elif (r1 < pix and pix <= r2):
        return ((s2 - s1) / (r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2) / (255 - r2)) * (pix - r2) + s2


r1 = int(input("Enter r1:"))
s1 = int(input("Enter s1:"))
r2 = int(input("Enter r2:"))
s2 = int(input("Enter s2:"))
# Reading the image
img = cv2.imread("Images/img.png", 1)

# Vectorizing the function to apply it to each value in the Numpy array
PieceWiseLinearTransformation = np.vectorize(PieceWiseLinearTransformation)
# Applying Contrast Stretching
ContrastStretching = PieceWiseLinearTransformation(img, r1, s1, r2, s2)
# Converting into uint8
ContrastStretching = np.array(ContrastStretching, dtype=np.uint8)
cv2.imshow("Original Image", img)
cv2.imshow("Contrast Stretching Image", ContrastStretching)
cv2.waitKey(0)
cv2.destroyAllWindows()
