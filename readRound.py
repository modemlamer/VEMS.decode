#!/usr/bin/env python
import time
import serial
import sys
import datetime
import re


if len(sys.argv) < 3:
        print("USAGE python readRound.py [SerialPort(eg. ttyUSB0)] [fileSuffix]")
        sys.exit()



if re.match("COM[0-9]+",str(sys.argv[1])):
        portString=''
else:
        portString='/dev/'



#ttyUSB0
ser = serial.Serial(
        port=portString+str(sys.argv[1]),
        baudrate = 19200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0.1
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
FrameCount=0

with open(myfileName, 'a') as the_file:
    the_file.write('--;'+myfileName+';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\n')
    while FrameCount < 4:
        FrameCount=FrameCount+1
        x=ser.readline().encode().hex()
        #print (x)
        #print (".")
        
        byteCounter=x.__len__()
        #print("bytecounter is "+byteCounter.__str__())
        if byteCounter == 18:
                print("Startequence detected")
        
        if byteCounter == 80:
                #print("Datasequence  detected   ")
                #EGT_Str=x[10]+x[11]
                #print (x[0]+x[1])
                EGT_value=(int("0x"+x[8]+x[9], 16)*256)+(int("0x"+x[10]+x[11], 16)-50)
                EGT_v2=(int("0x"+x[8]+x[9]+x[10]+x[11], 16)-50)
                Analog0=int("0x"+x[60]+x[61]+x[62]+x[63], 16)
                Analog2=int("0x"+x[68]+x[69]+x[70]+x[71], 16)
                Vin_raw=int("0x"+x[28]+x[29]+x[30]+x[31], 16)
                Vin=_map(Vin_raw,31800,34380,1070,1150)/100
                print("Vin: "+"%.2f" % Vin+"V EGT_:v2: "+EGT_v2.__str__()+" Analog0_value: "+Analog0.__str__()+" (0..255) Analog2_value: "+Analog2.__str__()+" (0..255)")
                #the_file.write("%.2f" % Vin+';'+EGT_v2.__str__()+';'+Analog0.__str__()+';'+Analog2.__str__()+';'+'\n')
                the_file.write(
                x[0]+x[1]+';'+x[2]+x[3]+';'+x[4]+x[5]+';'+x[6]+x[7]+';'+x[8]+x[9]+';'
                +x[10]+x[11]+';'+x[12]+x[13]+';'+x[14]+x[15]+';'+x[16]+x[17]+';'+x[18]+x[19]+';'
                +x[20]+x[21]+';'+x[22]+x[23]+';'+x[24]+x[25]+';'+x[26]+x[27]+';'+x[28]+x[29]+';'
                +x[30]+x[31]+';'+x[32]+x[33]+';'+x[34]+x[35]+';'+x[36]+x[37]+';'+x[38]+x[39]+';'
                +x[40]+x[41]+';'+x[42]+x[43]+';'+x[44]+x[45]+';'+x[46]+x[47]+';'+x[48]+x[49]+';'
                +x[50]+x[51]+';'+x[52]+x[53]+';'+x[54]+x[55]+';'+x[56]+x[57]+';'+x[58]+x[59]+';'
                +x[60]+x[61]+';'+x[62]+x[63]+';'+x[64]+x[65]+';'+x[66]+x[67]+';'+x[68]+x[69]+';'
                +x[70]+x[71]+';'+x[72]+x[73]+';'+x[74]+x[75]+';'+x[76]+x[77]+';'+x[78]+x[79]+';'
                +'\n')

        

        #print (x.__len__())
        #time.sleep(0.2)
        ser.write({0x41})
        #0