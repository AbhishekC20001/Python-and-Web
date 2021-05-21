'''import re
numlist=[]
handle=open('regex_sum_502192.txt','r')
for line in handle:
    line=line.rstrip()
    stuff=re.findall('[0-9]+',line)
    if len(stuff)==0 :
        continue

    for i in range(len(stuff)):

        num=float(stuff[i])
        numlist.append(num)

ans=sum(numlist)
print(ans)'''


'''import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()'''


'''# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
lst=[]
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)

    num=int(tag.contents[0])
    lst.append(num)

print(sum(lst))    '''



'''# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
url = input('Enter - ')
count=int(input("Enter count:"))
pos=int(input("Enter position:"))

for i in range(count):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')


    # Retrieve all of the anchor tags
    tags = soup('a')
    i=0
    for tag in tags:
        if i == pos-1:
            print(tag.get('href', None))
            url=tag.get('href', None)
        i+=1
        #print(tag.get('href', None))
        #print('TAG:', tag)
        #print('URL:', tag.get('href', None))
        #print('Contents:', tag.contents[0])
        #print('Attrs:', tag.attrs)'''



'''import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input('Enter - ')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = urllib.request.urlopen(url, context=ctx).read()
#print(data)

tree = ET.fromstring(data.decode())
#print(tree)
results = tree.findall('comments/comment')
#counts = tree.findall('.//count')
print(results)


lst=[]
for item in results:
    #print(item.find('count').text)
    num=int(item.find('count').text)
    lst.append(num)
print(sum(lst))     '''



'''lat = results[0].find('').find('location').find('lat').text
lng = results[0].find('geometry').find('location').find('lng').text
location = results[0].find('formatted_address').text

print('lat', lat, 'lng', lng)
print(location)'''






import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=2))
    info = json.loads(data)
    for item in info['results']:
        print(item['place_id'])

    '''lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)'''
