EV Charging Station Project
---

This project has two branches. The *EATON branch* and the *Eluminocity branch*. 

## Eaton Branch

There's an EATON EV Charging Station at IIT using a laptop connected to its controller running a Windows executable (DAM3000) to fetch data from the charging station and send it to the network. This project aims to replace the laptop for an IoT router and run this executable under a Linux environment inside the router. Because of incompatibilities between the x86 architecture of the executable and the ARM architecture of the Linux board inside the IoT router, we categorized this branch as unfeasible. *Edit:* We've been successful in executing the .exe in a raspberry pi with qemu and wine, but we're not sure that's a solution since the IoT router doesn't use raspberry pi.

## Eluminocity Branch 

This is a pilot project to connect a eluminocity EV charging station to an IoT router, fetch data from this charging station and store it in the IoT router to be fetched by the SSN backend. We have implemented a Python script ``eluminocity.py`` which can fetch data and store it in CSV format on the IoT router.  

### IoT Router

* [Initial Setup and Wi-Fi Sharing](docs/iot-setup.md)
* [Installing a GUI](docs/gui-guide.md)

### EATON Charging Station

* [Setting Up a Raspberry Pi for ARM to x86 Emulation](docs/eaton-raspberry.md)
* [Feasibility Report](docs/eaton-feasibility.md)

### Eluminocity Charging Station

* [Initial Setup of the Charging Module](docs/eluminocity-setup.md)
* [Sharing the IoT Router Internet with the Module](docs/eluminocity-internet.md)
* [Accessing the Module's web interface through the IoT router's IP] (docs/eluminocity-browser.md)

### Next Steps

* [Use OCPP 1.5 to extract more data from the eluminocity charger](docs/eluminocity-next.md)
* [Finish setting up the Raspberry Pi image and connect it to the IoT Router](docs/eaton-next.md)
