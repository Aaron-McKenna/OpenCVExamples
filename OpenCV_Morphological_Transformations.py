import cv2
import numpy as np
import matplotlib.pyplot as plt

# "Morphological transformations are simple operations based on the image shape"
# Normally performed on binary images
# 2 elements required, original images and a structuring element / Kernel

img = cv2.imread('smarties.png', 0)

_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# 2 x 2 square
kernal = np.ones((2, 2), np.uint8)

dilation = cv2.dilate(mask, kernal, iterations=3)

erosion = cv2.erode(mask, kernal, iterations=3)

# Opening = erosion then dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

# Closing = dilation then erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)


titles = ['Image', 'Mask', 'Dilation', 'Erode', 'Opening', 'Closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])


plt.show()
