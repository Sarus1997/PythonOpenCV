
#* เปิด vedio

import cv2

cap = cv2.VideoCapture("video/newyork.mp4")

while (cap.isOpened()):
    check , frame = cap.read() #* รับภาพต่อเนื่องจากกล้อง frame ต่อ frame 
    
    if check == True:
        cv2.imshow("Output" , frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): #* เช็กการกดปุัม เมื่อกดปุ่มนั้นๆ จะปิด
            break        
    else:
        break

cap.release()
cv2.destroyAllWindows()