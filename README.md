# Raspberry Pi TV Remote

## Installation

1. `sudo apt-get update`
1. `sudo apt-get upgrade`
1. `sudo apt-get install lirc`
1. Add following lines to `/etc/modules`

    ```
    lirc_dev
    lirc_rpi gpio_out_pin=22 gpio_in_pin=18
    ```

1. Add following lines to `/etc/lirc/hardware.conf`

    ```
    LIRCD_ARGS="--uinput"
    LOAD_MODULES=true
    DRIVER="default"
    DEVICE="/dev/lirc0"
    MODULES="lirc_rpi"
    LIRCD_CONF=""
    LIRCMD_CONF=""
    ```

1. Add the following line to `/boot/config.txt`

    ```
    dtoverlay=lirc-rpi,gpio_in_pin=18,gpio_out_pin=22
    ```

1. `sudo reboot`

## Useful Guides

* [Basic Diode Circuit and Test Script](http://www.raspberry-pi-geek.com/Archive/2015/10/Raspberry-Pi-IR-remote)
* [IR Diode and Receiver Schematics](http://alexba.in/blog/2013/06/08/open-source-universal-remote-parts-and-pictures/)
* [Setting up LIRC on the Raspberry Pi](http://alexba.in/blog/2013/01/06/setting-up-lirc-on-the-raspberrypi/)
* [Hardware Schematic for New Remote Learning](https://learn.adafruit.com/using-an-ir-remote-with-a-raspberry-pi-media-center/hardware)
* [Software Guide for New Remote Learning (using `irrecord`)](http://www.ocinside.de/html/modding/linux_ir_irrecord_guide.html)

