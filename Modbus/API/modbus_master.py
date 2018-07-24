
from modbus_rtu_v3 import Api
import argparse

'''
Main program do osblugi Api dla modbasa rtu.
Musi sie znajdowac w tym samym folderze co modbus_rtu_v3

Za pomoca parsera odczytuje opcje wprowadzane w terminal. 

Pomoc dla opcji po wpisaniu w terminal:

python modbus_master.py -h

!!!!Wersja zmiany adresu dla czujnikow appr!!!!


'''



parser = argparse.ArgumentParser()

parser.add_argument('-b', action='store', dest='speed', default=9600,
                    help='Predkość połączenia def: 9600')

parser.add_argument('-u', action='append', dest='unit',
                    default=[],
                    help='Adres Modbus ex:(-u 1 -u 2 -3)', )

parser.add_argument('-s', action='store', dest='reg_start',
                    help='Start zapytania')

parser.add_argument('-l', action='store', dest='reg_lenght',
                    help='Długość zapytania')

parser.add_argument('-i', action='store_const', dest='data_type',
                    const='ui16',
                    help='Rejetry typu int')

parser.add_argument('-f', action='store_const', dest='data_type',
                    const='float',
                    help='Rejetry typu float')

parser.add_argument('-q', action='store', dest='qty', default=3,
                    help='Ilosc powtorzen def: 3')

parser.add_argument('-a', action='store_true', default=False,
                    dest='boolean_switch',
                    help='Uruchominie zmiany adresu dla appar')

parser.add_argument('-o', action='store', dest='unit_old',
                    help='Stary unit adres ')

parser.add_argument('-n', action='store', dest='unit_new',
                    help='Nowy unit adres')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')

results = parser.parse_args() # pobranie rezultatow parsera
add_change = results.boolean_switch # sprawdzenie co chemy zrobic ( odczytanie rej, czy zmiana adresu )

if add_change == False:

    units = []
    for i in results.unit:
        units.append(int(i))

    print(
        "\n     Data:\nspeed = {},\nunit = {},\nreg_start= {},\nreg_lenght= {},\nreg_type= {},\nqty= {},".format(
            results.speed, units,
            results.reg_start,
            results.reg_lenght,
            results.data_type,
            results.qty))

    speed = int(results.speed)
    unit = units
    reg_start = int(results.reg_start)
    reg_lenght = int(results.reg_lenght)
    data_type = results.data_type
    qty = int(results.qty)
    rtu = Api(speed=speed)
    if data_type == 'ui16':
        readholding = rtu.read_holding(unit, reg_start, reg_lenght, data_type, qty)
    elif data_type == 'float':
        readinput = rtu.read_input(unit, reg_start, reg_lenght, data_type, qty)
else:
    unit_old = int(results.unit_old)
    unit_new = int(results.unit_new)
    rtu = Api(speed=9600)
    add = rtu.appar_add_change(unit_old, unit_new, 'ui16')
