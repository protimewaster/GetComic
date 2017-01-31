import requests
import re
import urllib.request

chapter = 852
chapterno = str(chapter)
print (chapterno)
jsurl = ("http://comic.sfacg.com/Utility/2/" + chapterno + '.js')
jstext = requests.get(jsurl).text
print (jstext)
picpath = re.findall("Pic/OnlineComic\d/OnePiece/\d\d\d/\d*.\w\w\w",jstext)

for i in picpath:
##        print (i)
        host = 'http://hotpic.sfacg.com/'
        picurl = host + i
##        print (picurl)
        
        x = re.findall(r"\d\d", i)
        file = int(x[1])
        filename = r"%03d" % file
        path = chapterno + "-" + filename + ".jpg"
        print (path)
        
        data = urllib.request.urlretrieve(picurl, path)

print ('Work Done')
