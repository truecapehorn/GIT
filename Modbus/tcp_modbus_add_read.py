#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.client.sync import ModbusTcpClient
import time
import sys
from sys import platform
from modbus_def import port

arg_1 = int(sys.argv[1])  # adres modbus start
arg_2 = int(sys.argv[2])  # adres modbus stop
arg_3 = str(sys.argv[3])  # adres tcp ip
arg_4 = int(sys.argv[4])  # adres rejestru start
arg_5 = int(sys.argv[5])  # ilosc rejestrow





def adresCheck(unit_start=arg_1, unit_stop=arg_2, address=arg_3, add_start=arg_4 - 1, len=arg_5):
    unit_range = (unit_start, unit_stop)
    com=port()
    print('Sprawdzenie adresow z zakresu: {}, TCP adres: {}, Rejestry od: {} do: {}, Port: {} \n'.format(unit_range,
                                                                                                             address,
                                                                                                             add_start + 1,
                                                                                                             add_start + len,
                                                                                                             23))

    count = 0
    connection = True
    try:
        while connection:
            print('Polaczenia: ', count)
            add_error=[]
            for i in range(unit_range[0],unit_range[1]+1):
                try:
                    client = ModbusTcpClient('210.200.181.102',port=23)
                    connection = client.connect()
                    print(connection)
                    if connection == True:
                        massure = client.read_holding_registers(add_start, len, unit=i)
                        print("Wartosci dla adresu {} : {}".format(i, massure.registers[0:]))
                    else:
                        print('Złe adresy rejstrow')
                    client.close()
                    time.sleep(0.2)


                except AttributeError:
                    print('Błąd połaczenia z adresem: {}'.format(i))
                    client.close()
                    time.sleep(0.1)
                    continue

            time.sleep(1)
            count += 1
            print('\n')

    except KeyboardInterrupt:
        print('Przerwanie przez urzytkownika')


if __name__ == "__main__":
    adresCheck()
