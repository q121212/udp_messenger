#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import logger

def start_server(host='192.168.0.52', port=7777):
	timeout = 600
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
		handler(received[0])
	server.close()

def handler(message):
	if message == b'Exit':
		print("Bye!\nReceived signal to Exit.")
		exit()
	if message.startswith(b'exec:'):
		try:
			eval(message[5:])
		except Exception as e:
			print("  Error occured: ", e)

if __name__ == '__main__':
	start_server('192.168.43.244')