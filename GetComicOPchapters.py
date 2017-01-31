import requests
import re
import urllib.request

for chapter in range(852,853): #The starting and ending nos of the chapters
	chapterno = str(chapter)
	print (chapterno)
	jsurl = ("http://comic.sfacg.com/Utility/2/" + chapterno + '.js')
	jstext = requests.get(jsurl).text
##	print (jstext)
	picpath = re.findall("Pic/OnlineComic\d/OnePiece/\d\d\d/\d\d\d_\d*.\w\w\w",jstext)

	for i in picpath:
	    # print (i)
	    host = 'http://coldpic.sfacg.com/'
	    filename = re.findall("\d\d\d_\d*", i)
	    # print (name)

	    for b in range(len(filename)):
	        path = chapterno + "-" + filename[b] + ".jpg"
	        # print (path)
	        picurl = host + i
	        print (picurl)
	        data = urllib.request.urlretrieve(picurl, path)

print ('Work Done')
