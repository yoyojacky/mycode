import RPi.GPIO as GPIO
import time

servoPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)

p = GPIO.PWM(servoPin, 50)
p.start(2.5)
dc = [2.5, 5, 7.5, 10, 12.5]
try:
    while True:
        for i in range(len(dc)): 
            p.ChangeDutyCycle(dc[i])
            time.sleep(0.1)
        for i in range(len(dc)): 
            p.ChangeDutyCycle(dc[-i])
            time.sleep(0.1)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
