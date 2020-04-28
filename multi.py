import bs4
import requests
import time
#Only use urlopen if you'd like to use one url. The method urlopen won't work for multiple url's!
#URLS to scrape
#urls = ['http://10.0.1.4/1.html', 'http://10.0.1.4/2.html','https://google.com']

#Opening the test file and stripping the \n 
with open('test.txt', 'r') as f:
    urlList = [line.rstrip() for line in f]
#Testing if the strip.
#It works print (urlList)
print("Scrapping "+ urlList[0])
for url in urlList:
    time.sleep(5) #Loops every 5 seconds
    page = requests.get(url)
    html = page.content
    soup = bs4.BeautifulSoup(html, "html.parser")
    test = soup.find('title')
    ptest = test.get_text()
    #print(test)
    print("Scrapping", ptest)
else:
    print("Completed scrapping")
