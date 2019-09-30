#!/usr/bin/python
import socket
DEFAULT_TIMEOUT = 1.0
HOST = '192.168.1.101'
PORT = 63351 # The same port as used by the server
FILENAME = "DataStream.csv"

def start_sensor(host,port, filename):
	print ("Connecting to " + host)
	try:
	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
	    s.settimeout(DEFAULT_TIMEOUT)
	    s.connect((HOST, PORT))
	    f = open (FILENAME, "w")
	    try:
		print("Writting in DataStream.csv, Press ctrl + c to stop")
		while (1):
		    data = s.recv(1024)
		    data = data.replace("(","")
		    data = data.replace(")","\n")
		    #print(data)
		    f.write(data)
	    except KeyboardInterrupt:
		f.close
		s.close
	except:
	    print ("No connection")

start_sensor(HOST, PORT, FILENAME)
