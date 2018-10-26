#!/usr/bin/env python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO 
import time 

INT1 = 18
INT2 = 27
INT3 = 22 
INT4 = 23 

Pin_list = [ INT1, INT2, INT3, INT4]
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for Pin in Pin_list:
    GPIO.setup(Pin,GPIO.OUT)
    GPIO.output(Pin,GPIO.LOW)

def stopcar():
    for Pin in Pin_list:
        GPIO.output(Pin, GPIO.LOW)

def forward(second):
    GPIO.output(Pin_list[0], GPIO.HIGH)
    GPIO.output(Pin_list[3], GPIO.HIGH)
    GPIO.output(Pin_list[1], GPIO.LOW)
    GPIO.output(Pin_list[2], GPIO.LOW)
    time.sleep(second)
    stopcar()


def backward(second):
    GPIO.output(Pin_list[0], GPIO.LOW)
    GPIO.output(Pin_list[3], GPIO.LOW)
    GPIO.output(Pin_list[1], GPIO.HIGH)
    GPIO.output(Pin_list[2], GPIO.HIGH)
    time.sleep(second)
    stopcar()

def turnleft(second):
    GPIO.output(Pin_list[0], GPIO.HIGH)
    GPIO.output(Pin_list[3], GPIO.LOW)
    GPIO.output(Pin_list[1], GPIO.LOW)
    GPIO.output(Pin_list[2], GPIO.LOW)
    time.sleep(second)
    stopcar()

def turnright(second):
    GPIO.output(Pin_list[0], GPIO.LOW)
    GPIO.output(Pin_list[3], GPIO.HIGH)
    GPIO.output(Pin_list[1], GPIO.LOW)
    GPIO.output(Pin_list[2], GPIO.LOW)
    time.sleep(second)
    stopcar()

def turnaround(second):
    GPIO.output(Pin_list[0], GPIO.HIGH)
    GPIO.output(Pin_list[3], GPIO.LOW)
    GPIO.output(Pin_list[1], GPIO.LOW)
    GPIO.output(Pin_list[2], GPIO.HIGH)
    time.sleep(second)
    stopcar()

try:
    print(u'前进')
    forward(1)
    time.sleep(1)
    stopcar()
    print(u'后退')
    backward(1)
    time.sleep(1)
    stopcar()
    print(u'左转')
    turnleft(1)
    time.sleep(1)
    stopcar()
    print(u'右转')
    turnright(1)
    time.sleep(1)
    stopcar()
    print(u'原地打转')
    turnaround(1)
    time.sleep(1)
    stopcar()
except KeyBoardInterrupt as e:
    print "stop the program"
    GPIO.cleanup()
