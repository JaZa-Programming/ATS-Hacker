"""Tests for the keyword aggregator api."""

from ats_hacker.api.aggregator import aggregate
import json


def test_simple_aggregate():
    input = "This is a test job description."
    want = json.dumps({
        "this": 1,
        "is": 1,
        "a": 1,
        "test": 1,
        "job": 1,
        "description": 1
    })
    got = aggregate(input)
    assert want == got
