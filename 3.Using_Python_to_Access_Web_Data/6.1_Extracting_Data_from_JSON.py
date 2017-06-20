import json
import urllib

address = raw_input('Enter location: ')
#address = 'http://python-data.dr-chuck.net/comments_42.json'
print 'Retrieving', address
uh = urllib.urlopen(address)
data = uh.read()
print 'Retrieved',len(data),'characters'


info = json.loads(data)
c = 0
s = 0

comments = info['comments']
for comment in comments:
    num = int(comment['count'])
    s += num
    c += 1
print 'Count:',c
print 'Sum:',s

