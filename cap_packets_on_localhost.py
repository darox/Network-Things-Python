#!/usr/bin/python3.8
#Pyshark will only work, if tshark is installed on the system
import pyshark
from os import sys



interface = 'Loopback'
CapFilter = 'tcp port 65432'
#Setup capture on localhost
cap = pyshark.LiveCapture(interface=interface, bpf_filter=CapFilter)


#Run continous packet tracing
for packet in cap.sniff_continuously():
    #Print captured packets to shell
    print(packet)