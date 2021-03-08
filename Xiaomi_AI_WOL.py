#!/usr/bin/env python3

from Blinker.Blinker import Blinker, BlinkerButton, BlinkerNumber, BlinkerMIOT, BlinkerText
from Blinker.BlinkerConfig import *
from Blinker.BlinkerDebug import *
import re
import socket
import struct
from time import sleep

auth = 'Private Key' #Enter your private Key

BLINKER_DEBUG.debugAll()

Blinker.mode("BLINKER_WIFI")
Blinker.miotType('BLINKER_MIOT_OUTLET')
Blinker.begin(auth)

#檢查mac地址
def check_mac(mac_addr):
    #長度檢查
    if len(mac_addr) == 12:
        pass
    elif len(mac_addr) == 17:
        mac_addr = mac_addr.replace(':', '')
    else:
        return False
    #正則檢查
    pattern = re.compile(r'[0-9A-Fa-f]{12}')
    result = pattern.match(mac_addr)
    if result is not None:
        return True
    else:
        return False

#Main WOL
def wake_on_lan(mac):
    if len(mac) == 12:
        pass
    elif len(mac) == 17:
        mac = mac.replace (':', '')
        mac = mac.replace('-', '')
    else:
        raise ValueError('mac地址有誤')

    if check_mac(mac):
        data = 'FFFFFFFFFFFF' + mac * 16
        byte_data = b''
        for i in range(0, len(data), 2):
            byte_dat = struct.pack('B', int(data[i: i + 2], 16))
            byte_data = byte_data + byte_dat
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(byte_data, ('192.168.1.255', 9)) #If your IP is 192.168.0.x, change to 192.168.0.255
        sock.close()
    else :
        raise ValueError('mac地址有誤')

button1 = BlinkerButton("btn-abc")
button2 = BlinkerButton("btn-2")
text1 = BlinkerText("tex-abc")
number1 = BlinkerNumber("num-abc")

counter = 0
state_tmp = ''
oState = 'on'

def miotPowerState(state):
    ''' '''

    global oState

    BLINKER_LOG('need set power state: ', state)

    oState = state

    BlinkerMIOT.powerState(state)
    BlinkerMIOT.print()
    wake_on_lan('MAC-address') #Main WOL，Change MAC-address

def miotQuery(queryCode):
    ''' '''

    global oState

    BLINKER_LOG('MIOT Query codes: ', queryCode)

    if queryCode == BLINKER_CMD_QUERY_ALL_NUMBER :
        BLINKER_LOG('MIOT Query All')
        BlinkerMIOT.powerState(oState)
        BlinkerMIOT.print()
    elif queryCode == BLINKER_CMD_QUERY_POWERSTATE_NUMBER :
        BLINKER_LOG('MIOT Query Power State')
        BlinkerMIOT.powerState(oState)
        BlinkerMIOT.print()
        
    else :
        BlinkerMIOT.powerState(oState)
        BlinkerMIOT.print()

def button1_callback(state):
    """ """

    BLINKER_LOG('get button state: ', state)
    button1.icon('fad fa-power-off')
    button1.color('#298FCC')
    button1.text('正在開機...')
    button1.print(state)
    wake_on_lan('MAC-address') #Main WOL，Change MAC-address

def button2_callback(state):
    """ """

    BLINKER_LOG('get button state: ', state)

    button2.icon('fad fa-python')
    button2.color('#298FCC')
    button2.text('Button')
    button2.print(state)

def data_callback(data):
    BLINKER_LOG('read:', data)
    global counter
    BLINKER_LOG("Blinker readString: ", data)
    counter += 1
    number1.print(counter)

button1.attach(button1_callback)
button2.attach(button2_callback)
Blinker.attachData(data_callback)

BlinkerMIOT.attachPowerState(miotPowerState)
BlinkerMIOT.attachQuery(miotQuery)

if __name__ == '__main__':
    while True:
        Blinker.run()
        time.sleep(0.3) 
