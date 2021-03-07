# Blinker_WOL
使用小米小愛音箱進行WOL，需要有樹莓派

請先去官網下載需要的庫。
https://diandeng.tech/doc/getting-start-rpi-wifi
已經在樹莓派 zero W 上測試正常運作
需要更改private key和MAC 地址。

根據官網教程安裝好程序，已經成功運行測試程序之後根據[這篇教程](https://diandeng.tech/doc/xiaoai)綁定米家app
之後把這個repo的`Xiaomi_AI_WOL.py`下載到目標樹莓派
`git clone https://github.com/SodaWithoutSparkles/Blinker_WOL/`
`cd Blinker_WOL`
`nano Xiaomi_AI_WOL.py`
更改private key 和MAC 地址，有需要的話更改broadcast address。
之後嘗試運行：`sudo python3 Xiaomi_AI_WOL.py`
關機的話，自己ssh吧。
