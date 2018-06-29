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

            for nr, coil in enumerate(coils):
                Y['Y{}'.format(nr)] = coil
            for nr, switch in enumerate(switches):
                X['X{}'.format(nr)] = switch
            # for nr, reg in enumerate(regsR):
            #     REG_R['R{}'.format(nr)] = reg
            # for nr, reg in enumerate(regsD):
            #     REG_D['D{}'.format(nr)] = reg

            # for k, v in Y.items():
            #     pass
            #     print('{} - {}'.format(k, v))
            # for k, v in X.items():
            #     pass
            #     print('{} - {}'.format(k, v))
            # print('\nCoils: ', Y)
            # print('\nSwiches: ', X)
            # print('\nREG R: ', REG_R)
            # print('\nREG D: ', REG_D)
            # print('\nSek: ',REG_R['R4128'])

            break
        break
    return Y, X, REG_R, REG_D


# def imputOutput(REG, mapa):
#     for k1, v1 in REG[1].items():
#         print(k)
        # if v1 == True:
        #     print('Wejscie {} jest {}'.format(k1, v1))
        #     for k2,v2 in mapa[0].items():
        #         if v2==k1:
        #             if mapa[1][k2]==True:
        #                 mapa[1][k2]=False
        #             else:
        #                 mapa[1][k2] = v1
        #             print(k2,mapa[1][k2],time.time())
        #     print(mapa[1],'\n')

def imputOutput(REG, mapa):
    lista={}
    lista1={}
    for k1, v1 in REG[1].items():
        for k2,v2 in mapa[0].items():
            if v2==k1:
                lista[k2]=v1
        # print(k)
            if v1 == True:
                print('Wejscie {} jest {}'.format(k1, v1))

                print(lista)


def maping():
    F = open('inputMap.txt', 'r')
    # excel_document = openpyxl.load_workbook('adr2.xlsx')
    # print(excel_document)
    mapa = {}
    wyjscia={}
    lista = []
    for line in F.readlines():
        parts = line.split()
        lista.append(parts)
    F.close()
    print('lista: ',lista)
    for i in lista:
        mapa[i[0]] = i[1]
    print('mapa: ',mapa)
    for k in mapa.keys():
        wyjscia[k]=False
    print('wyjscia: ',wyjscia)


    return mapa,wyjscia


c = modbusConnection()
mapa = maping()
REG = readModbusReg(c)
print('\nCoils: ',REG[0])
print('\nSwiches: ', REG[1])
print('\nREG R: ', REG[2])
print('\nREG D: ', REG[3])

while True:

    REG = readModbusReg(c)
    pkl = open('reg.pkl', 'wb')
    pickle.dump(REG, pkl)
    pkl.close()
    imputOutput(REG, mapa)
