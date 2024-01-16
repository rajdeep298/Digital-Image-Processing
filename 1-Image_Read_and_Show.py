import cv2

img = cv2.imread('Images/img.png', 1)

# 1reads colour image
# 0 reads grayscale image
# -1 reads image as it is including alpha channel

# print(img)

cv2.imshow('image', img)
cv2.waitKey(0)  # 0 means infinite time and any value means that amount of time in milliseconds
cv2.destroyAllWindows()
