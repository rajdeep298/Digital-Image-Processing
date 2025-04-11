import cv2

img = cv2.imread("Images/img.png", 1)
rols, cols, ch = img.shape

# Rotation about center 90 degree anti-clockwise
matrix = cv2.getRotationMatrix2D((rols / 2, cols / 2), -90, 1)  # 1 is the scale factor
new_img = cv2.warpAffine(img, matrix, (rols, cols))  # warpAffine is used to apply the matrix on the image
# (rols, cols) is the size of the new image

cv2.imshow("window", new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Rotation about center 90 degree clockwise
matrix = cv2.getRotationMatrix2D((rols / 2, cols / 2), +90, 1)
new_img = cv2.warpAffine(img, matrix, (rols, cols))

cv2.imshow("window", new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
