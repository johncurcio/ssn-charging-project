Sharing the IoT Router's Connection to the Internet with the Charging Module
---

SSH into the IoT router from your computer and then SSH into the charger using the IoT router's terminal. On the charger terminal type:

``$ ip route add default via 192.168.123.220``

Then on the IoT router terminal window type:

```
$ iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
$ iptables -A FORWARD -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
$ iptables -A FORWARD -i usb0 -o eth0 -j ACCEPT
```

This will share the connection from the IoT router with the Charging Module, assuming the IoT router has an internet connection already estabilshed. You can now ``$ ping`` to check the internet connection on the charging module.