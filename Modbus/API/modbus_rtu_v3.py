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

    def __init__(self, method='rtu', port='com2', speed=9600, stopbits=2, parity='N', bytesize=8, timeout=1):
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
            "   Connection:\nmethod = {},\nport = {},\nbaudrate = {},\nstopbits = {},\nparity = {},\nbytesize = {},\ntimeout = {},\n".format(
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
                        data = massure.registers[0:]
                        print('Rejestry {} dla adresu {}: {}'.format(data_type, i, data))
                    elif data_type == 'float':
                        massure.registers[0::2], massure.registers[1::2] = massure.registers[1::2], massure.registers[
                                                                                                    0::2]
                        data_arr = np.array([massure.registers[0:]], dtype=np.int16)
                        data_as_float = data_arr.view(dtype=np.float32)
                        data = data_as_float
                        print('Rejestry {} dla adresu {}: {}'.format(data_type, i, data))
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
        return data

    def read_input(self, unit, reg_start, reg_lenght, data_type, qty=5):
        client = self.connection()
        connection = client.connect()
        if data_type == 'float':
            reg_lenght += 2
        print("Odczyt adresow input reg od {} do {} dla urzadzen {} : {}".format(reg_start,
                                                                                 (reg_start + reg_lenght),
                                                                                 unit,
                                                                                 connection))
        sesion = 1
        while connection and sesion <= qty:
            print("Sesja nr: ", sesion)
            time.sleep(0.3)
            massure = []
            for i in unit:
                try:
                    client.connect()
                    massure = client.read_input_registers(reg_start, reg_lenght, unit=i)

                    if data_type == 'ui16':
                        print('Rejestry {} dla adresu {}: {}'.format(data_type, i, massure.registers[0:]))
                    elif data_type == 'float':
                        massure.registers[0::2], massure.registers[1::2] = massure.registers[1::2], massure.registers[
                                                                                                    0::2]
                        data_arr = np.array([massure.registers[0:]], dtype=np.int16)
                        data_as_float = data_arr.view(dtype=np.float32)
                        print('Rejestry {} dla adresu {}: {}'.format(data_type, i, data_as_float.tolist()))
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

    def write_register(self, reg_add, val, mod_adress):
        try:
            client = self.connection()
            connection = client.connect()
            time.sleep(0.3)
            client.write_register(reg_add, val, unit=mod_adress)
            client.close()
        except AttributeError:
            print('Połaczenie z adresem {} nie udane'.format(mod_adress))
        return print('Nowa wartosc zapisana')

    def appar_add_change(self, unitOld, unitNew, data_type):
        unit = []
        unit.append(unitOld)
        print(unit)
        reg = self.read_holding(unit, 0, 30, data_type, 5)
        if reg != None:
            testVar = input("Czy chcesz zmienic adres z {} na {} ( t/n).".format(unitOld, unitNew))
            if testVar == "t" or testVar == 'T' and reg[1][28] == unitOld:
                print('Zmieniam adres z {} na {}'.format(unitOld, unitNew))
                self.write_register(28, unitNew, unitOld)
                time.sleep(0.5)
                unit = []
                print('Przeprowadzono zmiane adresu z {} na {}'.format(unitOld, unitNew))
                unit.append(unitNew)
                self.read_holding(unit, 0, 30, data_type, 5)
        print('\n')


if __name__ == '__main__':
    rtu = Api()
    fifek = Api(speed=2400)
    print(Api.__doc__)
    unith = [3]
    uniti = [64]
    fif = [1]
    readholding = rtu.read_holding(unith, 0, 10, 'ui16', 10)
    # readinput1 = rtu.read_input(uniti, 0, 10, 'ui16', 5)
    # readinput2 = fifek.read_input(fif, 0, 70, 'float', 5)
    #writereg = rtu.appar_add_change(1, 11, 'ui16')
