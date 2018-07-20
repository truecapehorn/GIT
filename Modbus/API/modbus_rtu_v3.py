#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from collections import OrderedDict
import time
import numpy as np


class Api():
    ''' Obsłoga Modbus RTU'''

    def __init__(self, method='rtu', port='com3', speed=9600, stopbits=2, parity='N', bytesize=8, timeout=1):
        self.method = method
        self.port = port
        self.speed = speed
        self.stopbits = stopbits
        self.parity = parity
        self.bytesize = bytesize
        self.timeout = timeout

    def connection(self):
        client = ModbusClient(method=self.method, port=self.port, baudrate=self.speed, stopbits=self.stopbits,
                              parity=self.parity, bytesize=self.bytesize, timeout=self.timeout)

        print(
            "Odczyt\nmethod = {},\nport = {},\nbaudrate = {},\nstopbits = {},\nparity = {},\nbytesize = {},\ntimeout = {},\n".format(
                self.method,
                self.port,
                self.speed,
                self.stopbits,
                self.parity,
                self.bytesize,
                self.timeout))

        time.sleep(1)
        return client

    def read_holding(self, unit, reg_start, reg_lenght, data_type, qty=5):
        client = self.connection()
        connection = client.connect()
        print("Odczyt adresow holding reg od {} do {} dla urzadzen {} : {}".format(reg_start,
                                                                                   reg_start + reg_lenght,
                                                                                   unit,
                                                                                   connection))
        sesion = 1
        while connection and sesion <= qty:
            print("Sesja nr: ", sesion)
            time.sleep(0.3)
            for i in unit:
                try:
                    client.connect()
                    massure = client.read_holding_registers(reg_start, reg_lenght, unit=i)
                    if data_type == 'ui16':
                        print('Rejestry {} dla adresu {}: {}'.format(data_type,i, massure.registers[0:]))
                    elif data_type == 'float':
                        massure.registers[0::2], massure.registers[1::2] = massure.registers[1::2], massure.registers[
                                                                                                    0::2]
                        data = np.array([massure.registers[0:]], dtype=np.int16)
                        data_as_float = data.view(dtype=np.float32)
                        print('Rejestry {} dla adresu {}: {}'.format(data_type,i, data_as_float.tolist()))
                    client.close()
                except AttributeError:
                    print('Połaczenie z adresem {} nie udane'.format(i))
                    continue
                except KeyboardInterrupt:
                    print('Przerwanie przez urzytkownika')
                    client.close()
                    break

            sesion += 1
            print("\n")

    def read_input(self, unit, reg_start, reg_lenght, data_type, qty=5):
        client = self.connection()
        connection = client.connect()
        if data_type=='float':
            reg_lenght+=2
        print("Odczyt adresow input reg od {} do {} dla urzadzen {} : {}".format(reg_start,
                                                                                    (reg_start + reg_lenght),
                                                                                    unit,
                                                                                    connection))
        sesion = 1
        while connection and sesion <= qty:
            print("Sesja nr: ", sesion)
            time.sleep(0.3)
            massure=[]
            for i in unit:
                try:
                    client.connect()
                    massure = client.read_input_registers(reg_start, reg_lenght, unit=i)

                    if data_type == 'ui16':
                        print('Rejestry {} dla adresu {}: {}'.format(data_type,i, massure.registers[0:]))
                    elif data_type == 'float':
                        massure.registers[0::2], massure.registers[1::2] = massure.registers[1::2], massure.registers[
                                                                                                    0::2]
                        data = np.array([massure.registers[0:]], dtype=np.int16)
                        data_as_float = data.view(dtype=np.float32)
                        print('Rejestry {} dla adresu {}: {}'.format(data_type,i, data_as_float.tolist()))
                    client.close()
                except AttributeError:
                    print('Połaczenie z adresem {} nie udane'.format(i))
                    continue
                except KeyboardInterrupt:
                    print('Przerwanie przez urzytkownika')
                    client.close()
                    break

            sesion += 1
            print("\n")



if __name__ == '__main__':
    rtu = Api()
    fifek=Api(speed=2400)
    print(Api.__doc__)
    unith = [3,5,7,9,10]
    uniti = [64]
    fif=[1]
    readholding = rtu.read_holding(unith, 0, 10, 'ui16', 1)
    readinput1 = rtu.read_input(uniti, 0, 10, 'ui16', 5)
    readinput2 = fifek.read_input(fif, 0, 70, 'float', 5)
