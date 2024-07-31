from bs4 import BeautifulSoup
import requests


class scraper:
    def __init__(self, search_title: str, field: str = None) -> None:
        search_title: str = search_title.replace(" ", "+", -1)
        if field:
            self.URL: str = f"https://arxiv.org/search/{field}?query={search_title}&searchtype=all&abstracts=show&order=-announced_date_first&size=50"
        else:
            self.URL: str = f"https://arxiv.org/search/?query={search_title}&searchtype=all&abstracts=show&order=-announced_date_first&size=50"
        

        RESPONSE: requests.Response = requests.request("get", self.URL)
        RESPONSE_CONTENT = RESPONSE.content
        
        self.SOUP: BeautifulSoup = BeautifulSoup(RESPONSE_CONTENT, "html.parser")
    
    def get_info(self) -> list[dict[str, str]]:
        self.ORDERED_LIST_RESULTS = self.SOUP.find("ol", attrs={'class':'breathe-horizontal'})
        self.LIST_OF_RESULTS = self.ORDERED_LIST_RESULTS.find_all('li', attrs={'class':'arxiv-result'})
        self.RESULTS: list[dict[str, str]] = []

        for i in self.LIST_OF_RESULTS:
            self.TITLE: str = str(i.find('p', attrs={'class':'title is-5 mathjax'}).text)
            self.AUTHORS: str = str(i.find('p', attrs={'class':'authors'}).text)
            self.SUMMARY: str = str(i.find('p', attrs={'class':'abstract mathjax'}).text)
            
            self.TITLE = self.TITLE.replace("\n", "", -1)
            self.AUTHORS = self.AUTHORS.replace("\n", "", -1).replace("Authors", "", -1).replace(":", "", -1).split(',')

            self.URLS_PARENT_ELEMENT = i.find('p', attrs={'class':'list-title is-inline-block'})
            self.URLS_ELEMENTS = self.URLS_PARENT_ELEMENT.find_all('a', href=True)
            self.URLS = []
            
            for _, aElement in enumerate(self.URLS_ELEMENTS):
               self.URLS.append(aElement.get('href')) 

            self.MAIN_URL = self.URLS[0]
            self.PDF_URL = self.URLS[1]

            self.RESULTS.append({'Title':self.TITLE, 'Authors':self.AUTHORS, 'Summary':self.SUMMARY, 'Main_url':self.MAIN_URL, "Pdf_url":self.PDF_URL})

        return self.RESULTS
