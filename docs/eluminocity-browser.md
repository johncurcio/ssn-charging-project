How to configure the EV Charging Controller web interface to be accessible through HTTP
---

# Browser access

The EV Charging station has a web interface for configuration, with many parameters that can be changed through it.
To make it easier to access that interface while connected to the IoT router, *iptables* can be used to route HTTP connections
through the IoT router to the charging controller, so that a simple HTTP access using a browser to the IoT router's address
will quickly bring up the web interface.

## IPTables setup

The following commands are required:

```
iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 80 -j DNAT --to 192.168.123.123:80
iptables -A FORWARD -p tcp -d 192.168.123.123 --dport 80 -j ACCEPT
```

Where 'eth0' can be changed to whatever interface the IoT router is being connected to through.
