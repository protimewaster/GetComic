from bs4 import BeautifulSoup
import urllib.request
import requests
import re

f = open('result.txt', 'w')

url = 'http://comic.sfacg.com/HTML/WZTX/'#change
resp = requests.get(url).text
soup = BeautifulSoup(resp, 'html.parser')
ul_tag = soup.find('ul', class_="serialise_list Blue_link2")
li_tag = ul_tag.findAll('li')
host = 'http://coldpic.sfacg.com/'

for li in li_tag:
    href = li.find('a', href=True)
    ch_url = "http://comic.sfacg.com" + href['href']
    if len(ch_url) == 37:
        num = re.findall("\d\d\d", ch_url)[0]
        js_url = 'http://comic.sfacg.com/Utility/1182/' + num + ".js" #change
        jsc = requests.get(js_url).text
        pic = re.findall("Pic/OnlineComic\d/WZTX/\d\d\d/\d\d\d.\d*.\w\w\w",jsc)#change
        for i in pic:
            name = re.findall("\d\d\d.\d*.\w\w\w", i)
            for b in range(len(name)):
                picurl = host + i
                f.write(picurl + '\n')
        
    else:
        num = re.findall("\d\d\d\w", ch_url)[0]
        js_url = 'http://comic.sfacg.com/Utility/1182/' + num + ".js" #change
        jsc = requests.get(js_url).text
        pic = re.findall("Pic/OnlineComic\d/WZTX/\d\d\d\w/\d\d\d.\d*.\w\w\w",jsc)#change
        for i in pic:
            name = re.findall("\d\d\d\w.\d*.\w\w\w", i)
            for b in range(len(name)):
                picurl = host + i
                f.write(picurl + '\n')

f.close()

print ("Work Done")
