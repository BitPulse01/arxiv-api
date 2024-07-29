from bs4 import BeautifulSoup
from colorama import Fore
import requests


class scraper:
    def __init__(self, search_title: str) -> None:
        search_title = search_title.replace(" ", "+", -1)
        self.URL: str = f"https://arxiv.org/search/?query={search_title}&searchtype=all&abstracts=show&order=-announced_date_first&size=50"

        RESPONSE: requests.Response = requests.request("get", self.URL)
        RESPONSE_CONTENT = RESPONSE.content
        
        self.SOUP = BeautifulSoup(RESPONSE_CONTENT, "html.parser")

    
    def find_titles_and_links(self):
        self.ORDERED_LIST_RESULTS = self.SOUP.find("ol", attrs={'class':'breathe-horizontal'})
        self.LIST_OF_RESULTS = self.ORDERED_LIST_RESULTS.find_all('li', attrs={'class':'arxiv-result'})
        self.RESULTS = []

        for i in self.LIST_OF_RESULTS:
            # TODO: TITLE, AUTHORS, SUMMARY, PDF, PDF URL, MAIN URL
            self.TITLE = i.find('p', attrs={'class':'title is-5 mathjax'})

            self.RESULTS.append({'TITLE':self.TITLE.text})

        return self.RESULTS


search = str(input("Type smth to search : "))

SCRAPER = scraper(search)
SCRAPER_INFO = SCRAPER.find_titles_and_links()

# title = SCRAPER_INFO[0]
# links = SCRAPER_INFO[1]

print(SCRAPER_INFO)