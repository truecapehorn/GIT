#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from collections import OrderedDict
import time



class Api():
    ''' Klasy do obsłogi Modbus RTU'''

    def __init__(self, method='rtu', port='com2', baudrate=9600, stopbits=2, parity='N', bytesize=8, timeout=1):
        self.method = method
        self.port = port
        self.baudrate = baudrate
        self.stopbits = stopbits
        self.parity = parity
        self.bytesize = bytesize
        self.timeout = timeout

    def connection(self):
        client = ModbusClient(method=self.method, port=self.port, baudrate=self.baudrate, stopbits=self.stopbits,
                              parity=self.parity, bytesize=self.bytesize, timeout=self.timeout)

        return client

    def read_holding(self,reg_start, reg_lenght, unit_start, unit_stop):
        unit_range = (unit_start, unit_stop)

        while True:
            client = self.connection()
            connection = client.connect()

            time.sleep(0.3)
            for i in range(unit_range[0], unit_range[1] + 1):
                try:
                    massure = client.read_holding_registers(reg_start, reg_lenght, unit=i)
                    print('Rejestry dla adresu {}: {}'.format(i,massure.registers[0:]))
                    client.close()
                except AttributeError:
                    print('Połaczenie z adresem {} nie udane'.format(i))
                    continue
            print("\n")






if __name__ == '__main__':

    rtu = Api()
    print(Api.__doc__)

    readholding = rtu.read_holding(0,10,1,10)