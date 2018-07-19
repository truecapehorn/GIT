#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from collections import OrderedDict
import time
import sys
from sys import platform
from modbus_def import port
from time import clock


class Api():
    ''' Klasy do obsłogi Modbus RTU'''

    def __init__(self, method='rtu', port='com2', baudrate=9600, stopbits=2, parity='N', bytesize=8, timeout=5):
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

    def read_holding(self,reg_start, reg_lenght, mod_adress):





        try:
            client = ModbusClient(method='rtu', port=com, baudrate=2400, stopbits=1, parity='N', bytesize=8, timeout=3)
            connection = client.connect()
            time.sleep(0.3)
            massure = client.read_holding_registers(reg_start - 1, reg_lenght, unit=mod_adress)
            print('Rejestry :', massure.registers[0:])
            # print(connection)
            client.close()
            return connection, massure.registers
        except AttributeError:
            print('Połaczenie z adresem {} nie udane'.format(mod_adress))