import csv
import urllib2
import os
import sys
from BeautifulSoup import BeautifulSoup
# or if you're using BeautifulSoup4:
# from bs4 import BeautifulSoup

soup = BeautifulSoup(open("pathtofile").read())


t = soup.findAll('table')

f = open(os.path.expanduser("~/Desktop/AmnestyScrape.txt"), 'w')

sys.stdout = f

for row in soup('table', {'class': 'confluenceTable'})[0].tbody('tr'):
    tds = row('td')
    print tds[0].find(text=True).encode('utf-8)'), ",",
    for li in tds[3].findAll('li'):
        print li.text.encode("utf-8"), ";",
    print "\n"
