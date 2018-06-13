# -*- coding: utf-8 -*-
# !/usr/bin/python3


F = open('adr.txt', 'r')
dict={}
for line in F.readlines():
    parts = line.split()
    dict[parts[0]]=parts[1]

#print(dict)

swapDict={}
for key,val in dict.items():
    swapDict[val]=key

#print(swapDict)
L=list(swapDict.keys())
#print(L)
E=open(u'wej.txt', 'r')
for line in E.readlines():
    parts = line.split()
    #print(parts)
    w=[]
    for item in parts:
        if item in L:
            item = swapDict[item]
        #print(item)
        w.append(item)
    #print(w)
    setfile=open('pilk.txt','a')
    print(w,file=setfile)
    setfile.close()









