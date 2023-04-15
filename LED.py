import RPi.GPIO as GPIO
import time
import random

#LED_B = 24
#LED_G = 23
LED_R = 18

# GPIO 핀 모드 설정
GPIO.setmode(GPIO.BCM)
#GPIO.setup(LED_B, GPIO.OUT)
#GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_R, GPIO.OUT)

# LED 모듈 색상 설정
#BLUE = GPIO.PWM(LED_B, 1000)
#GREEN = GPIO.PWM(LED_G, 1000)
RED = GPIO.PWM(LED_R, 1000)

# LED 모듈 초기 상태 설정
#BLUE.start(0)
#GREEN.start(0)
RED.start(0)

try:
    while True:
        predicted_distance = random.uniform(3.0, 7.0)
        if predicted_distance >= 3 and predicted_distance < 4.5:
            for i in range(50):
                RED.ChangeDutyCycle(100)  # LED 밝기 100%
                time.sleep(0.1)  # 0.1초 대기
                RED.ChangeDutyCycle(0)  # LED 끄기
                time.sleep(0.1)  # 0.1초 대기
        elif predicted_distance >= 4.5 and predicted_distance < 5.5:
            for i in range(25):
                RED.ChangeDutyCycle(100)  # LED 밝기 100%
                time.sleep(0.2)  # 0.2초 대기
                RED.ChangeDutyCycle(0)  # LED 끄기
                time.sleep(0.2)  # 0.2초 대기
        elif predicted_distance >= 5.5 and predicted_distance <= 7:
            for i in range(12):
                RED.ChangeDutyCycle(100)  # LED 밝기 100%
                time.sleep(0.5)  # 0.5초 대기
                RED.ChangeDutyCycle(0)  # LED 끄기
                time.sleep(0.5)  # 0.5초 대기
        else:
            #BLUE.ChangeDutyCycle(0)
            #GREEN.ChangeDutyCycle(0)
            RED.ChangeDutyCycle(0)

        time.sleep(10) # 10초 주기로 예측 거리를 업데이트함

except KeyboardInterrupt:
    #BLUE.stop()
    #GREEN.stop()
    RED.stop()
    GPIO.cleanup()
