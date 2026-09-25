from fastapi import FastAPI
from mylib.logics import (
    get_wikipedia_summary,
    search_wikipedia as search_wikipedia_pages,
    phrase as get_wikipedia_phrase,
    analyze_sentiment as analyze_sentiment_text,
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

@app.get("/wikipedia/phrase/{name}")
async def read_wikipedia_phrase(name: str):
    return {"phrase": await get_wikipedia_phrase(name)}

@app.get("/wikipedia/sentiment/{text}")
async def analyze_sentiment(text: str):
    sentiment = await analyze_sentiment_text(text)
    return {"sentiment": sentiment}

if __name__ == "__main__":
    pass