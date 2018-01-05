'''


'''


def data():
    F = open('exel.csv', 'r')
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
