from fastapi import FastAPI
from mylib.logics import (
    get_wikipedia_summary,
    search_wikipedia as search_wikipedia_pages,
)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/add/{num1}/{num2}")
async def add_numbers(num1: int, num2: int):
    """Add two numbers and return the result."""
    return {"result": num1 + num2}

@app.get("/wikipedia/summary")
async def read_wikipedia_summary(name: str = "War Goddess", length: int = 1):
    return {"summary": await get_wikipedia_summary(name, length)}

@app.get("/wikipedia/search")
async def search_wikipedia(name: str):
    return {"results": await search_wikipedia_pages(name)}

if __name__ == "__main__":
    pass