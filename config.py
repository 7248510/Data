import requests
urls = ['http://10.0.1.4:3000/'] #This is url is for testing headers, I wrote an Node js application to view your browsers headers & method
#cookies = dict(cookies='Leaving the option')
#Opening the test file and stripping the \n 
session = requests.session()
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','accept-language':'en-US,en;q=0.5','accept-encoding': 'gzip, deflate'}
#req = session.get(url, headers=headers)
with open('test.txt', 'r') as f:
    urlList = [line.rstrip() for line in f]