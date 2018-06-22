from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time
import sys

# TODO Dodac zapisywanie zmian w pliku.
# TODO Opisac program w funckcji lub klasie
start = 29 - 1
count = 2
unitOld = 1
unitNew = 2

client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=2400, stopbits=1, parity='N', bytesize=8, timeout=3)
connection = client.connect()
print(connection)
try:
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

except AttributeError:
    print('Adres jest inny niż {} , lub jest inny błąd w adresacji '.format(unitOld))

client.close()
