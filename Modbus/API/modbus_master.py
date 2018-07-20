import sys
from ast import literal_eval
from modbus_rtu_v3 import Api

'''

arg_1 = (sys.argv[1])  #  speed of unit             
arg_2 = (sys.argv[2])  # list of unit               
arg_3 = (sys.argv[3])  # add of reg start           
arg_4 = (sys.argv[4])  # len of reg                 
arg_5 = (sys.argv[5])  #  data type of reg          
arg_6 = (sys.argv[6])  # repeat                     



'''
print(__doc__)

arg_1 = (sys.argv[1])  #  holding , input
arg_2 = (sys.argv[2])  #  speed of unit
arg_3 = (sys.argv[3])  # list of unit
arg_4 = (sys.argv[4])  # add of reg start
arg_5 = (sys.argv[5])  # len of reg
arg_6 = (sys.argv[6])  #  data type of reg
arg_7 = (sys.argv[7])  # repeat


reg_type=arg_1
speed=int(arg_2)
unit=literal_eval(arg_3)
reg_start=int(arg_4)
reg_lenght=int(arg_5)
data_type=arg_6
qty=int(arg_7)

rtu=Api(speed=speed)

if reg_type=="":
    readholding = rtu.read_holding(unit, reg_start, reg_lenght, data_type, qty)
else:
    readinput=rtu.read_input(unit, reg_start, reg_lenght, data_type, qty)













