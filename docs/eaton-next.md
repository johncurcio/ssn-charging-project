Finish setting up the Raspberry Pi image and connect it to the IoT Router
--

We have managed to run the DAM-3000M software on a raspberry pi, which successfully emulates an x86 windows app on a ARM linux board. Nevertheless, we have a few issues with that:

1. The chinese fonts in the windows app are not supported, they have to be added.
2. The raspberry pi uses an 8GB image, which far surpasses the capacity of the IoT router, therefore we cannot simply port this image to the IoT. We can either try a new solution or simply to connect the raspberry pi to the IoT router. 
3. We can only run one version of the DAM-3000 software, which is in chinese and it is portable. Any attempts to install the english version have failed. 
4. The portable chinese version that we're porting to the raspberry pi is no longer being used in the EATON charger, and therefore it may not be compatible with it. 
5. Tests with the actual charger have not been successful so far. 