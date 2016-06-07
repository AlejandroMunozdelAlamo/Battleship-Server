#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

# Battleship Game Server
# Abel Castilla Rodríguez, Alejandro Muñoz Del Álamo, Damián Nimo Járquez
# Copyright © 2016

# sys.argv[1];
# sys.argv[2];


import socket 
import sys


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
	tirada = sys.argv[1];
	cadena = sys.argv[2];

	print >> sys.stderr, 'sending "%s"' % cadena
	sock.sendall(tirada)


finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
