
import definicje


serverHost = "192.168.0.35"
serverPort = 502
coilAdrStart = 0+0
coilLength = 96
switchAdrStart = 1000+0
switchLength = 60
regAdrStartR = 0
regLengthR = 4168
regAdrStartD = 6000
regLengthD = 120 #2998


# define modbus server host, port
c = definicje.defineModbus(serverHost, serverPort)
Y={}
X={}
REG_R ={}
REG_D = {}
regs =[]

while True:
    # modbus check
    definicje.modbusCheck(c,serverHost,serverPort)
    # read n coils
    while c.is_open():
        coils=definicje.readCoils(c, coilAdrStart, coilLength)
        switches=definicje.readCoils(c, switchAdrStart, switchLength)
        regAdrStart=regAdrStartR
        regsR=[]
        while regAdrStart<regLengthR-120:
            regsR=regsR+definicje.readRegister(c,regAdrStart,120)
            print(regAdrStart)
            print(regsR)
            regAdrStart+=121

        regsD = definicje.readRegister(c, regAdrStartD, regLengthD)

        for nr, coil in enumerate(coils):
            Y['Y{}'.format(nr)]=coil
        for nr, switch in enumerate(switches):
            X['X{}'.format(nr)] = switch
        for nr, reg in enumerate(regsR):
            REG_R['R{}'.format(nr)] = reg
        for nr, reg in enumerate(regsD):
            REG_D['D{}'.format(nr)] = reg

        for k,v in Y.items():
            print('{} - {}'.format(k,v))
        for k,v in X.items():
            print('{} - {}'.format(k,v))
        print(Y['Y3'])
        print('\nCoils: ',Y)
        print('\nSwiches: ',X)
        print('\nREG R: ',REG_R)
        print('\nREG D: ', REG_D)
        for k,v in sorted(REG_R.items()):
            if v!=0:
                print('{} - {}'.format(k,v))
        break
    break
