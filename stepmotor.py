# -*- coding:utf-8 -*-
'''
import RPi.GPIO as GPIO
import time 

INT1 = 1
INT2 = 2
INT3 = 3
INT4 = 4 
'''
import time
import pigpio
MOTOR_A1 = 2
MOTOR_A2 = 1 

#connect to pigpiod daemon
pi = pigpio.pi()

# pi set frequency
pi.set_PWM_frequency(MOTOR_A2, 100)

pi.set_servo_pulsewidth(MOTOR_A1, 0)
pi.set_PWM_dutycycle(MOTOR_A2,255)
time.sleep(1)

#disconnect
pi.stop()
