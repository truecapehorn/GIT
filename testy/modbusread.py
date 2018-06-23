#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time
import sys

first_arg = int(sys.argv[1])
sec_arg = int(sys.argv[2])
third_arg = int(sys.argv[3])


def adresCheck(add1=first_arg, add2=sec_arg, speed=third_arg):
    unit_range = (add1, add2)
    print('Sprawdzenie adresow z zakresu :', unit_range, 'Predkosc', speed, '\n')
    count = 0
    # unit_dymision = list(range(1, 3))
    # print(unit_dymision)

    client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=speed, stopbits=1, parity='N', bytesize=8,
                          timeout=3)

    try:
        while True:
            connection = client.connect()
            print('Polaczenie: ', count, connection)
            for i in unit_range:
                massure = client.read_holding_registers(6, 4, unit=i)
                print("Wartosci dla adresu {} : {}".format(i, massure.registers[0:]))
                time.sleep(1)
            count += 1
            client.close()

    except AttributeError:
        print('Adres jest inny niż {} , lub jest inny błąd w adresacji '.format(unitOld))

    client.close()


if __name__ == "__main__":
    adresCheck()
