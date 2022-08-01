#!/usr/bin/python3

import socket


HOST = '127.0.0.1'
PORT = 7777

# af_inet --> connecting over ipv4
# sock_stream --> port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
