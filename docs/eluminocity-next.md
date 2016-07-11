Use OCPP 1.5 to extract more data from the eluminocity charger
--

We have received instructions from eluminocity saying that in order to extract more information from the charging station we would

"need to implement a backend system according to this [OCPP 1.5] specification. Once you have that, you configure the station for SOAP based OCPP and point it to your backend system. This entity is then able to send ``GetConfiguration`` commands to the charger. The charger will report its address to this backend system with every message."

Due to time constraints, implementing a full backend was not possible, but we believe that it can be done. However we're not sure if the backend would be as reliable as the one being used now.  

We have also found a few implemented backend systems online, but they were all Windows x86 apps and that's not compatible with the IoT router at the moment. 