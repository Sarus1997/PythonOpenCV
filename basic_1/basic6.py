
#* เปิดกล้อง

import cv2

cap = cv2.VideoCapture(0)

while (True):
    ret , frame = cap.read() #* รับภาพต่อเนื่องจากกล้อง frame ต่อ frame 
    cv2.imshow("Output" , frame)
    
    #* เช็กการกดปุัม เมื่อกดปุ่มนั้นๆ จะปิด
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()