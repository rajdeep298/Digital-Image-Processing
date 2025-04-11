import cv2

img1 = cv2.imread("Images/img.png", 1)
img2 = cv2.imread("Images/Tom_Jerry.jpg", 1)
cv2.imshow("Original Image 1", img1)
cv2.imshow("Original Image 2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

rows, cols, ch = img1.shape
img2 = cv2.resize(img2, (cols, rows))

# Addition
add = img1 + img2
# add = cv2.add(img1, img2)  # This is the same as the above line
cv2.imshow("Addition", add)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Subtraction
sub = img1 - img2
# sub = cv2.subtract(img1, img2)  # This is the same as the above line
cv2.imshow("Subtraction", sub)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Multiplication
mul = img1 * img2
# mul = cv2.multiply(img1, img2)  # This is the same as the above line
cv2.imshow("Multiplication", mul)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Division
div = img1 / img2
# div = cv2.divide(img1, img2)  # This is the same as the above line
cv2.imshow("Division", div)
cv2.waitKey(0)
cv2.destroyAllWindows()
