#!/usr/bin/env python
"""first please add python libarary via this command: python -m easy_install --user https://github.com/pl31/python-liquidcrystal_i2c/archive/master.zip """
import time
import liquidcrystal_i2c

try:
    while True:
	try:
		lcd = liquidcrystal_i2c.LiquidCrystal_I2C(0x27, 1, numlines=4)
		print("Detect 1 LCD2004 Device on 0x27....")
		pstr= '00000000000000000000'       
		lcd.printline(0,pstr) 
		lcd.printline(1,pstr)
		lcd.printline(2,pstr) 
		lcd.printline(3,pstr)   
		time.sleep(5)
		
	except IOError as e:
		print("The fucking device is missing...")
except KeyboardInterrupt:
	print("Fuck that shit!!")


