#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time
import sys
from sys import platform

arg_1 = int(sys.argv[1])  # adres modbus start
arg_2 = int(sys.argv[2])  # adres modbus stop
arg_3 = int(sys.argv[3])  # predkosc polaczenia
arg_4 = int(sys.argv[4])  # adres rejestru start
arg_5 = int(sys.argv[5])  # ilosc rejestrow


def adresCheck(unit_start=arg_1, unit_stop=arg_2, speed=arg_3, add_start=arg_4 - 1, len=arg_5):
    unit_range = (unit_start, unit_stop)
    if platform == "linux" or platform == "linux2":
        port = '/dev/ttyUSB0'
    elif platform == "darwin":
        port = '/dev/ttyUSB0'
    elif platform == "win32":
        port = 'com5'
    print('Sprawdzenie adresow z zakresu: {}, dla predkosci: {}, Rejestry od: {} do: {}, Port: {} \n'.format(unit_range,
                                                                                                             speed,
                                                                                                             add_start + 1,
                                                                                                             add_start + len,
                                                                                                             port))

    count = 0
    client = True
    add_error = []
    while client:

        print('Polaczenie: ', count)
        for i in range(unit_range[0],unit_range[1]+1):
            try:
                unit = i
                client = ModbusClient(method='rtu', port=port, baudrate=speed, stopbits=1, parity='N', bytesize=8,
                                      timeout=3)
                connection = client.connect()
                massure = client.read_holding_registers(add_start, len, unit=i)
                print("Wartosci dla adresu {} : {}".format(i, massure.registers[0:]))
                client.close()
                time.sleep(1)
            except AttributeError:
                add_error.append(unit)
                print('Błąd połaczenia z adresem: {} {}'.format(unit,add_error))
                client.close()
                time.sleep(1)
                continue

        time.sleep(1)
        count += 1
        print('\n')

if __name__ == "__main__":
    adresCheck()
