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
            self.TITLE: str = str(i.find('p', attrs={'class':'title is-5 mathjax'}).text)
            self.AUTHORS: str = str(i.find('p', attrs={'class':'authors'}).text)
            self.SUMMARY: str = str(i.find('p', attrs={'class':'abstract mathjax'}).text)
            
            self.TITLE = self.TITLE.replace("\n", "", -1)
            self.AUTHORS = self.AUTHORS.replace("\n", "", -1).replace("Authors", "", -1)
            # TODO: Refactor this jumbled up mess of a code to use an parent_element.find_all('a') instead of ... whatever
            self.URLS_PARENT_ELEMENT = i.find('p', attrs={'class':'list-title is-inline-block'})
            self.URLS = []

            for _, element in enumerate(self.URLS_PARENT_ELEMENT):
                self.URLS.append(element)
            
            self.MAIN_URL = self.URLS[0]
            self.PDF_URL = str(self.URLS[2]).replace("<span>", "", -1).replace("</span>", "", -1)
            self.PDF_URL = self.PDF_URL.split(",")[0].replace("[", "", -1).replace("]", "", -1)
            print(BeautifulSoup(self.PDF_URL, 'html.parser').find('a').get('href'))

            self.RESULTS.append({'TITLE':self.TITLE, 'AUTHORS':self.AUTHORS, 'SUMMARY':self.SUMMARY, 'MAIN_URL':self.MAIN_URL, "PDF_URL":self.PDF_URL})

        return self.RESULTS


search: str = str(input("Type smth to search : "))

SCRAPER: scraper = scraper(search)
SCRAPER_INFO: list[dict[str, str]] = SCRAPER.find_titles_and_links()

# print(SCRAPER_INFO)
