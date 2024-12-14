# resize image
import cv2

img = cv2.imread('img/cat1.jpg', -1)
img = cv2.resize(img, (640,480))

cv2.imshow('Output', img)
cv2.waitKey(delay=3000)
cv2.destroyAllWindows()
