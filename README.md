# Raspberry Pi TV Remote

This project aims to turn a Raspberry Pi with a touchscreen into a universal
remote for one or more devices (like a TV, cable box, and Apple TV).
The Raspberry Pi will control devices by sending IR signals and/or CEC frames (if the device to be controlled is connected via HDMI).
The touchscreen will display big buttons (as few as possible, for simplicity)
that users can simply press to perform a few commands, such as:

* _Power on/off_ – Turn the TV on or off
* _Mute_ - Mute the TV
* _Volume up_ - Turn up the TV volume
* _Volume down_ - Turn down the TV volume
* _Watch CNN_
    1. Turn on the TV
    1. Turn on the cable box
    1. Set the cable box as the active input on the TV
    1. Change the channel on the cable box to CNN
* _Google Hangouts_
    1. Turn on the TV
    1. Turn on (or wake up, if possible) the _Google Chromebox for Meetings_ device
    1. Set the Chromebox as the active input on the TV
* _Watch News Feed_
    1. Turn on the TV
    1. Turn on the device that is streaming news videos from the internet (e.g. a Raspberry Pi using the [rpi-chrome-display] project; might be the same Rasbperry Pi as the one running this *rpi-tv-remote* project)
    1. Set the news feed device as the active input on the TV


## Installation


### Summary

At its core, this project is designed to run on a Raspberry Pi 3 Model B
running the Raspbian Stretch operating system. Some hardware is required to
allow the Raspberry Pi to send IR signals and a touchscreen display is required
to allow user input. (If you're starting from scratch, all of the hardware
including the Raspberry Pi should cost less than $200.) This project then uses
the *lirc* library to send (and optionally receive) IR data.


### Requirements

