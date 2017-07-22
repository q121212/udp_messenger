#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import logger

timeout = 600
host = '192.168.0.52'
port = 7777
addr = (host, port)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(addr)

print ('Waiting for data ({0} seconds)...'.format(timeout))
while True:
	server.settimeout(timeout)
	try:
		d = server.recvfrom(1048576)
	except socket.timeout: 
		print('Time is out. {0} seconds have passed'.format(timeout))
		break
	received = d
	addr = d[1]
	print ('Received data: ' , received)
	logger.insert_text(str(received[0]) + ' ' + str(received[1]))
	msg = "The message was received.".format(received[0])
	server.sendto(msg.encode('utf-8'), addr)
server.close()