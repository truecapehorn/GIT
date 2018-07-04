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
        port = 'com2'
        print('windows')
    return port



def port_v2():
    port='non'
    ktoryPort = input('Jaki Port chesz wybrać\n1: dev/ttyUSB0\n2: com2\n3: com3\n4: com4\n5: com5\n')
    if ktoryPort =='1':
        port = '/dev/ttyUSB0'
    elif ktoryPort=='2':
        port = 'com2'
    elif ktoryPort=='3':
        port = 'com3'
    elif ktoryPort=='4':
        port = 'com4'
    elif ktoryPort=='5':
        port = 'com5'
    print(port)
    return port







if __name__ == '__main__':

    port_v2()




