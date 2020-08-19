from bs4 import BeautifulSoup
import requests
import time
import re
from config import urls, session, headers, urlList#,cookies
#urll = function url list
def urll():
    print("Scrapping "+ urlList[0])
    #Scrapping from a url
    for url in urlList:
        #time.sleep(2) #Loops every X seconds, remove the comment if you're going live/plan to scrape a lot
        page = requests.get(url,headers=headers) #,cookies=cookies
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
#urla = function url array
def urla():
    #Scrapping from an array
    for url in urls:
        page = requests.get(url,headers=headers) #,cookies=cookies
        html = page.content
        bs = BeautifulSoup(html, 'html.parser')
        test = bs.find('title')
        ptest = test.get_text()
        print("Scrapping", ptest)
    else:
        print("Completed scrapping")