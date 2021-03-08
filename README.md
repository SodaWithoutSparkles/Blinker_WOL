# Blinker_WOL
使用小米小爱音箱进行WOL，需要有树莓派

请先去[官网](https://diandeng.tech/doc/getting-start-rpi-wifi)下载需要的库。
已经在树莓派 zero W 上测试正常运作。

**需要更改private key和MAC 地址。**

根据官网教程安装好程序，已经成功运行测试程序之后根据[这篇教程](https://diandeng.tech/doc/xiaoai)绑定米家app，
之后把这个repo的`Xiaomi_AI_WOL.py`下载到目标树莓派。

```
git clone https://github.com/SodaWithoutSparkles/Blinker_WOL/
cd Blinker_WOL
nano Xiaomi_AI_WOL.py
```
更改private key 和MAC 地址，有需要的话更改broadcast address。(第9, 52, 77, 107行)
MAC地址的格式是FF-FF-FF-FF-FF-FF

之后尝试运行：
```
sudo python3 Xiaomi_AI_WOL.py
```
关机的话，自己ssh吧。
可以配合`cpulimit`限制cpu usage。
# Blinker_WOL
使用小米小愛音箱進行WOL，需要有樹莓派

請先去[官網](https://diandeng.tech/doc/getting-start-rpi-wifi)下載需要的庫。
已經在樹莓派 zero W 上測試正常運作。

**需要更改private key和MAC 地址。**

根據官網教程安裝好程序，已經成功運行測試程序之後根據[這篇教程](https://diandeng.tech/doc/xiaoai)綁定米家app，
之後把這個repo的`Xiaomi_AI_WOL.py`下載到目標樹莓派。

```
git clone https://github.com/SodaWithoutSparkles/Blinker_WOL/
cd Blinker_WOL
nano Xiaomi_AI_WOL.py
```
更改private key 和MAC 地址，有需要的話更改broadcast address。(第9, 52, 77, 107行)
MAC地址的格式是FF-FF-FF-FF-FF-FF
之後嘗試運行：
```
sudo python3 Xiaomi_AI_WOL.py
```
關機的話，自己ssh吧。
可以配合`cpulimit`限制cpu usage。
