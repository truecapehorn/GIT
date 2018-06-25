from webHmiApi import Api

Blebox=Api('http://192.168.1.201',"",3,)

def wifi_status():
    '''
        WiFi - Get information about connection to WiFi network
        RX:
        "scanning": Is scanning for WiFi networks in progress.,
        "ssid": Name of connected WiFi network.,
        "station_status": Status of current conection with WiFi network. Where:
                        0 - Not configured, 1 - Connecting,
                        2 - Wrong password, 3 - WiFi network not found,
                        4 - Error, 5 - Connected.,
        "ip": Device's IP in WiFi network.
    '''
    header={}
    api_address = '/api/wifi/status'
    address = (api_address, header)
    r=Blebox.reqGet(address)
    print(r)
    return r

wifi_status()










