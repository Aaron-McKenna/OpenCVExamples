import cv2

img = cv2.imread('lena.jpg', 1)

print(img)

cv2.imshow('image', img)

k = cv2.waitKey()
# k key number is 27
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_Copy.png', img)
    cv2.destroyAllWindows()

