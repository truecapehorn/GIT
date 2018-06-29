import definicje
import time
import random



def regRead(c, addresStart, addresEnd):
    regs = []
    address = addresStart
    if address + 120 > addresEnd:
        lenght = addresEnd - addresStart
    else:
        lenght = 120

    while True:
        if len(regs)+120<=addresEnd-addresStart:
            pass

        elif len(regs)+120 > addresEnd-addresStart:
            address = address
            lenght = addresEnd-address

        if len(regs) == addresEnd-addresStart:
            #print('break',len(regs))
            break

        #print('odczyt - ',address,':',lenght+address,'rejestrow :',lenght)
        #print(len(regs))
        #regs=regs+c[address,lenght+address]
        regs = regs + definicje.readRegister(c, address, lenght)
        address += lenght
        #time.sleep(0.03)
    return regs

if __name__ == '__main__':

    c = [x for x in range(10000)]
    random.shuffle(c)
    regs=regRead(c,6000,8925)
    print(regs)
