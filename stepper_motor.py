# stepper motor testing code
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ControlPin = [7, 11, 13, 15]

for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

seq = [ [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1] ]

## 1 revolution = 8 cycles
## gear reduction = 1/64 
## 8x64 = 512 cycles
try:
    while True:
        for i in range(512):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(ControlPin[pin], seq[halfstep][pin])
                    print("halfstep is: %d, pin is %d"%(halfstep, pin))
                time.sleep(0.001)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    print("Bye bye!")

