from bs4 import BeautifulSoup
import time
import requests
import mysql.connector
import datetime
from config import headers, sqlConf
controller = range(1,11) 
#This was a little test program to test the different schema's/web scraping ranges. To run this host the 1-10 html files on an server/docker and then run the scraper
def execute():
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
        #Declarations/BS 
        html = page.content
        bs = BeautifulSoup(html, 'html.parser')
        for a in bs.findAll("p"):
            print(a.get_text())  
            z = a.get_text() 
            complete = z + "\n"
            #Another logical error solved. It has to append, not write!
            with open('Sample.txt','a') as f:
                f.write(complete)
                f.close()  
            #
            def collect():
                time = datetime.datetime.now().strftime('%H:%M:%S')
                date =  datetime.datetime.now().strftime('%Y-%m-%d')
                combination = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                cnx = mysql.connector.connect(**sqlConf)
                cursor = cnx.cursor()
                cursor.execute("INSERT INTO STATIC(URL, DATE, TIME, COMB) VALUES(%s,%s,%s,%s)", (url, date, time, combination))
                cnx.commit()
                cursor.close()
                cnx.close()
            collect()
'''         
                USE TEST;
                CREATE TABLE STATIC (
                    UNIQ_ID INT AUTO_INCREMENT,
                    URL VARCHAR(350),
                    DATE VARCHAR(50),
                    TIME VARCHAR(50),
                    COMB VARCHAR(50),
                    PRIMARY KEY(UNIQ_ID)
                );
SAMPLE DB OUTPUT, FROM THE TEST PAGES, The timer works perfectly :)
+---------+------------------------+------------+----------+----------------------+
| UNIQ_ID | URL                     | DATE       | TIME     | COMB                |
+---------+-------------------------+------------+----------+---------------------+
|       1 | http://10.0.1.4/1.html  | 2020-05-18 | 23:15:14 | 2020-05-18 23:15:14 |
|       2 | http://10.0.1.4/2.html  | 2020-05-18 | 23:15:16 | 2020-05-18 23:15:16 |
|       3 | http://10.0.1.4/3.html  | 2020-05-18 | 23:15:18 | 2020-05-18 23:15:18 |
|       4 | http://10.0.1.4/4.html  | 2020-05-18 | 23:15:21 | 2020-05-18 23:15:21 |
|       5 | http://10.0.1.4/5.html  | 2020-05-18 | 23:15:23 | 2020-05-18 23:15:23 |
|       6 | http://10.0.1.4/6.html  | 2020-05-18 | 23:15:25 | 2020-05-18 23:15:25 |
|       7 | http://10.0.1.4/7.html  | 2020-05-18 | 23:15:27 | 2020-05-18 23:15:27 |
|       8 | http://10.0.1.4/8.html  | 2020-05-18 | 23:15:30 | 2020-05-18 23:15:30 |
|       9 | http://10.0.1.4/9.html  | 2020-05-18 | 23:15:32 | 2020-05-18 23:15:32 |
|      10 | http://10.0.1.4/10.html | 2020-05-18 | 23:15:34 | 2020-05-18 23:15:34 |
+---------+-------------------------+------------+----------+---------------------+
'''
