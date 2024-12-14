
#* เปิด กล้อง และ บันทึกวิดีโอ

import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
result = cv2.VideoWriter("Output" , fourcc , 20.0 , (640,480))

while (cap.isOpened()):
    check , frame = cap.read() #* รับภาพต่อเนื่องจากกล้อง frame ต่อ frame 
    
    if check == True:
        ## x = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS_FULL)
        
        cv2.imshow("Output" , frame)
        result.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): #* เช็กการกดปุัม เมื่อกดปุ่มนั้นๆ จะปิด
            break        

result.release()
cap.release()
cv2.destroyAllWindows()