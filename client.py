#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
import sys

HOST = '192.168.43.244'
PORT = 7777

def input_message():
	host = HOST
	port = PORT
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	while True:
		msg = input('Enter message to send: ')
		client.sendto(msg.encode('utf-8'), (host, port))
		d = client.recvfrom(102400)
		reply = d[0]
		addr = d[1]
		# print(d)
		print (" Server reply:\t" + reply.decode('utf-8'))
		
	client.close()

def send_message(message):
	'''Analogue for bash command: echo -n "hello" >/dev/udp/192.168.0.52/7777 '''
	host = HOST
	port = PORT
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	msg = message
	client.sendto(msg.encode('utf-8'), (host, port))
	d = client.recvfrom(1048576)
	reply = d[0]
	addr = d[1]
	# print(d)
	print (" Server reply:\t" + reply.decode('utf-8'))
		
	client.close()

if __name__ == '__main__':
	x=0
	ext_param = ''
	try:
		ext_param = sys.argv[1]
	except:
		pass

	while True:
		x+=1
		send_message(ext_param + '_' + str(x))
	# input_message()