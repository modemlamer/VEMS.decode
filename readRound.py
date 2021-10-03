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

EGT_Str=""
EGT_value=0
EGT_v2=0
Analog0=0
Analog2=0


while 1:


        x=ser.readline().hex()
        print (x)
        print (".")
        byteCounter=x.__len__()
        print("bytecounter is "+byteCounter.__str__())
        if byteCounter == 18:
                print("Startequence detected")
        
        if byteCounter == 80:
                print("Datasequence  detected   ")
                #EGT_Str=x[10]+x[11]
                EGT_value=(int("0x"+x[8]+x[9], 16)*256)+(int("0x"+x[10]+x[11], 16)-50)
                EGT_v2=(int("0x"+x[8]+x[9]+x[10]+x[11], 16)-50)
                Analog0=int("0x"+x[60]+x[61]+x[62]+x[63], 16)
                Analog2=int("0x"+x[68]+x[69]+x[70]+x[71], 16)
                print("EGT_:v2: "+EGT_v2.__str__()+" Analog0_value: "+Analog0.__str__()+" (0..255) Analog2_value: "+Analog2.__str__()+" (0..255)")

        

        #print (x.__len__())
        time.sleep(2)
        ser.write({0x41})
        0