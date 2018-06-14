#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import switchBoxD_API, time
from random import randint

halospoty = 'http://192.168.0.201'
lampki = 'http://192.168.0.202'
kotlownia = 'http://192.168.0.203'
'''
switchBoxD_API.device_state(kotlownia)
switchBoxD_API.wifi_scan(kotlownia)
switchBoxD_API.wifi_status(kotlownia)
switchBoxD_API.device_network(kotlownia)
switchBoxD_API.devive_uptime(kotlownia)
switchBoxD_API.switch_state(kotlownia)
switchBoxD_API.relay_state(kotlownia)
#switchBoxD_API.relay_set_post(lampki,1, 1)
#switchBoxD_API.relay_set_get(lampki,0,2)
'''
switchBoxD_API.device_state(kotlownia)
switchBoxD_API.device_state(lampki)
switchBoxD_API.device_state(halospoty)




scene=False
while scene:
    r = randint(0, 9)
    print(r)
    if r == 3:
        switchBoxD_API.relay_set_get(lampki, 0, 1)
    elif r == 5:
        switchBoxD_API.relay_set_get(lampki, 1, 1)
    elif r == 8:
        switchBoxD_API.relay_set_get(lampki, 0, 1)
    elif r == 2:
        switchBoxD_API.relay_set_get(lampki, 1, 1)
    elif r == 0:
        switchBoxD_API.relay_set_get(lampki, 0, 1)
        time.sleep(1)
        switchBoxD_API.relay_set_get(lampki, 1, 1)

    else:
        switchBoxD_API.relay_set_get(lampki, 0, 0)
        switchBoxD_API.relay_set_get(lampki, 1, 0)
    time.sleep(1)
