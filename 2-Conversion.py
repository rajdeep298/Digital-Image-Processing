import cv2

# Color to Grayscale
img = cv2.imread("Images/img.png", 1)
cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("window", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Grayscale to Binary
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
# Here ret is storing the threshold limit and
# thresh is storing the converted image

cv2.imshow("window", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Color to Binary
ret2, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("window", thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# RGB to HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("window", img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

# HSV to RGB
img_rgb = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("window", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

# RGB to YCrCb
img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow("window", img_YCrCb)
cv2.waitKey(0)
cv2.destroyAllWindows()

# YCrCb to RGB
img_rgb = cv2.cvtColor(img_YCrCb, cv2.COLOR_YCrCb2BGR)
cv2.imshow("window", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()


