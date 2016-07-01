Setting up a Raspberry Pi for Eaton
---

## Setting Up the Raspberry Pi

Most of the instructions can be found at: https://github.com/AlbrechtL/RPi-QEMU-x86-wine, with a few corrections. 

The command to install the image in your SD card should be:

``$ sudo dd bs=4m if=20150924_RPi-QEMU-x86-wine.img /dev/mmcblk``

Notice that the m is not capital. 

Because we're using a Raspberry Pi 1, we had to force an HDMI output in order to connect it to the TV. Change the file ``/boot/config.txt`` and add the lines:

```
hdmi_force_hotplug=1
hdmi_drive=2
```

That should give you the image with Qemu and Wine x86 installed. 

## Setting Up the SSH for Windows

In order to set up the SSH to use the raspberry pi with Windows, you need to disable (if enabled) the WiFi sharing and (re)enable it so the DHCP can work and you can get an IP address for the raspberry py. Using ``arp -a -v`` you can find the raspberry pi's ip address and use it to ssh into it. 

## Setting Up Wine

In order to run the DAM-3000 software under wine, we need to install the mfc42 dll. 
