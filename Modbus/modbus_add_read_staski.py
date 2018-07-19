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

arg_1 = int(sys.argv[1])  # adres modbus start
arg_2 = int(sys.argv[2])  # adres modbus stop
arg_3 = int(sys.argv[3])  # predkosc polaczenia
arg_4 = int(sys.argv[4])  # adres rejestru start
arg_5 = int(sys.argv[5])  # ilosc rejestrow
arg_6 = int(sys.argv[6])  # typ rejestrów

''' 
    arg_6: 
        1- holding
        2 -input
 
'''

'''

    decoded = OrderedDict([
        ('string', decoder.decode_string(8)),
        ('bits', decoder.decode_bits()),
        ('8int', decoder.decode_8bit_int()),
        ('8uint', decoder.decode_8bit_uint()),
        ('16int', decoder.decode_16bit_int()),
        ('16uint', decoder.decode_16bit_uint()),
        ('32int', decoder.decode_32bit_int()),
        ('32uint', decoder.decode_32bit_uint()),
        ('32float', decoder.decode_32bit_float()),
        ('32float2', decoder.decode_32bit_float()),
        ('64int', decoder.decode_64bit_int()),
        ('64uint', decoder.decode_64bit_uint()),
        ('ignore', decoder.skip_bytes(8)),
        ('64float', decoder.decode_64bit_float()),
        ('64float2', decoder.decode_64bit_float()),
    ])


'''



def adresCheck(unit_start=arg_1, unit_stop=arg_2, speed=arg_3, add_start=arg_4 - 1, lenght=arg_5, typ=arg_6):
    unit_range = (unit_start, unit_stop)
    typ_rejestru = arg_6
    com = port()
    print('Sprawdzenie adresow z zakresu: {} : {}, dla predkosci: {}, Rejestry od: {} do: {}, Port: {} \n'.format(typ,
                                                                                                                  unit_range,
                                                                                                                  speed,
                                                                                                                  add_start,
                                                                                                                  add_start + lenght,
                                                                                                                  com))

    count = 0
    reg = []
    all_reg = []
    try:
        client = ModbusClient(method='rtu', port=com, baudrate=speed, stopbits=2, parity='N', bytesize=8, timeout=5)

        while True:
            start = clock()
            connection = client.connect()
            print('Sesja: ', count)

            for i in range(unit_range[0], unit_range[1] + 1):
                try:
                    if connection == True:
                        if typ == 1:
                            print ('holding')
                            massure = client.read_holding_registers(add_start, lenght, unit=i)
                            print(massure.registers)

                        elif typ == 2:

                            print ('input')
                            results = client.read_input_registers(add_start, lenght, unit=i)
                            divs=lenght/2
                            print(results.registers)
                            for a in range(int(divs)):
                                print(a)
                                print(results.registers[a*2:2+2*a])
                                res=results.registers[a*2:2+2*a]
                                decoder = BinaryPayloadDecoder.fromRegisters(res, byteorder=Endian.Big,wordorder=Endian.Little)
                                massure=(decoder.decode_32bit_float())
                                print("Wartosci dla adresu {} : {}".format(i, massure))
                                reg.append(massure)


                        else:
                            print ('Nie wlasciwy typ rejstru. Argument 6 1: holding 2: input')

                        #print("Wartosci dla adresu {} : {}".format(i, massure.registers[0:]))
                        #reg.append(massure.registers[0:])
                    else:
                        print('Złe adresy rejstrow')
                    time.sleep(1)

                except AttributeError:
                    print('AttributeError for address: {}'.format(i))
                    print(sys.exc_info()[0])
                    print (massure)
                    #reg.append(['nan'] * len)
                    time.sleep(1)
                    continue
            print(reg)
            all_reg.append(reg)
            reg = []
            client.close()
            end = clock() - start
            print('Czas wykonania: ', end, '\bs')

            time.sleep(0)
            count += 1
            print('\n')


    except KeyboardInterrupt:
        print('Przerwanie przez urzytkownika')
        print(all_reg)


if __name__ == "__main__":
    adresCheck()
