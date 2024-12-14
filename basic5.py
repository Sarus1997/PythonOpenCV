# export image อ่านภาพสี ส่งออกเป็นภาพสีเทา
import cv2
import os

# Ensure the Save directory exists
os.makedirs('Save', exist_ok=True)

img = cv2.imread('img/cat1.jpg', 0)  #  0 = กำหนดค่าสี
img_resize = cv2.resize(img, (640,480))

cv2.imshow('Output', img_resize)

cv2.imwrite('save/cat2_esize.jpg', img_resize)

cv2.waitKey(delay=3000)
cv2.destroyAllWindows()
