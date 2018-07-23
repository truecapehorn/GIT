import argparse
from ast import literal_eval


parser = argparse.ArgumentParser()

parser.add_argument('-b', action='store', dest='speed', default=9600,
                    help='Przechowuje predkosc polaczenia')

parser.add_argument('-u', action='append', dest='unit',
                    default=[],
                    help='Dodanie unit adress ex:(-u 1 -u 2 -3)',)

parser.add_argument('-s', action='store', dest='reg_start',
                    help='Start zapytania')


parser.add_argument('-l', action='store', dest='reg_lenght',
                    help='Długośc zapytania')


parser.add_argument('-i', action='store_const', dest='data_type',
                    const='ui16',
                    help='Rejetry typu int')

parser.add_argument('-f', action='store_const', dest='data_type',
                    const='float',
                    help='Rejetry typu float')


parser.add_argument('-q', action='store', dest='qty', default=3,
                    help='Przechowuje ilosc powtorzen')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')


results = parser.parse_args()
units=[]
for i in results.unit:
    units.append(int(i))


print ('speed     =', results.speed)
print ('unit       =', units)
print ('reg_start       =', results.reg_start)
print ('reg_lenght       =', results.reg_lenght)
print ('typ rejestru   =', results.data_type)
print ('qty     =', results.qty)



