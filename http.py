import httplib

url = "http://192.168.1.108:8080/api/field/location/1"

conn = httplib.HTTPConnection("192.168.1.108",8080)
conn.request(method="POST",url=url)

response = conn.getresponse()
res= response.read()
print res

