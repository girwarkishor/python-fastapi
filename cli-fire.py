#!/usr/bin/env python3

import fire
from mylib.logics import get_wikipedia_summary

if __name__ == '__main__':
    fire.Fire(get_wikipedia_summary)