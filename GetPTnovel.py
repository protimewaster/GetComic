from bs4 import BeautifulSoup
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://www.piaotian.net/html/8/8216/'
resp = requests.get(url)
resp.encoding = 'gb18030'
index = BeautifulSoup(resp.text, 'html.parser')
name = index.find('h1').text
filename = name + ".txt"
f = open(filename,'w', encoding = 'utf-8')

chapters = index.find_all("li")
for chapterno in range(4,len(chapters)):
    chaptertitles = chapters[chapterno].findAll('a', href=True)
    for chapter in chaptertitles:
        chaptertitle = chapter.text
        f.write(chaptertitle + '\n')
        
        chapterpath = chapter['href']
        host = 'http://www.piaotian.net/html/8/8216/'
        chapterurl = host + chapterpath
        chrep = requests.get(chapterurl)
        chrep.encoding = 'gb18030'
        chsoup = BeautifulSoup(chrep.text, 'html.parser')
        for p in chsoup.find_all('br'):
            f.write(p.text + '\n')
            
        print (chaptertitle)
        
f.close()

print ("All chapters are saved.")
