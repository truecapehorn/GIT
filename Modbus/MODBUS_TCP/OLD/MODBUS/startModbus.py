
import definicje


serverHost = "192.168.0.35"
serverPort = 502
coilAdrStart = 0+0
coilLength = 95
regAdrStart = 4128
regLength = 8
writeCoilAddres=2000+1030


# define modbus server host, port
c = definicje.defineModbus(serverHost, serverPort)
while True:
    # modbus check
    definicje.modbusCheck(c,serverHost,serverPort)
    # read n coils
    while c.is_open():
        bits=definicje.readCoils(c, coilAdrStart, coilLength)
        regs=definicje.readRegister(c,regAdrStart,regLength)
        for nr, bit in enumerate(bits):
            print('Y{} - {}'.format(nr,bit))
        print('\nBits: '+ str(bits))
        print('\nRegs: '+str(regs))

