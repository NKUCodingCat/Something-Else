#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:		basic_dump.py
#
# Author:	  Massimo Ciani
#
# Created:	 01/09/2009
# Copyright:   (c) Massimo Ciani 2009
#
#-------------------------------------------------------------------------------
from winpcapy import *
import time,SR
import sys,os
import string
import platform
import re
fcode = bpf_program()
NetMask = 0xffffff
filter = "dst host zzxx.nankai.edu.cn"
#from ctypes import *
def Listen():

	LINE_LEN=16
	if platform.python_version()[0] == "3":
		raw_input=input
	#/* prototype of the packet handler */
	#void packet_handler(u_char *param, const struct pcap_pkthdr *header, const u_char *pkt_data);
	PHAND=CFUNCTYPE(None,POINTER(c_ubyte),POINTER(pcap_pkthdr),POINTER(c_ubyte))
	header=POINTER(pcap_pkthdr)()
	pkt_data=POINTER(c_ubyte)()
	## Callback function invoked by libpcap for every incoming packet
	def _packet_handler(param,header,pkt_data):
		## convert the timestamp to readable format
		local_tv_sec = header.contents.ts.tv_sec
		ltime=time.localtime(local_tv_sec);
		timestr=time.strftime("%H:%M:%S", ltime)
		#print (param.contents)
		#for i in pkt_data.contents:
		#	ST += chr(i)
		
		#print("%s,%.6d len:%d" % (timestr, header.contents.ts.tv_usec, header.contents.len))
	
	NAMES =  SR.GETMAC()
	for i in range(0,len(NAMES)):
		print i+1,NAMES[i][0]
	global raw_input
	
	if (i>1 and re.match(r'^\d+$', n) and n>0 and n<i+2):
		n = raw_input("Please Input the Adapter you are using(1-%d): "%(i+1))
		name = NAMES[int(n)-1][1]
	elif (i==0):
		n = 0
		name = NAMES[0][1]
	elif(not NAMES):
		print "Adapter Not Found"
		os.system("PAUSE")
		sys.exit(-1)
	else:
		print "Input Error"
		os.system("PAUSE")
		sys.exit(-1)
	packet_handler=PHAND(_packet_handler)
	alldevs=POINTER(pcap_if_t)()
	errbuf= create_string_buffer(PCAP_ERRBUF_SIZE)
	## Retrieve the device list
	
	fp = pcap_open_live(name,65536,1,5000,errbuf)
	if (fp == None):
		print("\nUnable to open the adapter. %s is not supported by Pcap-WinPcap\n" % d.contents.name)
		## Free the device list
		pcap_freealldevs(alldevs)
		sys.exit(-1)
	print("\nlistening on %s...\n" % (NAMES[int(n)-1][0]))
	pcap_freealldevs(alldevs)
	if pcap_compile(fp,byref(fcode),filter,1,NetMask) < 0:
		print('\nError compiling filter: wrong syntax.\n')
		pcap_close(fp)
		sys.exit(-3)
	if pcap_setfilter(fp,byref(fcode)) < 0:
		print('\nError setting the filter\n')
		pcap_close(fp)
		sys.exit(-4)
	res = pcap_next_ex( fp, byref(header), byref(pkt_data))
	ST = ""
	while(True):
		if(res==-1 or res == 0):
			#print "Connection Error. Ignore it"
			continue
		if(res == -2):
			continue
		for i in range(1,header.contents.len + 1):
			if not (pkt_data[i-1]>127 or pkt_data[i-1]<33):
				ST+=chr(pkt_data[i-1])
		C = []
		C = re.findall("B\dU\d-[ABCDEF]",ST)
		res = pcap_next_ex( fp, byref(header), byref(pkt_data))
		if C:
			C += re.findall("Integrated_\d",ST)
			C += re.findall("Listening_\d",ST)
			pcap_close(fp)
			return C
		ST = ""
	