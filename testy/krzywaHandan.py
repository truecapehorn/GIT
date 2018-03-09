import math
from math import sqrt as sqrt
import matplotlib.pyplot as plt

tzew = []
wsp=10
x = 20.0*wsp
while x > -50.0*wsp:
    tzew.append(x)
    x -= 0.5


def func(x):

    for i in (1,2,3):

        if i==1:

            c=60*60
            x1 = 15.0*wsp
            y1 =1*60
            x2 = -40.0*wsp
            y2 = 638*60
        elif i==2:

            c=114*60
            x1 = 15.0*wsp
            y1 =1*60
            x2 = -40.0*wsp
            y2 = 1300*60

        elif i==3:

            c=172*60
            x1 = 15.0*wsp
            y1 =1*60
            x2 = -40.0*wsp
            y2 = 1950*60

        a = (y2 - (y1 * x2 / x1) + (c * x2 / x1) - c) / (((1 * (x2**2)) - ((1 * (x1**2) * x2) / x1)))
        b = y1 / x1 - c / x1 - (a * (x1**2)) / x1


        fun = (a * x**2 + b * x + c)
        p=-b/(2*a)
        q=(-b**2+4*a*c)/(4*a)
        if fun>28800:
            fun=28800
        if x>150:
            fun=60
        if i==1:
            fun1=fun/60
        elif i==2:
            fun2=fun/60
        elif i==3:
            fun3=fun/60

        if x==20:
            print('Dla {5} f(x)=({0})x**2 + ({1})x + ({2})\nWierzcholek: ({3},{4})'.format(a, b, c, p, q, i))

    return fun1,fun2,fun3

Tco = list(map(func, tzew))
plt.plot(tzew, Tco)
plt.xlabel("Tzew. x 0.1  [stC]")
plt.ylabel("Czas [min]")
plt.title("Krzywa grzewcza")
plt.legend(('Krzywa 1','Krzywa 2', 'Krzywa 3'))
plt.grid()
plt.show()
