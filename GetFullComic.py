from bs4 import BeautifulSoup
import urllib.request
import requests
import re
import os

#General information
name = 'WDQC'
host = 'http://comic.sfacg.com/'
pichost = 'http://coldpic.sfacg.com'
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
test = open("test.txt", 'w')

#Find chapter number
ultag = soup.find('ul', class_="serialise_list Blue_link2")
litag = ultag.findAll('li')
for li in litag:
    href = li.find('a', href=True)
    num = re.findall("\d.*\w+", href['href'])

    #Find url of pic in the js file
    for chapternum in num:
    	jsurl = host + "Utility/" + (ComicID) + "/" + chapternum + ".js"
    	js = requests.get(jsurl).text
    	picpaths = re.findall(r'"(/P.*?)";',js)
    	filecount = 1
    	for picpath in picpaths:
    		picurl = pichost + picpath
    		test.write(picurl + '\n')
    		filenum = r"%03d" % filecount
    		filepath = chapternum + "-" + filenum + ".jpg"
    		# data = urllib.request.urlretrieve(picurl, filepath)
    		filecount += 1
    	print ("Chapter " + chapternum + " is saved.")
test.close()
print ("Done")
