from bs4 import BeautifulSoup
import urllib.request
import requests
import re

f = open('result.txt', 'w')

url = 'http://comic.sfacg.com/HTML/WZTX/'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
ul_tag = soup.find('ul', class_="serialise_list Blue_link2")
li_tag = ul_tag.findAll('li')

for li in li_tag:
    href = li.find('a', href=True)
    ch_url = "http://comic.sfacg.com" + href['href']
    if len(ch_url) == 37:
        num = re.findall("\d\d\d", ch_url)[0]
        js_url = 'http://comic.sfacg.com/Utility/1182/' + num + ".js"
        jsc = requests.get(js_url).text
        nsoup = BeautifulSoup(jsc, 'html.parser')
        str = nsoup.text
        pic = re.findall("Pic.OnlineComic4.WZTX.\d\d\d.\d\d\d.\d*.\w\w\w",str)
        for i in pic:
            base = 'http://coldpic.sfacg.com/'
            name = re.findall("\d\d\d.\d*.\w\w\w", i)
            for b in range(len(name)):
                picurl = base + i
                f.write(picurl + '\n')
        
    else:
        num = re.findall("\d\d\d\w", ch_url)[0]
        js_url = 'http://comic.sfacg.com/Utility/1182/' + num + ".js"
        jsc = requests.get(js_url).text
        nsoup = BeautifulSoup(jsc, 'html.parser')
        str = nsoup.text
        pic = re.findall("Pic.OnlineComic4.WZTX.\d\d\d\w.\d\d\d.\d*.\w\w\w",str)
        for i in pic:
            base = 'http://coldpic.sfacg.com/'
            name = re.findall("\d\d\d\w.\d*.\w\w\w", i)
            for b in range(len(name)):
                picurl = base + i
                f.write(picurl + '\n')
        

f.close()

print ("Done")
    
   
    
