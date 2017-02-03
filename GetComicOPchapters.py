import requests
import re
import urllib.request

for chapter in range(852,853): #The starting and ending nos of the chapters
	chapterno = str(chapter)
	print (chapterno)
	jsurl = ("http://comic.sfacg.com/Utility/2/" + chapterno + '.js')
	jstext = requests.get(jsurl).text
##	print (jstext)
	lines = re.findall(".*?", jstext)
	count = 1

	for line in lines:
	    picpath = re.findall("Pic/.*?/.*.\w\w\w", line)
	    host = 'http://coldpic.sfacg.com/'
		filenum = r"%03d" % count
		
	    for path in picpath:
	        path = chapterno + "-" + filenum + ".jpg"
	        picurl = host + path
	        data = urllib.request.urlretrieve(picurl, path)

print ('Work Done')
