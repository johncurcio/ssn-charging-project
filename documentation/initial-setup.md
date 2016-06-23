Eluminocity Charging Module
---

# Setting up the module

In order to get the module working you will need a micro USB cable to connect the EV charging station to the IoT router or to your computer. 

Once hooked up, the configuration page for the charging station is accessible via a web browser: http://192.168.123.123/ 

You can also access the state of the charging module with http://192.168.123.123/rest/full_state

You can also SSH into the device by using the username root and password root under the ip 192.168.123.123

## Windows configuration

If you're using a machine with Windows, you may need to install a RNFDIS Ethernet Driver (we didn't have to on Windows 10). The Driver can be found at: http://www.driverscape.com/download/rndis-ethernet-gadget 

Further instructions for setting up the device are at: https://github.com/ev3dev/ev3dev/wiki/Setting-Up-Windows-USB-Ethernet-Networking

## Unix Configuration

Mac most likely won't need any configuration, you may find it necessary for Linux, however.

### IoT Router

After connecting to the IoT router, the charging station may be under the name ``virbr0`` if you type ``ifconfig`` on the terminal. This will make it impossible to connect to the charging module, you need to disable ``virbr0`` on Linux, and change it to ``usb0``.

Use ``ifconfig virbr0 down`` to disable it and ``ifconfig usb0 192.168.123.123`` to add the IP address to usb0 and add usb0 to the list. All is detailed at: https://github.com/ev3dev/ev3dev/wiki/Setting-Up-Linux-USB-Ethernet-Networking

This will work only once. In order to make the changes permanent, you need to change the ``/etc/network/interfaces`` and add the lines:

```
auto usb0
    iface usb0 inet static
    address 192.168.123.220
```

# Getting data

After all the set up, you can get the data from the EV charging station by using 

``wget http://192.168.123.123/rest/full_state``

This will then be used with a script to store the data that's regularly being pulled from the charging module.

