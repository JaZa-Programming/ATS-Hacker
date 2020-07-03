"""Tests for the keyword aggregator api."""

import json
from api.aggregator import aggregate


def test_aggregate_return_type():
    doc = "This is a test."
    got = aggregate(doc)
    assert isinstance(got, str)


def test_simple_aggregate():
    doc = "This is a test job description."
    want = json.dumps({
        "this": 1,
        "is": 1,
        "a": 1,
        "test": 1,
        "job": 1,
        "description": 1
    })
    got = aggregate(doc)
    assert want == got


def test_complex_aggregate():
    doc = "This is a test job. This is a test job description. This is" \
        " what I am testing."
    want = json.dumps({
        "this": 3,
        "is": 3,
        "a": 2,
        "test": 2,
        "job": 2,
        "description": 1,
        "what": 1,
        "i": 1,
        "am": 1,
        "testing": 1
    })
    got = aggregate(doc)
    assert want == got
