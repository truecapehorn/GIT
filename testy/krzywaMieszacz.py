import math
from math import sqrt as sqrt
import matplotlib.pyplot as plt

tzew = []
wsp=1
x = 20.0*wsp
while x > -31.0*wsp:
    tzew.append(x)
    x -= 0.5


def func(x):


    c = 33.0*wsp # temp dla 0 stopni
    x1 = 20.0*wsp
    y1 = 20.0*wsp
    x2 = -20.0*wsp
    y2 = 40.0*wsp
    a = (y2 - (y1 * x2 / x1) + (c * x2 / x1) - c) / (((1 * (x2**2)) - ((1 * (x1**2) * x2) / x1)))
    b = y1 / x1 - c / x1 - (a * (x1**2)) / x1
    fun = a * x**2 + b * x + c
    if x == -25:
        print('f(x)=({})x**2 + ({})x + ({})'.format(a, b, c))
    #if x<-25:fun=42

    return fun,

Tco = list(map(func, tzew))
plt.plot(tzew, Tco)
plt.xlabel("Tzew. ")
plt.ylabel("Tco")
plt.title("Krzywa grzewcza")
plt.grid()
plt.show()
