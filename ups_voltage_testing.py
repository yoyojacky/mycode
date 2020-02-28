# execute this command if you don't have pi-ina219 liberary.
# sudo pip3 install pi-ina219
from ina219 import INA219
from ina219 import DeviceRangeError
import time as t 
import subprocess

SHUNT_OHMS = 0.05
ina = INA219(SHUNT_OHMS)
ina.configure()

def read():
    ina = INA219(SHUNT_OHMS)
    ina.configure()
    print("Bus Voltage: %.3f V" % ina.voltage())

    try:
        print("Bus Current: %.3f mA" % ina.current())
        print("Power: %.3f mW" % ina.power())
        print("Shunt voltage: %.3f mV" % ina.shunt_voltage())

    except DeviceRangeError as e:
        print(e)

if __name__== "__main__":
    try:
        while True:
            read()
            print(subprocess.getoutput('date +"%F %T.%s%::z" ; sudo hwclock'))
            t.sleep(5)
            print('-' * 40)
    except KeyboardInterrupt:
        print("Quit!!!")

