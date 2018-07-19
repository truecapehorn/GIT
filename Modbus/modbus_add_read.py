#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time
import sys
from sys import platform
from modbus_def import port
from time import clock

arg_1 = int(sys.argv[1])  # adres modbus start
arg_2 = int(sys.argv[2])  # adres modbus stop
arg_3 = int(sys.argv[3])  # predkosc polaczenia
arg_4 = int(sys.argv[4])  # adres rejestru start
arg_5 = int(sys.argv[5])  # ilosc rejestrow





def adresCheck(unit_start=arg_1, unit_stop=arg_2, speed=arg_3, add_start=arg_4 - 1, len=arg_5):
    unit_range = (unit_start, unit_stop)
    com=port()
    print('Sprawdzenie adresow z zakresu: {}, dla predkosci: {}, Rejestry od: {} do: {}, Port: {} \n'.format(unit_range,
                                                                                                             speed,
                                                                                                             add_start + 1,
                                                                                                             add_start + len,
                                                                                                             com))

    count = 0
    reg=[]
    all_reg=[]
    try:
        client = ModbusClient(method='rtu', port=com, baudrate=speed, stopbits=1, parity='N', bytesize=8, timeout=1)

        while True:
            start = clock()
            connection=client.connect()
            print('Sesja: ', count)
            #for i in range(unit_range[0],unit_range[1]+1):
            for i in [1,2,3,4]:
                try:
                    if connection == True:
                        massure1 = client.read_holding_registers(add_start, len, unit=i)
                        massure2= client.read_input_registers(add_start,len,unit=i)

                        if i==2:
                            print("Wartosci dla adresu {} : {}".format(i, massure2.registers[0:]))
                            reg.append(massure2.registers[0:])
                        else:
                            print("Wartosci dla adresu {} : {}".format(i, massure1.registers[0:]))
                            reg.append(massure1.registers[0:])

                    else:
                        print('Złe adresy rejstrow')
                    time.sleep(0.1)

                except AttributeError:
                    print('Błąd połaczenia z adresem: {}'.format(i))
                    reg.append([0]*len)
                    time.sleep(1)
                    continue
            print(reg)
            all_reg.append(reg)
            reg=[]
            client.close()
            end = clock() - start
            print('Czas wykonania: ', end,'\bs')

            time.sleep(0)
            count += 1
            print('\n')


    except KeyboardInterrupt:
        print('Przerwanie przez urzytkownika')
        print(all_reg)


if __name__ == "__main__":
    adresCheck()

