import definicje, regRead, randTable
import random
import pickle,time

serverHost = "192.168.0.35"
serverPort = 502
coilAdrStart = 0 + 0
coilLength = 96
switchAdrStart = 1000 + 0
switchLength = 60
regAdrStartR = 0
regLengthR = regAdrStartR + 4168
regAdrStartD = 6000
regLengthD = regAdrStartD + 2998

# c=randTable.random_reg()
# coils=randTable.random_bool()
# switches=randTable.random_bool()

Y = {}
X = {}
REG_R = {}
REG_D = {}


def modbusConnection():
    # define modbus server host, port
    c = definicje.defineModbus(serverHost, serverPort)
    # modbus check
    definicje.modbusCheck(c, serverHost, serverPort)
    return c


def readModbusReg(c):
    ''' Return [0] - {Y}
        Return [1] - {X}
        Return [2] - {R}
        Return [3] - {D}
    '''
    while True:

        # read n coils
        while c.is_open():
            coils = definicje.readCoils(c, coilAdrStart, coilLength)
            switches = definicje.readCoils(c, switchAdrStart, switchLength)
            # regsR = regRead.regRead(c, regAdrStartR, regLengthR)
            # regsD = regRead.regRead(c, regAdrStartD, regLengthD)
            Y=coils
            X=switches

            break
        break
    return Y, X


def maping():
    F = open('outputMap.txt', 'r')
    # excel_document = openpyxl.load_workbook('adr2.xlsx')
    # print(excel_document)
    wejscia=[]
    wyjscia=[]
    lista=[]
    for line in F.readlines():
        parts = line.split()
        lista.append(parts)
    F.close()
    print('lista: ',lista)
    for i in lista:
        wejscia.append(i[0])
        wyjscia.append(i[1::])
    print(wyjscia)
    return wejscia,wyjscia




c = modbusConnection()
REG = readModbusReg(c)
mapa=maping()
print('\nCoils: ',REG[0])
print('\nSwiches: ', REG[1],'\n')




while True:
    REG = readModbusReg(c)
    for nr, x in enumerate(REG[1]):
        M=list(map())





