import math
import matplotlib.pyplot as plt
R1 = 1000
fx = []
x = 175000
while x > 970:
    fx.append(x)
    x -= 1


while True:
    R1 += 1000
    def func(x):
        fun = (x * 24) / (R1 + x)
        return fun


    czas2 = list(map(func, fx))
    maxf = max(czas2)
    print(maxf, R1)
    if maxf <= 10:
        break

print("Rezystancja R1 dzielnika  to : {} kohm".format(R1/1000))
plt.plot(fx, czas2)
plt.xlabel("Rntc ")
plt.ylabel("Uwy")
plt.title("funkcja")
plt.grid()
plt.show()




