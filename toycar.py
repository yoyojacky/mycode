import pygame
import sys
import smbus
import time

#MOTOR_DRIVER Address
MOTOR_DRIVER_ADDRESS = 0x18
MOTOR_DRIVER_BUS = 1
bus = smbus.SMBus(MOTOR_DRIVER_BUS)

#MOTOR_DRIVER Functions
MOTOR_DRIVER_SPEED_1_L = 0x01
MOTOR_DRIVER_SPEED_1_H = 0x02
MOTOR_DRIVER_SPEED_2_L = 0x03
MOTOR_DRIVER_SPEED_2_H = 0x04
MOTOR_DRIVER_COUNT_1_L = 0x05
MOTOR_DRIVER_COUNT_1_H = 0x06
MOTOR_DRIVER_COUNT_2_L = 0x07
MOTOR_DRIVER_COUNT_2_H = 0x08
MOTOR_DRIVER_DIRECTION = 0x09
MOTOR_DRIVER_SPEED_NOW_1_L = 0x0a
MOTOR_DRIVER_SPEED_NOW_1_H = 0x0b
MOTOR_DRIVER_SPEED_NOW_2_L = 0x0c
MOTOR_DRIVER_SPEED_NOW_2_H = 0x0d
MOTOR_DRIVER_COUNT_NOW_1_L = 0x0e
MOTOR_DRIVER_COUNT_NOW_1_H = 0x0f
MOTOR_DRIVER_COUNT_NOW_2_L = 0x10
MOTOR_DRIVER_COUNT_NOW_2_H = 0x11
MOTOR_DRIVER_DIRECTION_NOW = 0x12
MOTOR_DRIVER_ENABLE = 0x13
MOTOR_DRIVER_MODE = 0X14

MOTOR_DRIVER_PWM_NOW_2_L = 0x1f
MOTOR_DRIVER_PWM_NOW_2_H = 0x20

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('pygame event')
'''pygame.key.set_repeat(100, 500)'''
def setspeed():
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_SPEED_1_L,speed & 0xff)  
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_SPEED_1_H,speed >> 8)  
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_SPEED_2_L,speed & 0xff)  
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_SPEED_2_H,speed >> 8)  
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_ENABLE,100)
def decspeed():
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_SPEED_1_L,temp1 & 0xff)  
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_SPEED_1_H,temp1 >> 8)  
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_SPEED_2_L,temp1 & 0xff)  
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_SPEED_2_H,temp1 >> 8)    
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_ENABLE,100)
def turnleft():
    temp0 = 200
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_SPEED_1_L,temp0 & 0xff)  
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_SPEED_1_H,((temp0 >> 8) | 0x80))  
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_SPEED_2_L,(temp0 -100) & 0xff)  
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_SPEED_2_H,((temp0 -100) >> 8) | 0x80)    
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_ENABLE,100)
def turnright():
    temp0 = 200
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_SPEED_1_L,(temp0 - 100) & 0xff)  
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_SPEED_1_H,((temp0 - 100) >> 8) | 0x80)  
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_SPEED_2_L,temp0 & 0xff)  
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_SPEED_2_H,((temp0 >> 8) | 0x80))   
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_ENABLE,100)
def setdirection(sysnax):
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_DIRECTION,sysnax)
    bus.write_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_ENABLE,100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  
        list = [pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d]   
        keys_pressed = pygame.key.get_pressed()    
        if keys_pressed[list[1]]:
            print("S")
            speed = 200
            while (speed < 300):
                speed += 10
                setdirection(1)
                setspeed()
                if keys_pressed[list[3]]:
                    print("d")
                    turnleft()
                elif keys_pressed[list[2]]:
                    print("a")
                    turnright()
        
        elif keys_pressed[list[0]]:
            print("w")
            speed = 200
            while (speed < 350):
                speed += 10
                setdirection(2)
                setspeed()
                if keys_pressed[list[3]]:
                    print("d")
                    turnleft()
                elif keys_pressed[list[2]]:
                    print("a")
                    turnright()
        elif keys_pressed[list[3]]:
            print("d")
            turnleft()
            
        elif keys_pressed[list[2]]:
            print("a")
            turnright()         
        else:
            temp1 = (bus.read_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_PWM_NOW_2_H) << 8) | (bus.read_byte_data(MOTOR_DRIVER_ADDRESS,MOTOR_DRIVER_PWM_NOW_2_L))
            print(temp1)
            while (temp1 > 1):
                time.sleep(0.01)
                temp1 -= 1
                decspeed()
            else:
                temp1 = 0
                decspeed()
    pygame.display.update()   
            
