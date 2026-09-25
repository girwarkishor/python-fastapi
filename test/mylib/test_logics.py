import asyncio

from mylib.logics import get_wikipedia_summary


def test_get_wikipedia_summary():
    summary = asyncio.run(get_wikipedia_summary())
    assert "god" in summary