Setting Up the IoT Router
---

In order to SSH into the IoT router we have to change its IP address to a static one. Once you connect the device (let's call it ``iot``) to a Windows PC, you can go to Adapter Settings and change the following configurations for the IPv4:

```
IP Address: 10.16.8.3
Netmask: 255.255.255.0
DNS: 8.8.8.8
Alt. DNS: 8.8.4.4 
``` 

By this point you can ssh into ``root@10.16.8.1`` to connect to the IoT router statically. 

After that you can go to your WiFi and change the Sharing tab settings, adding ``iot`` to the shared connection drop down.

It's usually also necessary to change the gateway address in the interfaces file on ``/etc/network`` directory to have internet connection inside the IoT router. Use vi or nano to add a line: ``gateway 10.16.8.3`` after the address line. Reboot the system ``$ reboot``.

You can now ``$ ping 8.8.8.8`` and check if the internet connection inside the router is working.