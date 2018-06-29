#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read_bit
# read 10 bits and print result on stdout

from pyModbusTCP.client import ModbusClient
import time

SERVER_HOST = "91.239.155.66"
SERVER_PORT = 500
ADDRESS_START = 2000+1030
ADDRESS_WR = 2000+1030
LENGHT  = 120

toggle = True
is_ok=False
c = ModbusClient()

# uncomment this line to see debug message
#c.debug(True)

# define modbus server host, port
c.host(SERVER_HOST)
c.port(SERVER_PORT)

while True:
    # open or reconnect TCP to server
    if not c.is_open():
        if not c.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))

    # if open() is ok, read coils (modbus function 0x01)
    if c.is_open():
        if   is_ok==False:
            is_ok = c.write_single_coil(ADDRESS_WR, toggle)

            if is_ok:
                print("bit #" + str(ADDRESS_WR) + ": write to " + str(toggle))

            else:
                print("bit #" + str(ADDRESS_WR) + ": unable to write " + str(toggle))
            time.sleep(0.5)
        # read 10 bits at address 0, store result in regs list
        bits = c.read_coils(ADDRESS_START, LENGHT)

        # if success display registers
        if bits:
            print(is_ok)
            print("bit from M{} to M{} : ".format(ADDRESS_START-2000,ADDRESS_START+LENGHT-2001)+str(bits))
            if bits[0]==False:
                is_ok=False
            bit_no = ADDRESS_START
            for i in bits:

                print('Bit M{} - {}'.format(bit_no-2000,i))
                bit_no+=1

    # sleep 2s before next polling
    time.sleep(2)