# -*- coding: utf-8 -*-
# !/usr/bin/python3


''' Program dopasowuje wejscia do wyjsc i transponuje do formy przjazniejszej yn=xn,xn...'''

''' Nalezy na wejsciepodac mu tabele o jednakowej ilosci kolumn we
    wszystkich wierszach np:
    X2	Y27	$	$	$
    X3	Y34	Y38	$	$
    X4	Y24	Y25	Y9	$
    X5	Y20	Y21	$	$
    X6	Y30	Y31	Y20	Y21

    Wielkosc tabeli nalezy uwzglednic w słowniku dict1

    Na wyjscu otrzymamy :
    Y27  -  X2
    Y28  -  X39
    Y29  -  X39
    Y3  -  T42
    Y30  -  X6;X36;T40;T44
    Y31  -  X6;X36;T40;T44
    Y32  -  X38

'''
# TODO: Dodac dopasowywanie wielkosci tabeli wejsciowej do słownika ddict1
# TODO: Dodac sortowanie y0,y1,y2. Trzeba zczytac wyjscie od drugiego znaku
    #   Zrobic z niej inna kolumne i posortowac po niej.



def program2():
    F = open('adr3.txt', 'r')
    # excel_document = openpyxl.load_workbook('adr2.xlsx')
    # print(excel_document)
    dict1 = {}
    lista = []
    for line in F.readlines():
        # parts1 = line.strip()
        parts = line.split()
        lista.append(parts)

    for i in lista:
        dict1[i[0]] = [i[1], i[2], i[3]]

    l = []
    w = []

    for k, v in dict.items(dict1):
        for i in range(len(v)):
            if v[i] != '$':
                w = [v[i], k]
                l.append(w) # tablica y,x ale nie jescze z powtórzeniami

    print('Długosc tablicy przed kompresją :',len(l),'\n')
    print(l, '\n')
    ad = {}
    s = []
    for i in l:
        v = i[1]
        if str(i[0]) not in ad.keys(): # jezeli nie ma powtórzenia to dodaje nowa wartosc do klucza
            ad[i[0]] = v
        else:
            ad[i[0]] = '{};{}'.format(ad[i[0]], v, ) # a jezeli jest to dodaje nastepny element do słownika

    print(ad, '\n')
    print('Długosc tablicy po kompresji :',len(ad),'\n')

    for k in sorted(ad):
        setfile = open('transp2.txt', 'a')
        print(k, ' - ', ad[k], file=setfile)
        setfile.close()
        print(k, ' - ', ad[k])

    #spr='Y38'
    #print('\n','{} - {}'.format(spr,ad[spr]))


program2()
