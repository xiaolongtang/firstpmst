#!/usr/bin/python
import serial
from time import sleep
import string
import binascii
import httplib

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.5)

print ser.port
print ser.baudrate

conn = httplib.HTTPConnection("192.168.1.108",8080)

def recv(serial):
    while True:
        data = serial.readline()
        if data == '':
            continue
        else:
            break
        sleep(0.02)
    return str(binascii.b2a_hex(data))[0:-1]


while True:
    data = recv(ser)
    if data != '':
        print data
        url = "http://192.168.1.108:8080/api/field/"+data+"/location/1"
        conn.request(method="POST",url=url)
        response = conn.getresponse()
        res= response.read()
        print res
        #ser.write(data)
