import lmxl
import requests
from bs4 import BeautifulSoup
import os

class Scraper:
    def __init__(self, credentials_path):
        # authentication
        self.authenticate(credentials_path)

    def authenticate(self, credentials_path):
        # Set the path to the credentials
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

    def scrape(self, url):
        site = requests.get(url)
        soup = BeautifulSoup(site.content, "lxml")  # what does lxml do?
        print(soup.content)
        defs = soup.find_all('div', {'class': 'li_content'})
        print(defs)

# testing
path = 'C:\\Users\\kelly\\Desktop\\translate\\translate_test.json'
url = "https://sentence.yourdictionary.com/pencil"

s = Scraper(path)
s.scrape(url)

'''
class Scraper:
    def __init__(self, credentials_path):
        # authentication
        self.authenticate(credentials_path)

    def authenticate(self, credentials_path):
        # Set the path to the credentials
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

    def scrape(self, url):
        site = requests.get("http://oreilly.com/store/samplers.html")
        content = site.content
        soup = BeautifulSoup(site.content)  # what does lxml do?
        print(site.status_code)
        print(site.headers)
        print("*************")
        defs = soup.find_all("div")
        print(defs)

# testing
path = 'C:\\Users\\kelly\\Desktop\\translate\\translate_test.json'

url = "https://sentence.yourdictionary.com/pencil"

s = Scraper(path)
s.scrape(url)
'''
