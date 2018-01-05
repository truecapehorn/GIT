import math
import matplotlib.pyplot as plt

tzew = []
x = 5
while x > -15:
    tzew.append(x)
    x -= 0.5

print(tzew)
temperatura1 = []
krzywa = 1
temp = 1


def func(tzew, krzywa):
    tpok = 2300
    delta = tpok - (tzew * 100)
    temperatura = (delta * krzywa + 2300) / 23
    return temperatura

for i in tzew:

    if temp > 3800:
        krzywa -= 1
    elif temp < 2800:
        krzywa += 1
    temp = func(i, krzywa)
    lis=[temp,krzywa]
    if temp>2800 or temp<3800:
        temperatura1.append(lis)

print(temperatura1)

plt.plot(tzew, temperatura1)
plt.xlabel("temp. zew. ")
plt.ylabel("czas [min]")
plt.title("Krzywa grzewcza")
plt.grid()
plt.show()
