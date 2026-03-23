import cv2
import numpy as np
import os
import RPi.GPIO as GPIO
import time

# --- 1. GPIO 및 서보 모터 설정 ---
SERVO_PIN = 18          # PWM 신호 핀 (BCM 18번)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

pwm = GPIO.PWM(SERVO_PIN, 50)  # 50Hz 설정
pwm.start(0)            # 초기 신호 0

def open_door():
    """서보 모터를 움직여 문을 열고 2초 뒤 닫는 함수"""
    print("[INFO] Door Opening...")
    pwm.ChangeDutyCycle(7.5)  # 90도 이동 (열림)
    time.sleep(2)             # 2초 유지
    pwm.ChangeDutyCycle(2.5)  # 0도 이동 (닫힘)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(0)    # 서보 모터 떨림 방지를 위해 신호 차단

# --- 2. 얼굴 인식 설정 ---
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')  # 학습된 모델 로드
cascadePath = "/eternal/facedoorrock/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

# ID별 이름 매핑 (ID 1은 Marcelo, 2는 Paula 등)
names = ['None', 'Marcelo', 'Paula', 'Ilza', 'Z', 'W'] 

# 카메라 시작
cam = cv2.VideoCapture(0)
cam.set(3, 640) # 너비
cam.set(4, 480) # 높이

# 인식 최소 창 크기 설정
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

# 무분별한 사진 저장 방지를 위한 변수
last_saved_time = 0 

print("\n [INFO] System Started. Press 'ESC' to exit.")

while True:
    ret, img = cam.read()
    img = cv2.flip(img, -1) # 상하 반전 (필요 시 수정)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
    )

    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        id_num, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        # --- 로직 수행 부분 ---
        # confidence가 낮을수록 정확도가 높음 (100 - confidence가 높을수록 일치)
        match_rate = round(100 - confidence)

        if (confidence < 100):
            name_id = names[id_num]
            conf_label = f"  {match_rate}%"
            
            # 일치율이 45% 이상일 때만 실제로 문을 엶 (수치 조정 가능)
            if match_rate > 45:
                open_door()
        else:
            name_id = "unknown"
            conf_label = f"  {match_rate}%"
            
            # 모르는 사람일 경우 5초 간격으로 사진 저장
            current_time = time.time()
            if current_time - last_saved_time > 5:
                file_name = f"intruder_{int(current_time)}.jpg"
                cv2.imwrite(file_name, img)
                print(f"[WARN] Unknown face detected! Saved as {file_name}")
                last_saved_time = current_time
        
        cv2.putText(img, str(name_id), (x+5, y-5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(conf_label), (x+5, y+h-5), font, 1, (255, 255, 0), 1)  
    
    cv2.imshow('camera', img) 
    
    k = cv2.waitKey(10) & 0xff
    if k == 27: # ESC 키를 누르면 종료
        break

# --- 3. 정리 ---
print("\n [INFO] Exiting Program and cleaning up")
cam.release()
cv2.destroyAllWindows()
pwm.stop()
GPIO.cleanup()
