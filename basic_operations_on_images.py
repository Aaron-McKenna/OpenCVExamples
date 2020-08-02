import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
# returns a tuple of number of rows, columns, and channels
print(img.shape)
# returns Total number of pixels in accessed
print(img.size)
# returns Image datatype is obtained
print(img.dtype)
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
