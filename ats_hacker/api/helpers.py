"""Helper functions for ats_hacker."""

import json


def decode_json(json_document: str) -> dict:
    return json.loads(json_document)
