from bs4 import BeautifulSoup
import urllib.request
import ssl
import requests
ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://www.piaotian.net/html/8/8216/'
resp = urllib.request.urlopen(url).read()
soup = BeautifulSoup(resp, 'html.parser')

f = open("WuDaoZongSi.txt",'w', encoding = 'utf-8')

title = soup.find_all("li")
for i in range(4,len(title)):
    chtitle = title[i].find_all('a', href=True)
    for t in chtitle:
        a = t['href']
        raw = 'http://www.piaotian.net/html/8/8216/'
        churl = raw + a
        b = t.text
        f.write(b + '\n')
        chrep = requests.get(churl)
        chrep.encoding = 'gb18030'
        chsoup = BeautifulSoup(chrep.text, 'html.parser')
        for i in chsoup.find_all('br'):
            f.write(i.text + '\n')
        print (b)
f.close()

print ("Export is done")
