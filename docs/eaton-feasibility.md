Feasibility Report for EATON Charger
---

## Problem Statement

The EATON charging station next to McCormick Tribune Campus Center is currently running a DAM3000[1] executable file to extract meter data from its hardware and send it over the network. In order to run this file, the charging station uses a Windows laptop connected to a wireless connection and it is attached to the station.

This project aims to replace the connected laptop with an SSN IoT router running the same executable file under a Linux environment. In order to achieve that, we proposed three solutions:

1.	**Wine:** Use Wine to run the Executable file under Linux
2.	**Qemu + Wine:** Use Qemu to run Wine and Wine to run the Executable
3.	**x86 board:** Use a different board in the IoT router with x86 architecture and Wine to run the executable. 

### Wine

In this solution we proposed to install Wine in the IoT router, which already had a Linux environment, and run the executable using Wine. This solution is unfeasible. 

The Linux board that’s shipped with the IoT router uses a processor with ARM architecture. However, the executable file we need to run is compiled under a x86 architecture, as most Windows executables are, and thus it cannot be run on another architecture without using some sort of translator or recompiling the entire source code of the executable in ARM. 

Because we don’t have the source code, recompiling the executable file is impossible. And Wine is not an emulator, therefore it cannot run the file cross architectures – we can’t run Wine for x86 on the board, and Wine for ARM does not run executables for x86. Hence, this option cannot be carried out and was dismissed as unfeasible. 

To address this problem we decided to try to use a translator/emulator, namely Qemu, to convert the x86 code to ARM in runtime. That’s the second option. 

### Qemu + Wine

The idea of this solution is to install Qemu under the Linux environment on the router, and because Qemu is an emulator, we can install a lightweight Linux distro, such as Puppy Linux which uses the x86 architecture, install Wine for x86 in Puppy and run the executable with Wine. Since everything inside Qemu is running in x86, and Qemu is translating the x86 code to ARM, we believe that the executable will run successfully. We may also try to run Wine directly on Qemu, if we can get a binary of Wine. Or try to install Windows on Qemu directly, however there’s the problem of a paid license for Windows and it is usually slower. 

The main problem with this solution is performance. We’re guessing that this will run very slowly, if at all. We’ve already installed a GUI and Qemu on the IoT router, and now we’re trying to emulate Wine in Qemu, but have made no further progress. 

We’re going to carry out for a few more days with this option, but mostly to assess its performance. In case the performance is acceptable, we’re using this as a solution for the problem proposed, if not we’re deeming this option as unfeasible as well. 

### x86 Board

The last solution and the one we think it would be more appropriate is to replace the ARM board we have on the IoT router with a x86 one. 

With an x86 processor, any Linux partition can run Wine (solution 1) and Wine can run the executable file. Or it can even run Windows, and Windows would run natively the executable file. 

The main concern with this approach is price. ARM boards are inexpensive and easy to find; the same thing is not true for x86 boards. Furthermore, there are no immediate plans to create x86 compatible IoT routers by SSN. And we have the risk, even if small, that there’s not much capacity in the board to run the executable file with a good performance, if at all. Thus this approach has not been pursued further.  


## Conclusion

With all that said, we still believe it’s possible to replace the laptop with an IoT router, but we may have to either recreate the executable file into an ARM Linux binary or to replace the IoT router boards with x86 boards, which are not feasible at the moment. Using software (Qemu and Wine) may be extremely slow, if we can actually run it. For the time being, we’re considering this project to be unfeasible, but we’re still running tests on Qemu to be sure the performance is as bad as expected. 





 
[1] DAM3000 executable can be found at http://www.art-control.com/englishs/products/ProductShow.asp?ID=150 in the file DAM3000.rar
