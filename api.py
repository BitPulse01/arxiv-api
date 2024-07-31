from fastapi import FastAPI
import scraper


SERVER: FastAPI = FastAPI()


@SERVER.get("/")
async def search(search: str, field: str | None = None):
    if field:
        SCRAPER = scraper.scraper(search_title= search, field= field)
        SCRAPER_INFO = SCRAPER.get_info()

        return SCRAPER_INFO
    
    SCRAPER = scraper.scraper(search_title= search)
    SCRAPER_INFO = SCRAPER.get_info()

    return SCRAPER_INFO

    