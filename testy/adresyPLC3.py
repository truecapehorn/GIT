# -*- coding: utf-8 -*-
# !/usr/bin/python3

def program1():
    F = open('adr.txt', 'r')
    dict = {}
    for line in F.readlines():
        parts = line.split()
        dict[parts[0]] = parts[1]

    # print(dict)

    swapDict = {}
    for key, val in dict.items():
        swapDict[val] = key

    # print(swapDict)
    L = list(swapDict.keys())
    # print(L)
    E = open(u'wej.txt', 'r')
    for line in E.readlines():
        parts = line.split()
        print(parts)
        w = []
        for item in parts:
            if item in L:
                item = swapDict[item]
            # print(item)
            w.append(item)
        print(w)
        setfile = open('pilk.txt', 'a')
        print(w, file=setfile)
        setfile.close()


def program2(addr):
    wej = 'X{}'.format(addr)
    F = open('adr.txt', 'r')
    dict1 = {}

    for line in F.readlines():
        # parts1 = line.strip()
        parts = line.split()
        # print(parts)
        dict1[parts[0]] = [parts[1], parts[2], parts[3], parts[4]]

    l=[]
    for k,v in dict.items(dict1):
        print(k,v)
        for i in range(len(v)):
            if v[i]!='-':
                w=v[i],k
                setfile = open('transp.txt', 'a')
                print(k,';' ,v[i], file=setfile)
                setfile.close()
                l.append(w)


    l.sort()
    print(len(l))
    print(l)
    add=[]
    for i in l:
        
        for a in range(len(i)):
            print(a)
        #print(l[i][0],l[i][1])







def program3():
    F = open('adr.txt', 'r')
    dict = {}
    dict1 = {}
    dict2 = {}
    dict3 = {}
    dict4 = {}

    for line in F.readlines():
        parts = line.split()
        # print(parts)
        dict[parts[0]] = [parts[1], parts[2], parts[3], parts[4]]

        dict1[parts[0]] = parts[1]
        dict2[parts[0]] = parts[2]
        dict3[parts[0]] = parts[3]
        dict4[parts[0]] = parts[4]

    swapDict1 = {}
    swapDict2 = {}
    swapDict3 = {}
    swapDict4 = {}

    print(dict['X1'])
    # print(dict1)
    # print(dict2)
    # print(dict3)
    # print(dict4)
    for key, val, in dict1.items():
        # print(key,val)
        swapDict1[val] = key

    for key, val, in dict2.items():
        # print(key,val)
        swapDict2[val] = key

    for key, val, in dict3.items():
        # print(key,val)
        swapDict3[val] = key

    for key, val, in dict4.items():
        # print(key,val)
        swapDict4[val] = key


program2(0)
