from bs4 import BeautifulSoup
import time
import requests
from config import headers
controller = range(1,11) 
#This was a little test program to test the different schema's/web scraping ranges. To run this host the 1-10 html files on an server/docker and then run the scraper
for x in controller:
    url = "http://10.0.1.4/{0}".format(x) + ".html" #The IP is meant for testing purposes, if you're going to scrape a live url change it!
    try:
        time.sleep(2)
        print(url)
        page = requests.get(url,headers=headers) #,cookies=cookies
    except Exception:
        print("An error occured in the request. Is your network adapter enabled?")
        print("Is the url schema correct?")
    except AttributeError:
        print("Are you scraping what's loaded in JavaScript?")
    html = page.content
    bs = BeautifulSoup(html, 'html.parser')
    for a in bs.findAll("p"):
        print(a.get_text())
