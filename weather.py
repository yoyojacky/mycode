#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2 
import ssl
import json
from gpiozero import MotionSensor
import time
import liquidcrystal_i2c

# instance pir module and lcd module.
pir = MotionSensor(4)
lcd = liquidcrystal_i2c.LiquidCrystal_I2C(0x27, 1, numlines=4)


def get_weather():
    """ access gaode API get weather"""
    report = []
    context = ssl._create_unverified_context()
    api = 'https://restapi.amap.com/v3/weather/weatherInfo?key=857e115ce98e9a5c5b93b0289715fe80&city=310000&extensions=base&output=JSON'
    response =  urllib2.urlopen(api, context=context)
    string = response.read()
    dc = json.loads(string)
    data = dc['lives'][0]
    #print(data)
    t = 'Temp: ' + data['temperature'] + 'C' 
    h = 'Humidity: ' + data['humidity'] + '%'
    report = data['reporttime']
    lcd.printline(0, report)
    lcd.printline(1, t)
    lcd.printline(2, h)

    
try:
    while pir.wait_for_motion():
        pir.wait_for_motion()
        lcd.printline(3,"Welcome back! Jacky!")
        pir.wait_for_no_motion()
        get_weather()
        lcd.printline(3,"Good bye! Jacky!")

except KeyboardInterrupt as e:
    print("you killed the program")
