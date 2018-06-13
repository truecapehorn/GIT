from math import log as log

#t2 - czas dla 50% wartosci ustalonej, t3- czas dla 63% wartosci ustalonej
t0=0
t2=10.0
t3=12.0


tempStart=204.0
tempUst = 210.0
tempMax=999.0
zadStart=208.0
zadStop=210.0

dY=((tempUst/tempMax)*100)-((tempStart/tempMax)*100)
dU=((zadStop/tempMax)*100)-((zadStart/tempMax)*100)
print (dY,dU)
t2=t2*60
t3=t3*60
k=dY/dU
t1=(t2-log(2)*t3)/(1-log(2))
tau=t3-t1
td=t1-t0
r=td/tau


print('\nt1 {},\ntau= {},\ntd= {},\nr= {},\nk= {},\n'.format(t1,tau,td,r,k))

Kp=1/(k*r)*((4/3)+(r/4))
Ti=td*((32+6*r)/(13+8*r))
Td=td*(4/(11+2*r))

print('Kp ={},\nTi ={},\nTd= {},\n'.format(Kp,Ti,Td))
