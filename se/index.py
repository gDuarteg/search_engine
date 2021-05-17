import json

from functools import partial
from collections import defaultdict
import re

from nltk.stem import LancasterStemmer


def clean_text(txt: str) -> str:
    # Regex obtida de https://www.geeksforgeeks.org/python-check-url-string/
    pattern = r"""
        (?i)  # Ignore case.
        \b  # Inicio de palavra.
        (?:
            https?://
        |
            www
            \d{0,3}
            [.]
        |
            [a-z0-9.\-]+
            [.]
            [a-z]{2,4}
            /
        )
        (?:
            [^\s()<>]+
        |
            \(
            (?:
                [^\s()<>]+
            |
                \(
                [^\s()<>]+
                \)
            )*
            \)
        )+
        (?:
            \(
            (?:
                [^\s()<>]+
            |
                \(
                [^\s()<>]+
                \)
            )*
            \)
        |
            [^\s`!()\[\]{};:'\".,<>?«»“”‘’]
        )
    """
    matcher = re.compile(pattern, re.VERBOSE)
    txt = matcher.sub("", txt)
    txt = re.sub(r"[\.,\?:;'\"/\\`~!@\\%\^&\*\(\)\[\]{}]", " ", txt)
    txt = re.sub("[«‹»›„“‟”’❝❞❮❯⹂〝〞〟＂‚‘‛❛❜❟]", " ", txt)

    txt = txt.lower()

    stemmer = LancasterStemmer()
    return " ".join([stemmer.stem(w) for w in txt.split() if w != ""])


class Index:
    def __init__(self, index):
        self.index = index

    def get(self, word: str):
        try:
            return self.index[word]
        except KeyError:
            return []

    def get_count(self, query: str, doc: str):
        try:
            return self.index[query][doc]
        except KeyError:
            return 0


def make_index(docs):
    index = defaultdict(partial(defaultdict, int))

    for k, doc in enumerate(docs):
        words = set(doc)
        for word in words:
            index[clean_text(word)][k] += 1
    return index


def load_index(path) -> Index:
    with open(path, "r") as file:
        return Index(json.load(file))