* Hardware
    * Raspberry Pi 3 Model B ([Amazon][RPi])
    * MicroSD card with at least 8 GB of storage ([Amazon][mSD])
    * MicroSD card adapter (some way to connect a MicroSD card to your laptop/desktop)
        * Either MicroSD to SD adapter (if your computer has an SD card slot) OR MicroSD to USB adapter ([Amazon][mSdAdapter])
    * Micro-USB charging cable to power Raspberry Pi
    * USB power supply (ideally with two 5V 2.4A ports) ([Amazon][Power])
    * Heatsinks for Raspberry Pi ([Amazon][Heatsinks])
    * IR LED diode ([Amazon][Blaster])
    * TO-92 NPN power transistor (electrical component) ([Amazon][Transistor])
    * Resistor ([Amazon][Resistor])
    * IR sensor (optional, for learning new remote's IR codes) ([Amazon][Sensor])
    * Small insulated wires and/or Raspberry Pi jumper wires ([Amazon][Jumpers])
    * Small breadboard (15 by 10)
    * 7-inch touchscreen for Raspberry Pi ([Amazon][Screen])
    * Wall-mountable case for touchscreen and Raspberry Pi ([Amazon][Case])
* Software
    * Raspbian Stretch operating system with GUI
    * Software for writing Raspbian to MicroSD card (see Raspberry Pi guides for details)
    * LIRC library and software (see below for how to install)
    * Git software (see below for how to install)


### Hardware Setup

1. Install Raspbian operating system on MicroSD card and put card in Raspberry Pi
1. Plug monitor into HDMI port (or you can use the Raspberry Pi touchscreen) and plug in USB keyboard and (optional) mouse
1. Connect electrical components to GPIO pins and breadboard according to [this schematic diagram](https://upverter.com/alexbain/f24516375cfae8b9/Open-Source-Universal-Remote/)
    * The schematic is embedded and linked at the bottom of this README as well.
    * Yes, you will have to learn how to read a schematic. But don't worry, this is a pretty simple one.
    * **Note:** The "IR Receiver" part of the schematic is optional since it is only needed if your remote's IR codes (i.e. for your TV remote) are not listed in the [LIRC remote repository](http://lirc.sourceforge.net/remotes/).
1. After the software is set up (see below), connect the touchscreen to the Raspberry Pi and put the screen and Raspberry Pi into the case.
    * The IR LED diode (and presumably the breadboard it is connected to) should be outside of the case and positioned in such a way that it is within line of sight of all of the IR sensors of all of the devices that you want to control.


### Software Configuration

1. Follow guides on Raspberry Pi project website to login to the Raspberry Pi (using monitor and keyboard)
1. Set password for default `pi` user
1. Make sure you cannot log in as `root` user without a password
1. Run `sudo raspi-config` to set the hostname to something memorable so you can more easily access your Raspberry Pi over the network
1. Connect Raspberry Pi to a wired Ethernet network and/or Wi-Fi (see guides on Raspberry Pi website)
1. Enable remote SSH login (optional but recommended)
1. Update all of the software on the Raspberry Pi by running the following commands:

    ```
    sudo apt-get update
    sudo apt-get upgrade
    ```

1. Install the LIRC library and software: `sudo apt-get install lirc`
1. Add following lines to `/etc/modules`

    ```
    lirc_dev
    lirc_rpi gpio_out_pin=22 gpio_in_pin=23
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
    dtoverlay=lirc-rpi,gpio_out_pin=22,gpio_in_pin=23
    ```

1. Restart the Raspberry Pi to apply the configuration changes: `sudo reboot`
1. Install Git so you can download this project's files to the Raspberry Pi: `sudo apt-get install git`
1. Generate an SSH keypair to enable passwordless authentication when downloading files from GitHub: `ssh-keygen -t rsa -C "pi@$(hostname)"`
    * **Note:** When the utility runs, press `Enter` three times (without typing any answer to its questions) to accept the default file location and to not set a password for the SSH keys.
1. Run `cat ~/.ssh/id_rsa.pub` to print the public key to your screen and then copy the key to your clipboard.
1. On a web browser (on your laptop/desktop computer), log in to GitHub as an admin of the *rpi-tv-remote* repository and go to [https://github.com/garrettheath4/rpi-tv-remote/settings/keys][rpi-tv-remote]
1. Make sure *Allow write access* is unchecked, paste the key into the *Key:* field, and click **Add key**.
1. Back in a terminal on your Raspberry Pi, clone this project to the Raspberry Pi: `git clone git@github.com:garrettheath4/rpi-tv-remote.git`
1. Switch your current directory to the directory containing the newly-cloned project files: `cd rpi-tv-remote`
1. Add the remote codes to the LIRC configuration file so that LIRC knows how to communicate with your device(s): `sudo cp -i remote_kitchen_tv.conf /etc/lirc/lircd.conf`
    * **Note:** This will overwrite whatever LIRC configurations you already have. If you have never used LIRC before on this Raspberry Pi, then they will probably be blank anyway and so it is safe to do this.
    * **Note:** After updating the LIRC configuration, you might need to restart the LIRC service with `sudo service lirc restart` or reboot the Raspberry Pi with `sudo reboot` for the changes to go into effect.


## Features and TODO

- [ ] Use simple web app to display buttons and trigger corresponding IR signal(s) if a button is pressed
- [ ] Add support for controlling TV over HDMI-CEC (instead of or in addition to IR signals)
- [ ] Send a remote "dummy button" IR signal to TV to delay the TV's auto-shutoff feature and keep it on during the day (6am to 6pm)


## Useful Guides

Most of this project is based off of Raspberry Pi guides I have found on the
Internet. Hardly any of this project is original; I just put it all together. I
had no idea how to even wire up components on a breadboard before I read these
guides. They deserve all of the credit, really. Here they are:

* [Basic Diode Circuit and Test Script](http://www.raspberry-pi-geek.com/Archive/2015/10/Raspberry-Pi-IR-remote)
* [IR Diode and Receiver Schematics](http://alexba.in/blog/2013/06/08/open-source-universal-remote-parts-and-pictures/)
* [Setting up LIRC on the Raspberry Pi](http://alexba.in/blog/2013/01/06/setting-up-lirc-on-the-raspberrypi/)
* [Hardware Schematic for New Remote Learning](https://learn.adafruit.com/using-an-ir-remote-with-a-raspberry-pi-media-center/hardware)
* [Software Guide for New Remote Learning (using `irrecord`)](http://www.ocinside.de/html/modding/linux_ir_irrecord_guide.html)


## Electrical Components Schematic

[![Open Source Universal Remote by alexbain f24516375cfae8b9 - Upverter](https://upverter.com/alexbain/f24516375cfae8b9/Open-Source-Universal-Remote/embed_img/13715285520000/)](https://upverter.com/alexbain/f24516375cfae8b9/Open-Source-Universal-Remote/#/)



<!-- Links -->
[rpi-chrome-display]: https://github.com/garrettheath4/rpi-chrome-display
[RPi]: http://a.co/8ERP4JK
[mSD]: http://a.co/dy1cmUz
[mSdAdapter]: http://a.co/iw1fmFy
[Power]: http://a.co/29xvK5r
[Heatsinks]: http://a.co/3chb4mt
[Blaster]: http://a.co/c04rJoF
[Transistor]: http://a.co/8UZ98Zf
[Resistor]: http://a.co/iBo8F9I
[Sensor]: http://a.co/ghllctE
[Jumpers]: http://a.co/f5Srtso
[Screen]: http://a.co/4cBsHMT
[Case]: http://a.co/eCyVvB3
[rpi-tv-remote]: https://github.com/garrettheath4/rpi-tv-remote/settings/keys