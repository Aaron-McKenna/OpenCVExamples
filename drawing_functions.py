import numpy as np
import cv2

# Read image in the colour. 0 = grayscale
# img = cv2.imread('lena.jpg', 1)
# Draw image using Numpy
img = np.zeros([512, 512, 3], np.uint8)


# Add Line
img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 5)
# Add Arrowed Line
img = cv2.arrowedLine(img, (0, 310), (255, 280), (200, 70, 40), 5)
# Add Rectangle
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 4)
# Add circle
img = cv2.circle(img, (447, 63), 63, (50, 200, 5), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
# Add Text to image
img = cv2.putText(img, "OpenCV", (10, 500), font, 4, (255, 255, 255), 8)

cv2.imshow('image', img)

cv2.waitKey()
cv2.destroyAllWindows()
