import math
import matplotlib.pyplot as plt

tzew = []
x = 17
while x > -30:
    tzew.append(x)
    x -= 0.5
print(tzew)


def func(x):
    for i in (1, 2, 3, 4):
        czas = 0
        delta = 70 - (x * 10)
        R1=10
        if delta > 0:
            czas = int((math.log(delta)*i*10))
        else:
            czas = i*10

        jest1 = int(((int((170 - (x * 10)) / 10) ** 2) * 3) / 5)
        jest2 = int(((int((170 - (x * 10)) / 10) ** 2) * 2) / 5)
        jest3 = int(((int((170 - (x * 10)) / 10) ** 2) * 1) / 5)
        wykl = int(((int((170 - (x * 10)) / 10))**2)*i / 8)
        fun = (((x * 6) / (R1 + x**2))*(10))

        if i == 1:
            czas1 = czas
            wykl1 = wykl
        elif i == 2:
            czas2 = czas
            wykl2 = wykl
        elif i == 3:
            czas3 = czas
            wykl3 = wykl
        elif i == 4:
            czas4 = czas
            wykl4 = wykl
        elif i == 5:
            czas5 = czas
            wykl5 = wykl
        elif i == 6:
            czas6 = czas
            wykl6 = wykl

    return jest1, jest2, jest3,fun#czas1, czas2, czas3, czas4,# wykl1, wykl2, wykl3, wykl4,


czas2 = list(map(func, tzew))
print(czas2)

plt.plot(tzew, czas2)
plt.xlabel("temp. zew. ")
plt.ylabel("czas [min]")
plt.title("Krzywa grzewcza")
plt.grid()
plt.show()
