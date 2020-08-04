import numpy as np
import cv2


def click_event(event, x, y, flags, params):
    # if left click pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ",", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        # getting X,Y coords
        strXY = str(x) + ", " + str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (0, 0, 0), 2)
        cv2.imshow("image", img)


img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
# X1 = 330
# Y1 = 280

# X2 = 390
# Y2 = 340
ball = img[280:340, 330:390]
# X1 = 100
# Y1 = 273

# X2 = 160
# Y2 = 333
img[273:333, 100:160] = ball

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, .9, img2, .1, 0)

cv2.imshow('image', dst)

cv2.setMouseCallback('image', click_event)
cv2.waitKey()
cv2.destroyAllWindows()
