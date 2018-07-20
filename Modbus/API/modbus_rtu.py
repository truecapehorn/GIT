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
            "Odczyt\nmethod = {},\nport = {},\nbaudrate = {},\nstopbits = {},\nparity = {},\nbytesize = {},\ntimeout = {}\n".format(
                self.method,
                self.port,
                self.speed,
                self.stopbits,
                self.parity,
                self.bytesize,
                self.timeout))

        time.sleep(1)
        return client

    def read_holding(self, unit_start, unit_stop, reg_start, reg_lenght, qty):
        client = self.connection()
        connection = client.connect()
        print("Odczyt adresow holding reg od {} do {} dla urzadzen od {} do {}: {}".format(unit_start, unit_stop,
                                                                                           reg_start,
                                                                                           reg_start + reg_lenght,
                                                                                           connection))
        sesion = 1
        while connection and sesion <= qty:
            print("Sesja nr: ", sesion)
            time.sleep(0.3)
            for i in range(unit_start, unit_stop + 1):
                try:

                    massure = client.read_holding_registers(reg_start, reg_lenght, unit=i)
                    print('Rejestry dla adresu {}: {}'.format(i, massure.registers[0:]))
                except AttributeError:
                    print('Połaczenie z adresem {} nie udane'.format(i))
                    continue
                except KeyboardInterrupt:
                    print('Przerwanie przez urzytkownika')
                    client.close()
                    break

            sesion += 1
            print("\n")

    def read_input(self, unit_start, unit_stop, reg_start, reg_lenght, qty):
        client = self.connection()
        connection = client.connect()
        print("Odczyt adresow input reg od {} do {} dla urzadzen od {} do {}: {}".format(reg_start,
                                                                                         2*(reg_start + reg_lenght),
                                                                                         unit_start,
                                                                                         unit_stop,
                                                                                         connection))
        sesion = 1
        while connection and sesion <= qty:
            print("Sesja nr: ", sesion)
            time.sleep(0.3)
            for i in range(unit_start, unit_stop + 1):
                res=[]
                dec=[]
                start=reg_start
                c=0
                try:


                    for a in range(1,reg_lenght+1):
                        result = client.read_input_registers(start+c, 2, unit=i)
                        res.append(result.registers)
                        c+=2


                    for d in res:
                        #decoder = BinaryPayloadDecoder.fromRegisters(d, byteorder=Endian.Big, wordorder=Endian.Little)
                        decoder = BinaryPayloadDecoder.fromRegisters(d, byteorder=Endian.Little, wordorder=Endian.Big)
                        massure = (decoder.decode_32bit_float())
                        dec.append(massure)
                    print('Rejestry dla adresu {}: {}'.format(i, dec))
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
    print(Api.__doc__)

    #readholding = rtu.read_holding(1, 32, 0, 10,3)
    readinput=rtu.read_input(63,64,0,5,6)

