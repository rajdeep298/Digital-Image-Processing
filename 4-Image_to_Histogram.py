import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("Images/img.png", 0)

cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

dst = cv2.calcHist(img, [0], None, [256], [0,256])
plt.hist(img.ravel(),256,[0,256])
#or
#plt.plot(dst)
plt.title('Histogram for gray scale image')
plt.show()