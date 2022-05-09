#!/usr/bin/env python
import time
import serial
import sys

#ttyUSB0
ser = serial.Serial(
        port='/dev/'+str(sys.argv[1]),
        baudrate = 19200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0.5
)

#  Prominent Arduino map function :)
def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
	

y = datetime.datetime.now()
#print(y.strftime("%Y-%m-%d-%H%M%S")) 
myfileName=y.strftime("%Y-%m-%d-%H%M%S")+'-VEMS-Bytelog-'+str(sys.argv[2])+'.csv'
EGT_Str=""
EGT_value=0
EGT_v2=0
Analog0=0
Analog2=0
Vin_raw=0
Vin=0

with open('somefile.txt', 'a') as the_file:
    while 1:


        x=ser.readline().hex()
        print (x)
        #print (".")
        byteCounter=x.__len__()
        #print("bytecounter is "+byteCounter.__str__())
        if byteCounter == 18:
                print("Startequence detected")
        
        if byteCounter == 80:
                #print("Datasequence  detected   ")
                #EGT_Str=x[10]+x[11]
                EGT_value=(int("0x"+x[8]+x[9], 16)*256)+(int("0x"+x[10]+x[11], 16)-50)
                EGT_v2=(int("0x"+x[8]+x[9]+x[10]+x[11], 16)-50)
                Analog0=int("0x"+x[60]+x[61]+x[62]+x[63], 16)
                Analog2=int("0x"+x[68]+x[69]+x[70]+x[71], 16)
                Vin_raw=int("0x"+x[28]+x[29]+x[30]+x[31], 16)
                Vin=_map(Vin_raw,31800,34380,1070,1150)/100
                print("Vin: "+"%.2f" % Vin+"V EGT_:v2: "+EGT_v2.__str__()+" Analog0_value: "+Analog0.__str__()+" (0..255) Analog2_value: "+Analog2.__str__()+" (0..255)")
                the_file.write("%.2f" % Vin+';'+EGT_v2.__str__()+';'+Analog0.__str__()+';'+Analog2.__str__()+';'+'\n')
        

        #print (x.__len__())
        #time.sleep(0.2)
        #ser.write({0x42, 0x43})
        ser.write({0x41})
        #0