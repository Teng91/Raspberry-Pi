# 在 Raspberry Pi 上使用 OpenCV 和控制伺服馬達
## 安裝 Raspberry Pi OS
- 在 Raspberry Pi 上安裝 Raspberry Pi OS，並按照指示將其安裝到 SD 卡上
- Raspberry Pi OS安裝網址：https://www.raspberrypi.com/software/?fbclid=IwAR2pMxAf1jxRfaCY3nYxxQ5BfOIq1pbgAMoP0RnWA_-YDTPCQXECSNXVHiM
## 安裝必要的函式庫
- 在 Raspberry Pi 上安裝 OpenCV，可以使用以下命令：
```
// 安裝OpenCV
sudo apt update
sudo apt upgrade
sudo apt install python3-opencv
// 安裝 RPi.GPIO
sudo apt install python3-rpi.gpio
```
## 連接伺服馬達
- MG996R 伺服馬達有三個主要引腳：電源（通常為 5V）、接地（GND）和訊號（控制伺服馬達的 PWM 訊號）
- 將伺服馬達的訊號針腳接到 Raspberry Pi 的 GPIO 針腳（例如 GPIO 17）
- 將伺服馬達的電源針腳接到 Raspberry Pi 的 5V 針腳，並將接地針腳接到 Raspberry Pi 的 GND 針腳
