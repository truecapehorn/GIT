import rxv
from rxv import PlaybackSupport



def receiversFind():
    receivers = rxv.find()
    return print(receivers)

def receiversOnOff(rx,turn=True):
    rx.on=turn
    return print('Receiver= {} OK'.format(turn))

def receiversVol(rx,vol=-51):
    rx.volume=vol
    return print('Receiver vol= {}'.format( vol))

def receiversInputFind(rx):
    return rx.inputs()

def receiversSetInput(rx,input='NET RADIO'):
    rx.input=input
    return print('Input = {}'.format(input))

def receiversPlay(rx):
    if (rx.get_playback_support() & PlaybackSupport.PLAY) != 0:
        rx.play()
    return print('Play OK! ')

rx=receiversFind()
rx= rxv.RXV("http://192.168.0.201:80/YamahaRemoteControl/ctrl", "RX-V473")

receiversOnOff(rx,True)
receiversVol(rx,-47)
receiversInputFind(rx)
receiversSetInput(rx)
receiversPlay(rx)
