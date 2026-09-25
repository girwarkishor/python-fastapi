import wikipedia
from textblob import TextBlob

# ApplicationName/Version (ProjectURL or ContactInformation)
wikipedia.set_user_agent(
    "python-fastapi/0.1 (https://github.com/girwarkishor/python-fastapi)"
)


async def get_wikipedia_summary(name: str = "War Goddess", length: int = 1) -> str:
    """Get the summary of a Wikipedia page for a given query."""
    my_wiki = wikipedia.summary(name, length)
    return my_wiki

async def search_wikipedia(name: str):
    """Search for a Wikipedia page for a given query."""
    search_results = wikipedia.search(name)
    return search_results

async def analyze_sentiment(text: str) -> str:
    """Analyze the sentiment of a given text."""
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

async def phrase(name: str) -> str:
    """Return a phrase."""
    page = wikipedia.page(name)
    blob = TextBlob(page.content)
    return blob.noun_phrases
    # return page.content[:100]  # Return the first 100 characters of the page content
