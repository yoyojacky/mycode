#!/usr/bin/env python
"""first please add python libarary via this command: python -m easy_install --user https://github.com/pl31/python-liquidcrystal_i2c/archive/master.zip """
import socket
import os.path
import sys
import struct
import fcntl
import os
import time
import liquidcrystal_i2c

lcd = liquidcrystal_i2c.LiquidCrystal_I2C(0x27, 1, numlines=4)

while True:
    try:
        pstr = 'IP:'+ str(os.popen('hostname -I').read()).strip('\n')
        lcd.printline(0,pstr)
        pstr = 'MEM:'+ str(os.popen('free -m|grep Mem |awk \'{print $NF}\'').read().strip('\n'))
        lcd.printline(1,pstr) 
        pstr = 'TEMP:'+ str(float(open('/sys/class/thermal/thermal_zone0/temp').read()) /1000.0)+'C'
        lcd.printline(2,pstr)
        pstr ='Ld:'+str(os.popen('uptime |cut -d \',\' -f3-6 |cut -d : -f2 ').read().strip('\n'))
        lcd.printline(3,pstr)   
        time.sleep(0.2)
    except KeyboardInterrupt as e:
        print("quit from the loop!")
        break


