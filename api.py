from fastapi import FastAPI


SERVER: FastAPI = FastAPI()


@SERVER.get("/")
async def root():
    return {"message": "Hello World"}