Accessing the Module's web interface through the IoT router's IP
---

# Browser access

The EV Charging station has a web interface with many configuration parameters that can be changed through it.
To allow easier access to the interface while connected to the IoT router, *iptables* can be used to route HTTP connections
through the IoT router to the charging controller, so that a simple HTTP request to the IoT router's address will quickly bring up the web interface.

## IPTables setup

The following commands are required:

```
iptables -A PREROUTING -t nat -p tcp --dport 80 -j DNAT --to 192.168.123.123:80
```
