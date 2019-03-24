import lxml
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

    def scrape(self, keyword):
        url = "https://sentence.yourdictionary.com/" + keyword
        site = requests.get(url)
        soup = BeautifulSoup(site.content, "lxml")
        defs = soup.find_all('div', {'class': 'li_content'})
        print(defs[0].text)
        return defs[0].text

# # testing
# path = 'C:\\Users\\kelly\\Desktop\\translate\\translate_test.json'
# # url = "https://sentence.yourdictionary.com/pencil"
#
# word = 'desk'
# s = Scraper(path)
# s.scrape(word)
