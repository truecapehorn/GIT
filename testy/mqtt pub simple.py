
import paho.mqtt.publish as publish
import json
import time
import datetime
from pogoda import pogoda as pog

#auth = {"username":"user", "password":"admin"}

while True:
    czas=time.localtime()
    timer=datetime.datetime.now().isoformat()
    pogodynka=pog()

    rok=czas[0]
    miesiac=czas[1]
    dzien=czas[2]
    godzina=czas[3]
    miniuta=czas[4]
    sekunda=czas[5]
    temperatura=pogodynka[0]
    wiatr = pogodynka[1]
    cisnienie = pogodynka[2]
    icona=pogodynka[3]

    MQTT_MSG=json.dumps(
        {
        "d" : {
        "ROK" : [ rok],
    	"MIESIAC" : [ miesiac ],
        "DZIEN" : [dzien],
    	"GODZINA" : [ godzina ],
        "MINUTA" : [miniuta],
    	"SEKUNDA" : [sekunda],
        "TEMPERATURA":[temperatura],
        "WIATR":[wiatr],
        "CISNIENIE":[cisnienie],
        "IKONA":[icona],

        },
        #"ts" : "2018-02-09T08:08:49.829542"
        "ts" : timer
    })


    publish.single("testy4", MQTT_MSG, qos=2, retain=False, hostname="192.168.0.135",
        port=1883, keepalive=60, will=None, auth=None, tls=None,
        )
    print(MQTT_MSG)
    print(pogodynka)


    time.sleep(1)



#{"d" : {"ROK": int(2015),"MIESIAC":int(day)},"ts" : "2017-04-18T17:36:52.501856"}
