#!/usr/bin/env python
# -*- coding: utf-8 -*-

# connection with FATEK by MODBUS TCP


from pyModbusTCP.client import ModbusClient
import time
import inspect  # do wyswietlania nazyw funkcji


def przerywnik(funkcja):
    print('\n' + 70 * '-' + '\n#', 'Program: ' + funkcja)


def defineModbus(serverHost, serverPort):
    przerywnik(inspect.getframeinfo(inspect.currentframe())[2])  # nazwa funkcji
    # defiine atribut of modbus client
    c = ModbusClient()
    # uncomment this line to see debug message
    # c.debug(True)
    # define modbus server host, port
    c.host(serverHost)
    c.port(serverPort)
    print('Define modbus server at {}::{}'.format(serverHost, serverPort))

    return c


def modbusCheck(c, serverHost, serverPort):
    przerywnik(inspect.getframeinfo(inspect.currentframe())[2])  # nazwa funkcji
    timeSleep = 2
    # open or reconnect TCP to server
    if not c.is_open():
        if not c.open():
            print('Unable to connect to the server at {}::{}'.format(serverHost, serverPort))
            print('Reconnect TCP to server wait {}s'.format(timeSleep))
            time.sleep(timeSleep)
        else:
            print('Modbus connection open OK!')


def readCoils(c, adrStart, length):
    przerywnik(inspect.getframeinfo(inspect.currentframe())[2])  # nazwa funkcji
    timeSleep = 0.03
    printer=False
    # if open() is ok, read coils (modbus function 0x01)
    # read n bits from ADDRES_START
    bits = c.read_coils(adrStart, length)
    # if success display registers not empty
    if bits and printer==True:
        bit_no = adrStart
        for i in bits:
            print('Bit M{} - {}'.format(bit_no - 2000, i))
            bit_no += 1
    print('Sleep {}s before next polling'.format(timeSleep))
    time.sleep(timeSleep)
    return bits


def readRegister(c, adrStart, length):
    przerywnik(inspect.getframeinfo(inspect.currentframe())[2])  # nazwa funkcji
    timeSleep = 0.03
    printer = False
    # if open() is ok, read register (modbus function 0x03)
    # read n reg from ADDRES_START
    regs = c.read_holding_registers(adrStart, length)
    # if success display registers
    if regs and printer == True :
        reg_no = adrStart
        for i in regs:
            print('Rejestr o adresie {} = {}'.format(reg_no, i))
            reg_no += 1
    #print('Sleep {}s before next polling'.format(timeSleep))
    time.sleep(timeSleep)
    return regs


def writeSinglecoil(c, addres, toggle):
    ''' Toggle = True or False '''
    przerywnik(inspect.getframeinfo(inspect.currentframe())[2])  # nazwa funkcji
    timeSleep = 2

    # write  bits value in modbus adress
    print("")
    print("write bits")
    print("----------")
    print("")
    write_ok = c.write_single_coil(addres, toggle)
    if write_ok:
        print("bit #" + str(addres) + ": write to " + str(toggle))
    else:
        print("bit #" + str(addres) + ": unable to write " + str(toggle))
        time.sleep(0.5)
    time.sleep(1)

    # read  bits value in modbus adress
    print("")
    print("read bits")
    print("---------")
    print("")
    readOK = readCoils(c, addres, 1)
    if readOK == toggle:
        print('Write OK')
        write_status=True
    else:
        print("unable to read")
        write_status=False

    print('Sleep {}s before next polling'.format(timeSleep))
    time.sleep(timeSleep)

    return write_status
