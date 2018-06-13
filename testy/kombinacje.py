
I1L1=4.05
I2L1=9.89
I3L1=6.05


I1L2=4.85
I2L2=4.57
I3L2=11.22

I1L3=9.14
I2L3=12.87
I3L3=4.28


c1=(I1L1,I1L2,I1L3)
c2=(I2L1,I2L2,I2L3)
c3=(I3L1,I3L2,I3L3)

komb=[(a,b,c) for a in c1 for b in c2 for c in c3 ]

print(komb)
print(len(komb))

for nr,i in enumerate(komb):
        sum=i[0]+i[1]+i[2]
        print(sum)
        if sum==26.07:
            print('jest')
