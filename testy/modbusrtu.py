import pymodbus
import serial
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient #initialize a serial RTU client instance
from pymodbus.transaction import ModbusRtuFramer

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

#count= the number of registers to read
#unit= the slave unit this request is targeting
#address= the starting address to read from

client= ModbusClient(method = "rtu", port="COM3",stopbits = 1, bytesize = 8, parity = 'E', baudrate= 9600)

#Connect to the serial modbus server
connection = client.connect()
print (connection)

#Starting add, num of reg to read, slave unit.
result= client.read_holding_registers(0x00,2,unit= 0xff)

print(result)

#Closes the underlying socket connection
client.close()
=======
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time
import sys

# TODO Dodac zapisywanie zmian w pliku.
# TODO Opisac program w funckcji lub klasie
start = 29 - 1
count = 2

arg_1 = int(sys.argv[1])  # adres modbus stary
arg_2 = int(sys.argv[2])  # adres modbus nowy

def add_change(unitOld = arg_1, unitNew=arg_2):
    try:
        client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=2400, stopbits=1, parity='N', bytesize=8, timeout=3)
        connection = client.connect()
        print(connection)

        rr = client.read_holding_registers(start, count, unit=unitOld)
        if rr.registers[1] == 2:
            predkosc = 2400
        else:
            predkosc = 'Nie 2400'
        print('Adres urzadzenia {},\nPredkosc jest ustawiona na {},'.format(rr.registers[0], predkosc))
        for i in range(1, 5):
            massure = client.read_holding_registers(6, 4, unit=unitOld)
            print(massure.registers[0:])
            time.sleep(1)
        testVar = input("Czy chcesz zmienic adres z {} na {} ( t/n).".format(unitOld, unitNew))
        if testVar == "t" or testVar == 'T':
            print('Zmieniam adres')
            time.sleep(2)
            if rr.registers[0] == unitOld:
                print('Zmieniam adres z {} na {}'.format(unitOld, unitNew))
                wr = client.write_register(start, unitNew, unit=unitOld)
                time.sleep(3)
                print('Przeprowadzono zmiane adresu')
                rr = client.read_holding_registers(start, count, unit=unitNew)
                print('Adres urzadzenia {},\nPredkosc jest ustawiona na {},'.format(rr.registers[0], rr.registers[1]))
                time.sleep(2)

            for i in range(1, 5):
                massure = client.read_holding_registers(6, 4, unit=unitNew)
                print(massure.registers[0:])
                time.sleep(1)



        client.close()

    except AttributeError:
        print('Adres jest inny niż {} , lub jest inny błąd w adresacji '.format(unitOld))

if __name__ == "__main__":
    add_change()
