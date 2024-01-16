import cv2

img1 = cv2.imread("Images/img.png", 1)
img2 = cv2.imread("Images/Tom_Jerry.jpg", 1)

cv2.imshow("Original Image 1", img1)
cv2.imshow("Original Image 2", img2)
cv2.waitKey(0)

# Resize both images to the same dimensions
rows, cols, _ = img1.shape
img2 = cv2.resize(img2, (cols, rows))

# Set weight for both images (in this case, both images have the same weight)
alpha = 0.5
beta = 0.5

# Weighted addition of both images
new_img = cv2.addWeighted(img1, alpha, img2, beta, 0)#addWeighted(img1,weight1,img2,weight2,gamma), gamma is the scalar added to each sum

cv2.imshow("Average Image", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
