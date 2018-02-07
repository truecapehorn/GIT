import math
from math import sqrt as sqrt
import matplotlib.pyplot as plt

tzew = []
wsp=10
x = 20.0*wsp
while x > -31.0*wsp:
    tzew.append(x)
    x -= 0.5


def func(x):


        c=30.0*wsp
        x1 = 20.0*wsp
        y1 =18*wsp
        x2 = -30.0*wsp
        y2 = 38.0*wsp

        a = (y2 - (y1 * x2 / x1) + (c * x2 / x1) - c) / (((1 * (x2**2)) - ((1 * (x1**2) * x2) / x1)))
        b = y1 / x1 - c / x1 - (a * (x1**2)) / x1

        fun = a * x**2 + b * x + c

        p=-b/(2*a)
        q=(-b**2+4*a*c)/(4*a)
        if x==20:
            print('f(x)=({0})x**2 + ({1})x + ({2})\nWierzcholek: ({3},{4})'.format(a, b, c, p, q))

        return fun,

Tco = list(map(func, tzew))
plt.plot(tzew, Tco)
plt.xlabel("Tzew. ")
plt.ylabel("Tco")
plt.title("Krzywa grzewcza")
plt.grid()
plt.show()
