#!/usr/bin/env python
#coding:utf8

import os
import socket

#stdin = os.fdopen(0)
#stdout = os.fdopen(1)
#stderr = os.fdopen(2)

fd = os.fdopen(3)
server = socket.fromfd(fd.fileno(), socket.AF_INET, socket.SOCK_STREAM)
server.listen(1)
conn, addr = server.accept()

print 'Connected by', addr
while 1:
    data = conn.recv(128)
    if not data: break
    conn.sendall(data)

conn.close()

