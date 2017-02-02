from bs4 import BeautifulSoup
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#get the menu page
url = 'http://book.sfacg.com/Novel/41889/MainIndex/'
resp = urllib.request.urlopen(url).read()
soup = BeautifulSoup(resp, 'html.parser')

#book name
book = soup.find('h1').text
print (book)
filename = book + ".txt"
f = open(filename, 'w', encoding = 'utf-8')
f.write(book + '\n'*2)

#chapter
chapter = soup.find_all('h3')
for ch in range(len(chapter)):
        print (chapter[ch].text)

#content 
links = soup.find_all('div', class_='story-catalog')
for x in links: 
        chtitle = x.find('h3') 
        print (chtitle.text) 
        f.write(chtitle.text + '\n'*2)
        c1 = x.find_all('li') 
        for i in c1:
                c2 = i.find('a', href=True)
                raw = 'http://book.sfacg.com'
                new = raw + c2['href']
##                print (new)
                nresp = urllib.request.urlopen(new)
                nsoup = BeautifulSoup(nresp, 'html.parser')
                a = nsoup.find_all('p')
                b = nsoup.find('div', 'list_menu_title').text
##                print (b)
                f.write(b + '\n'*2)
                for i in range(len(a)):
                        f.write(a[i].text + '\n')
                        f.write('\n')

f.close()

print ("All chapters are exported")
