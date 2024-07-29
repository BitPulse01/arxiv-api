from bs4 import BeautifulSoup
import requests


class scraper:
    def __init__(self, search_title: str) -> None:
        self.URL: str = f"https://arxiv.org/search/?query={search_title}&searchtype=all&abstracts=show&order=-announced_date_first&size=50&start=0"

    def scrape_site(self):
        RESPONSE: requests.Response = requests.request("get", self.URL)
        RESPONSE_CONTENT = RESPONSE.content
        
        self.SOUP = BeautifulSoup(RESPONSE_CONTENT, "html.parser")

        return self.SOUP


search = str(input("Type smth to search : "))

SCRAPER = scraper(search)
SCRAPER_INFO = SCRAPER.scrape_site()

print(SCRAPER_INFO)
