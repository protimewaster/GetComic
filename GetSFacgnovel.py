from bs4 import BeautifulSoup
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#get index page
url = 'http://book.sfacg.com/Novel/41889/MainIndex/'
resp = requests.get(url).text
index = BeautifulSoup(resp, 'html.parser')

#find novel name in <h1> under <div class="story-head"> and use it as output txt file name
novelname = index.find('h1', class_="story-title").text
print (novelname)
filename = novelname + ".txt"
f = open(filename, 'w', encoding = 'utf-8')
f.write(novelname + '\n'*2)

#find titles of chapters in <div class="story-catalog"> tags
chapters = index.findAll('div', class_='story-catalog')
chaptercount = 1
for chapter in chapters:       
        chapternum = r"%02d" % chaptercount
        chaptertitle = chapter.find('h3').text 
        f.write(chaptertitle + '\n'*2)
        print (chapternum, chaptertitle) 

        #find paths of sections of a chapter in <a> under <li> tags
        sectionpaths = chapter.findAll('li')
        sectioncount = 1
        for sectionpath in sectionpaths:
                pathurl = sectionpath.find('a', href=True)

                #compile urls of sections and get sections
                host = 'http://book.sfacg.com'
                sectionurl = host + pathurl['href']
                nresp = requests.get(sectionurl).text
                section = BeautifulSoup(nresp, 'html.parser')

                #find title of a section in <div class="list_menu_title"> tag in a section page
                sectiontitle = section.find('div', 'list_menu_title').text
                sectionnum = r"%02d" % sectioncount
                f.write(sectiontitle + '\n'*2)
                print (chapternum, sectionnum, sectiontitle)
                sectioncount += 1

                #find paragraphs in <p> tags
                paragraph = section.findAll('p')
                for p in paragraph:
                        f.write(p.text + '\n'*2)
                
        chaptercount += 1
        
f.close()

print ("All chapters are saved")
