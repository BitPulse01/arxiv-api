from fastapi import FastAPI


SERVER: FastAPI = FastAPI()


@SERVER.get("/")
async def root():
    return {}


@SERVER.get("/search/")
async def search(search: str):
    return {"SEARCH":search}
