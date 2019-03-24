import lxml
import requests
from bs4 import BeautifulSoup
import os

class Scraper:
    def scrape(self, keyword):
        url = "https://sentence.yourdictionary.com/" + keyword
        site = requests.get(url)
        soup = BeautifulSoup(site.content, "lxml")
        defs = soup.find_all('div', {'class': 'li_content'})

        short = defs[0].text

        range_list = len(defs)
        if range_list > 4:
            it = 4
        else:
            it = range_list
            
        for i in range(0, it):
            if len(defs[i].text) < len(short):
                short = defs[i].text

        #print(short)
        return(short)


# testing
#word = 'flag'

#s = Scraper()                ## create Scraper
#sentence = s.scrape(word)    ## return
