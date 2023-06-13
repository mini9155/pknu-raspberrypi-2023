import RPi.GPIO as GPIO
import time

button = 24
count = 0
red = 17
green = 22
blue = 27

# GPIO.setmode(GPIO.BCM)

# GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def clickHndler(channel):
    global count
    count = count + 1
    if (count % 2 == 0):
        GPIO.output(red, GPIO.LOW)
    else:
        GPIO.output(red, GPIO.HIGH)
    print(count)

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.add_event_detect(button, GPIO.RISING, callback=clickHndler)

while (True):
    time.sleep(1)