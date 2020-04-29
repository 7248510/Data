import requests
urls = ['http://10.0.1.4/1.html', 'http://10.0.1.4/2.html', 'https://google.com/']
#Opening the test file and stripping the \n 
session = requests.session()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; )' 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;'}
#req = session.get(url, headers=headers)
with open('test.txt', 'r') as f:
    urlList = [line.rstrip() for line in f]