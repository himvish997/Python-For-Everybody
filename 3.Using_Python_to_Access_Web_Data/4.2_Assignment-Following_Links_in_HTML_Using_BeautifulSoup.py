# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags


count = raw_input("Enter Count : ")
position = raw_input("Enter Position : ")
print url
for i in range(int(count)):
    tags = soup('a')
    tag = tags[int(position)-1]
    print tag.get('href', None)
    html = urllib.urlopen(tag.get('href', None)).read()
    soup = BeautifulSoup(html)

    
    

