from bs4 import BeautifulSoup
from colorama import Fore
import requests


class scraper:
    def __init__(self, search_title: str) -> None:
        search_title: str = search_title.replace(" ", "+", -1)
        self.URL: str = f"https://arxiv.org/search/?query={search_title}&searchtype=all&abstracts=show&order=-announced_date_first&size=50"

        RESPONSE: requests.Response = requests.request("get", self.URL)
        RESPONSE_CONTENT = RESPONSE.content
        
        self.SOUP: BeautifulSoup = BeautifulSoup(RESPONSE_CONTENT, "html.parser")
    
    def find_titles_and_links(self) -> list[dict[str, str]]:
        self.ORDERED_LIST_RESULTS = self.SOUP.find("ol", attrs={'class':'breathe-horizontal'})
        self.LIST_OF_RESULTS = self.ORDERED_LIST_RESULTS.find_all('li', attrs={'class':'arxiv-result'})
        self.RESULTS: list[dict[str, str]] = []

        for i in self.LIST_OF_RESULTS:
            # TODO: TITLE, AUTHORS, SUMMARY, PDF, PDF URL, MAIN URL
            self.TITLE: str = str(i.find('p', attrs={'class':'title is-5 mathjax'}).text)

            self.RESULTS.append({'TITLE':self.TITLE})

        return self.RESULTS


search: str = str(input("Type smth to search : "))

SCRAPER: scraper = scraper(search)
SCRAPER_INFO: list[dict[str, str]] = SCRAPER.find_titles_and_links()

print(SCRAPER_INFO)
