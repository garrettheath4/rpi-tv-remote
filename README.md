# Raspberry Pi Auto TV IR Controller

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

