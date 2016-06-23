Installing a GUI on the IoT Router
---

It's actually very straighforward to add a GUI to the router. First, you need to update apt by using:

``$ apt-get update``

And then to install the GUI, we used the command:

``$ apt-get -y install xorg lightdm xfce4 tango-icon-theme gnome-icon-theme``

Wait until the command is finished (additionally you can add ``firefox`` to the apt-get above to install a browser); you can then ``$ reboot`` the system. At this point the GUI is installed, but it won't run automatically if you plug the IoT router to the TV. 

You'll have to ssh into the router, and use the command ``$ startx`` to run the GUI. You can then connect the HDMI cable and see that the GUI is installed and working.

You can add a ``startx`` line to the end of ``/etc/rc.local`` to run the GUI automatically, however it will always boot as root. 