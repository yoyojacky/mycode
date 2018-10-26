#!/usr/bin/env python
# -*- coding:utf-8 -*-

import serial
import time as t


s = serial.Serial("/dev/ttyUSB0", 9600)
try:
    while True:
        dataframe = []
        data = s.readline()
        data = data.lstrip('$')
        if data[0:5] == 'GPRMC':
            dataframe.append(data.strip('\r\n').split(','))
            print dataframe[0]
        
            if dataframe[0][2] == 'V':
                print(data)
                print('狗日的GPS寻星失败!')
            else:
                print('终于寻星成功！')

except KeyboardInterrupt:
    print('bye')

#    t.sleep(1) 

