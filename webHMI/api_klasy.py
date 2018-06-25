from webHmiApi import Api

dd=Api('http://192.168.0.229','1D0DC2F189E5D96EB16AAD59A9A9C2C3C6FE3C0F',5)


ids=list(range(1,5))
a=map(str,ids)
id=','.join(a)
print(id)


#reg=dd.getRegLog('1528863571','1528949971','{}'.format(id))
#print(reg)

changreg=dd.changeRegVal('90',3)
print(changreg)