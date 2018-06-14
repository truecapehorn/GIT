#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yamaha
import rxv
import switchBoxD_API
import loctime
import time
'''Uruchamia i po 40min wyłącza wzmacniacz'''
rx = rxv.RXV("http://192.168.1.102:80/YamahaRemoteControl/ctrl", "RX-V671")

halospoty = 'http://192.168.1.201'
lampki = 'http://192.168.1.202'
kotlownia = 'http://192.168.1.203'

while True:

    if rx.on == False:
        yamaha.receiversInputFind(rx)
        yamaha.receiversOnOff(rx, True)
        time.sleep(1)
        yamaha.receiversVol(rx, -50)
        time.sleep(1)
        yamaha.receiversSetInput(rx, 'TUNER')
        time.sleep(2)

    if rx.on == True:
        time.sleep(3600)
        # print(yamaha.receiversInputFind(rx))
        yamaha.receiversOnOff(rx, False)
        switchBoxD_API.relay_set_get(lampki, 0, 0)
        switchBoxD_API.relay_set_get(lampki, 1, 0)
        switchBoxD_API.relay_set_get(halospoty, 0, 0)
        switchBoxD_API.relay_set_get(halospoty, 1, 0)
        break
