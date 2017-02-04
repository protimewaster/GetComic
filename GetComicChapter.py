from bs4 import BeautifulSoup
import urllib.request
import requests
import re
import os

#General information
name = 'WDQC'
Chapters = range(31, 32)

host = 'http://comic.sfacg.com/'
pichost = 'http://hotpic.sfacg.com'
index = host + 'HTML/' + name
resp = requests.get(index)
resp.encoding = 'utf-8'

#Find ComicID
ComicIDs = re.findall(r"ComicID=\d*", resp.text)
IDs = re.findall("\d{1,5}", ComicIDs[0])
ComicID = IDs[0]

#Find comic name
soup = BeautifulSoup(resp.text, 'html.parser')
title = soup.title.text
comicname = re.match(r"(.*?),(.*)", title).group(1)
print (comicname)
os.makedirs(comicname, exist_ok=True)
os.chdir(comicname)

for chapternum in Chapters:
    num = r"%03d" % chapternum
    jsurl = host + "Utility/" + (ComicID) + "/" + num + ".js"
    js = requests.get(jsurl).text
    picpaths = re.findall(r'"(/P.*?)";',js)
    filecount = 1
    for picpath in picpaths:
    	picurl = pichost + picpath
    	filenum = r"%03d" % filecount
    	filename = num + "-" + filenum + ".jpg"
    	urllib.request.urlretrieve(picurl, filename)
    	filecount += 1
    print ("Chapter " + num + " is saved.")

print ("Done")
