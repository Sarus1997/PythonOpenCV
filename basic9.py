
#* เปิด กล้อง และ บันทึกวิดีโอ

import cv2

cap = cv2.VideoCapture("video/newyork.mp4")

while (cap.isOpened()):
    check , frame = cap.read() #* รับภาพต่อเนื่องจากกล้อง frame ต่อ frame 
    
    if check == True:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS_FULL)
        
        cv2.imshow("Output" , frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): #* เช็กการกดปุัม เมื่อกดปุ่มนั้นๆ จะปิด
            break        
    else:
        break #* เมื่อวิดีโอจบ จะปิดอัตโนมัติ

cap.release()
cv2.destroyAllWindows()