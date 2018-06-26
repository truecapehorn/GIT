from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time
import sys
import sys
from sys import platform


def port():
    if platform == "linux" or platform == "linux2":
        port = '/dev/ttyUSB0'
        print('linux')
    elif platform == "darwin":
        port = '/dev/ttyUSB0'
        print('dariwn')
    elif platform == "win32":
        port = 'com3'
        print('windows')
    return port




