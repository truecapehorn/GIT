'''
Plik do zczytania danych z bazy csv

'''


def data():
    F = open('export.txt','r',encoding="utf-8-sig", )
    lista = []
    for line in F.readlines():
        parts1=line.strip()
        parts2=parts1.split(';')
        lista.append(parts2)
    F.close()
    return lista

lista=data()
for i in lista:
    print(i)
print('\n')
for i in range(10):
    print(lista[i])

for num,i in enumerate(lista[1]):
    print("lista {}: {}".format(num,i))
