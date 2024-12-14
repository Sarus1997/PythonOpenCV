# show image
import cv2

img = cv2.imread('img/cat1.jpg')

cv2.imshow('Output', img)
cv2.waitKey(delay=2000) # ไม่ต้องการให้ปิดอัตตโนมัติ ใส่ค่าเป็น 0
cv2.destroyAllWindows()
