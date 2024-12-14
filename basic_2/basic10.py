
#* อ่านรูป
import cv2

img = cv2.imread('img/cat1.jpg')

#* กำหนดขนาด
imgresize = cv2.resize(img, (640,480))

#* วาดเส้ยตรงในรูป
cv2.arrowedLine(imgresize, (0,0), (500,350), (255,255,0), 5)

cv2.imshow('Output', imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()
