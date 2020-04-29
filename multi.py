from bs4 import BeautifulSoup
import requests
import time
import re
#Only use urlopen if you'd like to use one url. The method urlopen method won't work for multiple url's!
#URLS in an array
urls = ['http://10.0.1.4/1.html', 'http://10.0.1.4/2.html','https://google.com'] 
#Opening the test file and removing the \n 
session = requests.session()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; )' 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;'}
#req = session.get(url, headers=headers)
with open('test.txt', 'r') as f:
    urlList = [line.rstrip() for line in f]
#Testing if the strip.
print("Scrapping "+ urlList[0])
#Scrapping from a url
for url in urlList:
    #time.sleep(2) #Loops every X seconds, remove the comment if you're going live/plan to scrape a lot
    page = requests.get(url,headers=headers)
    html = page.content
    bs = BeautifulSoup(html, 'html.parser')
    test = bs.find('title')
    ptest = test.get_text()
    #Using regex to search for the url, then returning headers
    if re.search(r'whatismybrowser', url):
        print(bs.find('table', {'class':'table-striped'}).get_text())
        #^Checking headers
        #print("The regex search worked!")
    print("Scrapping", ptest)
else:
    print("Completed scrapping")

#Scrapping from an array
for url in urls:
    page = requests.get(url,headers=headers)
    html = page.content
    bs = BeautifulSoup(html, 'html.parser')
    test = bs.find('title')
    ptest = test.get_text()
    print("Scrapping", ptest)
else:
    print("Completed scrapping")