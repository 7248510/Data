import requests
from bs4 import BeautifulSoup

session = requests.session()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; )' 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;'}
#The header follows the same format/It's based off the book Web Scrapping With Python 
#{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)' 'AppleWebKit 537.36 (KHTML, like Gecko) Chrome','Accept':'text/html,application/xhtml+xml,application/xml;' 'q=0.9,image/webp,*/*;q=0.8'}
#{'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4068.4 Safari/537.36'}
url = 'https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending'
req = session.get(url, headers=headers)
#{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; )','AppleWebKit/537.36 (KHTML, like Gecko)':'Chrome/83.0.4086.0 Safari/537.36'}
bs = BeautifulSoup(req.text, 'html.parser')
print(bs.find('table', {'class':'table-striped'}).get_text())
