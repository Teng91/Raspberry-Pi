import RPi.GPIO as GPIO
import time
import cv2
cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
i = 7 #center of ChangeDutyCycle
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo = GPIO.PWM(11,50)
servo.start(i) #restart servo

while cap.isOpened():
    start = time.time()
    ret, img = cap.read()
    img = cv2.flip(img, 0) #設定影像上下互換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #轉換成灰階
    faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10) #辨識影像
    if faces==():
        servo.ChangeDutyCycle(0) 
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2) #加上綠框
        center = x + w*0.5 #x-axis center position
        #print(center)
        if center >= 170: #x-axis +10
            i += 0.05 #turn left
            servo.ChangeDutyCycle(i)
            #time.sleep(0.1) #time delay
            #print(i)
        if center < 150: #x-axis -10
            i -= 0.05 #turn right
            servo.ChangeDutyCycle(i)
            #time.sleep(0.1) #time delay
            #print(i)
    end = time.time()
    
    #fps
    print("Found {0} faces!, fps= {1}".format(len(faces), round(1/(end - start))))
    cv2.imshow("view",img)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break #按q跳出迴圈
    
cap.release()
cv2.destroyAllWindows()
GPIO.cleanup()