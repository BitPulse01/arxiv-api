from bs4 import BeautifulSoup
import requests


class scraper:
    def __init__(self, search_title: str) -> None:
        self.URL: str = f"https://arxiv.org/search/?query={search_title}&searchtype=all&abstracts=show&order=-announced_date_first&size=50&start=0"

        RESPONSE: requests.Response = requests.request("get", self.URL)
        RESPONSE_CONTENT = RESPONSE.content
        
        self.SOUP = BeautifulSoup(RESPONSE_CONTENT, "html.parser")

        # print(self.SOUP)
    
    def find_titles(self):
        self.titles_elements = self.SOUP.select("p.title.is-5.mathjax")
        self.titles = []

        for self.title in self.titles_elements:
            self.titles.append(self.title.text)
        
        return self.titles


search = str(input("Type smth to search : "))

SCRAPER = scraper(search)
SCRAPER_INFO = SCRAPER.find_titles()

print(SCRAPER_INFO)
