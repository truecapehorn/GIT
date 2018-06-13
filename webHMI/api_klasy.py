from webHmiApi import Api

dd=Api('http://192.168.0.229','DKSJ323JNDJDEIE3')

reg=dd.getRegLog('444','666','1,2,3,4')
print(reg)