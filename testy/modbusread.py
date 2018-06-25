#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time
import sys

arg_1 = int(sys.argv[1])  # adres modbus start
arg_2 = int(sys.argv[2])  # adres modbus stop
arg_3 = int(sys.argv[3])  # predkosc polaczenia
arg_4 = int(sys.argv[4])  # adres rejestru start
arg_5 = int(sys.argv[5])  # ilosc rejestrow


def adresCheck(unit_start=arg_1, unit_stop=arg_2, speed=arg_3, add_start=arg_4 - 1, len=arg_5):
    unit_range = (unit_start, unit_stop)
    print('Sprawdzenie adresow z zakresu {}, dla predkosci {}, Rejestry od {} do {} \n'.format(unit_range,
                                                                                               speed,
                                                                                               add_start+1,
                                                                                               add_start + len))

    count = 0
    client = True
    try:
        while client:

            client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=speed, stopbits=1, parity='N', bytesize=8,
                                  timeout=3)

            try:
                connection = client.connect()
                print('Polaczenie: ', count, connection)
                for i in unit_range:
                    massure = client.read_holding_registers(add_start, len, unit=i)
                    print("Wartosci dla adresu {} : {}".format(i, massure.registers[0:]))
                    time.sleep(1)
                count += 1
                client.close()
                print('\n')

            except AttributeError:
                print('Adres jest inny, lub jest inny błąd w adresacji ')
    except  KeyboardInterrupt:
        print('\nPrzerwanie przez uzytkownika')
        client.close()


if __name__ == "__main__":
    adresCheck()
