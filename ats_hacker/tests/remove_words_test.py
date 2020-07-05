"""Tests for the ATS-Hacker remove_words function."""

from api.aggregator import aggregate
from api.remove_words import remove_words
import json


def test_word_removal():
    doc = "This is a test job description, a description with a few words to remove."
    keywords = aggregate(doc)
    want = {
        'test': 1,
        'job': 1,
        'description': 2,
        'few': 1,
        'words': 1,
        'remove': 1
    }
    got = remove_words(json.loads(keywords),
                       "ats_hacker/tests/test_data/words-to-remove.txt")
    assert want == got
