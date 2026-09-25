# python-fastapi

A small FastAPI and command-line project that retrieves summaries from
Wikipedia.

## Prerequisites

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)

Install `uv` if it is not already available:

```bash
pip install uv
```

## Installation

Clone the repository, move into the project directory, and install the
project dependencies:

```bash
uv sync
```

For a new project, the initial setup can be created with:

```bash
uv init --no-package
uv add "fastapi[standard]" wikipedia ipython
uv add --dev pytest pytest-cov black fire pylint
```

## Command-Line Usage

Display the available options:

```bash
uv run ./cli-fire.py --help
```

Retrieve a Wikipedia summary by specifying the page name and the number of
sentences to return:

```bash
uv run ./cli-fire.py get_wikipedia_summary --name "Python programming" --length 10
```

Search Wikipedia for pages related to a keyword. The command returns a list of
matching page titles:

```bash
uv run ./cli-fire.py search_wikipedia --name "python"
```

## Inspect Installed Packages

List packages installed in the project environment:

```bash
uv run python -m pip freeze | less
```

## Experiment in IPython

Start an interactive IPython session:

```bash
uv run ipython
```

Then import and call the library function:

```python
from mylib.logics import get_wikipedia_summary

get_wikipedia_summary("Python programming", length=1)
```

Alternatively, preload the function when starting IPython:

```bash
uv run ipython -i -c "from mylib.logics import get_wikipedia_summary"
```

You can then call it directly:

```python
get_wikipedia_summary()
```

## Run the API

Start the FastAPI development server with:

```bash
uv run fastapi dev
```

Once the server starts, the API is available at:

- Application: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Interactive API documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## TextBlob Setup

TextBlob is a Python library for processing text. This project uses it for
sentiment analysis and noun phrase extraction.

Add TextBlob to the project dependencies:

```bash
uv add textblob
```

Download the language corpora required by TextBlob:

```bash
uv run python -m textblob.download_corpora
```

If TextBlob raises a `MissingCorpusError`, run the corpus download command
again in the project environment. The corpora are required for features such
as sentiment analysis and noun phrase extraction.

## Workflow

![Project workflow](https://github.com/user-attachments/assets/771d644a-4b34-4863-99a8-76f4c9ecc07b)