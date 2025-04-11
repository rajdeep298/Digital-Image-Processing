import numpy as np
import cv2

img = cv2.imread("Images/img.png", 1)
cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Splitting the image into RGB
b, g, r = cv2.split(img)

k = np.zeros_like(b)

# Merging the image
b = cv2.merge((b, k, k))  # cv2.merge( (b, g, r) )
g = cv2.merge((k, g, k))
r = cv2.merge((k, k, r))

cv2.imshow("red", r)
cv2.imshow("green", g)
cv2.imshow("blue", b)
cv2.waitKey(0)
cv2.destroyAllWindows()
