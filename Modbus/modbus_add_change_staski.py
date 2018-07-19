from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time
import sys
from modbus_def import port

# TODO Dodac zapisywanie zmian w pliku.
# TODO Opisac program w funckcji lub klasie

arg_1 = int(sys.argv[1])  # adres modbus stary
arg_2 = int(sys.argv[2])  # adres modbus nowy
com = port()


def read_holding(reg_start, reg_lenght, mod_adress):
    try:
        client = ModbusClient(method='rtu', port=com, baudrate=2400, stopbits=1, parity='N', bytesize=8, timeout=3)
        connection = client.connect()
        time.sleep(0.3)
        massure = client.read_holding_registers(reg_start - 1, reg_lenght, unit=mod_adress)
        print('Rejestry :', massure.registers[0:])
        # print(connection)
        client.close()
        return connection, massure.registers
    except AttributeError:
        print('Połaczenie z adresem {} nie udane'.format(mod_adress))


def write_register(reg_add, val, mod_adress):
    try:
        client = ModbusClient(method='rtu', port=com, baudrate=2400, stopbits=1, parity='N', bytesize=8, timeout=3)
        client.connect()
        time.sleep(0.3)
        client.write_register(reg_add, val, unit=mod_adress)
        client.close()
    except AttributeError:
        print('Połaczenie z adresem {} nie udane'.format(mod_adress))
    return print('Nowa wartosc zapisana')


def add_change(unitOld=arg_1, unitNew=arg_2):
    unit = unitOld
    for i in range(1, 4):
        reg = read_holding(1, 30, unit)

    if reg != None:
        testVar = input("Czy chcesz zmienic adres z {} na {} ( t/n).".format(unitOld, unitNew))
        if testVar == "t" or testVar == 'T' and reg[1][28] == unitOld:
            print('Zmieniam adres z {} na {}'.format(unitOld, unitNew))
            write_register(28, unitNew, unitOld)
            time.sleep(0.5)
            print('Przeprowadzono zmiane adresu z {} na {}'.format(unitOld, unitNew))
            unit = unitNew
            for i in range(1, 4):
                read_holding(1, 30, unit)
    print('\n')


if __name__ == "__main__":
    add_change()
