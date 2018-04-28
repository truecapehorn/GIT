import switchBoxD_API
import time

addres = 'http://192.168.1.203'


switchBoxD_API.relay_set_get(addres,1,1)
time.sleep(60)
switchBoxD_API.relay_set_get(addres,1,0)
