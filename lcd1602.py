# do remember download I2C_LCD_driver for your LCd1602
import I2C_LCD_driver
import time 

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("DockerPi Series", 1, 0)
mylcd.lcd_display_string("52Pi.com", 2, 0)
time.sleep(5)

mylcd.lcd_clear()
mylcd.lcd_display_string("LIQUID CRYSTAL", 1, 0)
mylcd.lcd_display_string("DISPLAY Over I2C", 2, 0)
time.sleep(5)

mylcd.lcd_clear()
mylcd.lcd_display_string("Piholder is good", 1, 0)
mylcd.lcd_display_string("Just checkit out", 2, 0)
time.sleep(5)

mylcd.lcd_clear()
mylcd.lcd_display_string("Hostname: RPi1", 1, 0)
mylcd.lcd_display_string("IP:192.168.1.1", 2, 0)
time.sleep(5)

mylcd.lcd_clear()
mylcd.lcd_display_string("CPU Load: 0.31", 1, 0)
mylcd.lcd_display_string("Mem: 3983MB", 2, 0)
time.sleep(5)

mylcd.lcd_clear()
while True:
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Time: %s" % time.strftime("%H:%M:%S"),1)
    mylcd.lcd_display_string("Date: %s" % time.strftime("%m:%d:%Y"),2)
    time.sleep(1)
    for i in range(0,50):
        if i==49:
            break

mystring = "This is ABS holder for Raspberry Pi and Arduino series products"
str_pad = " " * 16
mystring = str_pad + mystring
for i in range(0, len(mystring)):
    lcd_text = my_long_string[i:(i+16)]
    mylcd.lcd_display_string(lcd_text, 1)
    time.sleep(0.4)
    mylcd.lcd_display_string(str_pad, 1)





