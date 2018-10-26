#!/usr/bin/env python
# coding:utf-8
import time as t
import serial 

right = u'youshou'
left = u'zuoshou'
rightleg = u'youjiao'
leftleg = u'zuojiao'
eyes = u'yanjing'


if __name__=='__main__':
    ser = serial.Serial('/dev/ttyS0', baudrate=115200, timeout=1)
    ser.write('AT+TTS=123\r')
    ser.write('AT+ASRADD=qianjin,2\r')
    ser.write('AT+ASRLIST?\r')
    feedback = ser.readline()
    print feedback
