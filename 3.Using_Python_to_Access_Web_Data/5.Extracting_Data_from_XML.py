import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
sum = 0
c = 1

while True:
    address = raw_input('Enter location: ')
    print 'Retrieving', address
    uh = urllib.urlopen(address)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    tree = ET.fromstring(data)
    lst = tree.findall('comments/comment')
    for item in lst:
        num = ('Name', item.find('count').text)
        sum = sum + int(num[1])
        c += 1
    print 'count:', c
    print "sum:", sum
    break
