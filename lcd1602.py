import I2C_LCD_driver
from time import * 

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("00000000000000000", 1, 0)
mylcd.lcd_display_string("00000000000000000", 2, 0)

