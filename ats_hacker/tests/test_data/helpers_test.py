"""Tests for the helper functions for ats_hacker."""

import json
from api.helpers import encode_json, decode_json


def test_json_encode():
    document = {'this': 1, 'is': 1, 'a': 1, 'test': 1}
    want = '{"this": 1, "is": 1, "a": 1, "test": 1}'
    assert encode_json(document) == want


def test_json_decode():
    document = '{"this": 1, "is": 1, "a": 1, "test": 1}'
    want = {'this': 1, 'is': 1, 'a': 1, 'test': 1}
    assert decode_json(document) == want
