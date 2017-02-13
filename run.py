#!/usr/bin/python
import serial
from time import sleep
import string
import binascii
import httplib

#ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.5)

#print ser.port
#print ser.baudrate

def recv(serial):
    while True:
        data = serial.read(40)
        if data == '':
            continue
        else:
            break
        sleep(0.02)
    return str(binascii.b2a_hex(data))[0:-1]

def recv2(serial):
    data = serial.readline()
    return str(binascii.b2a_hex(data))[0:-1]


while True:
    try:
         ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.5)
    
         print ser.port
         print ser.baudrate
         data = recv(ser)
    
         if data != '':
               print data
               conn = httplib.HTTPSConnection("HomeKitProject.run.aws-usw02-pr.ice.predix.io")
               url = "https://HomeKitProject.run.aws-usw02-pr.ice.predix.io/api/field/"+data+"/location/1"
               conn.request(method="POST",url=url)
               print 'post'
               #response = conn.getresponse()
               #res= response.read()
               #print res
               conn.close()
               #ser.write(data)
        
         ser.close()
         print ser.isOpen()
         sleep(5)
    except Exception, e:
        print e
    finally:
        if conn:
            conn.close()
        if ser.isOpen():
            ser.close()
            
