import math
import matplotlib.pyplot as plt


F = open('ntc.txt', 'r')
chart=[]
for line in F.readlines():
    parts = line.split()
    chart.append(parts)
print(chart)

temperatura=[]
rezystancja=[]

for i in chart:
    temperatura.append(int(i[0]))
    rezystancja.append(int(i[1]))

print(temperatura)
print(rezystancja)



plt.plot(rezystancja, temperatura)
plt.xlabel("R ")
plt.ylabel("temperatura")
plt.title("funkcja")
plt.grid()
plt.show()






