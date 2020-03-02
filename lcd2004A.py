#!/usr/bin/env python
"""first please add python library via this command: python -m easy_install --user https://github.com/pl31/python-liquidcrystal_i2c/archive/master.zip """
import sys
import time
import liquidcrystal_i2c
import commands
lcd = liquidcrystal_i2c.LiquidCrystal_I2C(0x27, 1, numlines=4)
try:
    while True:
        pstr= 'HOST_NAME:'+ str(commands.getoutput('hostname'))
        lcd.printline(0,pstr)
        pstr = 'IP_ADDR:'+ str(commands.getoutput('hostname -I'))
        lcd.printline(1,pstr)
        pstr = 'MEM_LOAD:' + str(commands.getoutput("free -m |grep Mem | awk \'{print $NF}\'"))+ 'MB'
        lcd.printline(2,pstr)
        pstr = 'CPU_TEMP:' + str(commands.getoutput('vcgencmd measure_temp'))
        lcd.printline(3,pstr)
        time.sleep(1)
except KeyboardInterrupt:
    pstr= 'Good Bye, My Dear!!!'
    for i in range(0,4):
        lcd.printline(i,pstr)
    os.exit()

