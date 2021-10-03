#!/usr/bin/env python
import time
import serial

ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate = 19200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)



while 1:


        x=ser.readline().hex()
        print (x)
        print (".")
        byteCounter=x.__len__()
        print("bytecounter is "+byteCounter.__str__())
        if byteCounter == 18:
                print("Startequence detected")
        
        if byteCounter == 80:
                print("Datasequence  detected")

        

        #print (x.__len__())
        time.sleep(2)
        ser.write({0x41})
        0