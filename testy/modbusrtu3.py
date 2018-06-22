from pymodbus3.client.sync import ModbusTcpClient
from pymodbus3.client.sync import ModbusSerialClient

client = ModbusSerialClient(method='rtu',port='/dev/ttyUSB0',parity='N',stopbits=1,bytesize=8,baudrate=9600,timeout=3)
result = client.read_holding_registers(1,2,unit=1)
client.close()

