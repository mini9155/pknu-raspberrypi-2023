import RPi.GPIO as GPIO
import time

signal_pin = 18

# GPIO.setmode(GPIO.BOARD) # 1~40
GPIO.setmode(GPIO.BCM) # GPIO 18, GROUND
GPIO.setup(signal_pin, GPIO.OUT) # GPIO18핀에다가 출력을 설정

while (True):
    GPIO.output(signal_pin, True) # GPIO 18번 핀에 전압 시그널 온
    time.sleep(0.02)
    GPIO.output(signal_pin, False) # GPIO 18번 핀에 전압 시그널 오프
    time.sleep(0.02) # 1초 동안 불 끈 상태로 대기dmstj 