import I2C_LCD_driver
from time import * 

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("DockerPi Series", 1, 0)
mylcd.lcd_display_string("52Pi.com", 2, 0)

