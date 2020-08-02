import numpy as np
import cv2


# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flags, params):
    # if left click pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ",", y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        # getting X,Y coords
        strXY = str(x) + ", " + str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 255), 2)
        cv2.imshow("image", img)
    # if right click pressed
    if event == cv2.EVENT_RBUTTONDOWN:
        # getting BRG values
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ", " + str(green) + ", " + str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (255, 255, 255), 2)
        cv2.imshow("image", img)


def click_event2(event, x, y, flags, params):
    # if left click pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        # create a small circle
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x, y))
        # if more than two points exist than create a line
        if len(points) >= 2:
            # Create lines that join together
            cv2.line(img, points[-1], points[-2], (255, 255, 0), 5, cv2.LINE_AA)

            # Create lines that are separate
            # cv2.line(img, points[0], points[1], (255, 255, 0), 5, cv2.LINE_AA)
            # points.clear()
        cv2.imshow('image', img)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread("lena_Copy.png")
cv2.imshow('image', img)
points = []

cv2.setMouseCallback('image', click_event2)
cv2.waitKey()
cv2.destroyAllWindows()



