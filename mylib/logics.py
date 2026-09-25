import wikipedia

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
