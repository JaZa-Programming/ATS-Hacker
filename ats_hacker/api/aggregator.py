"""The keyword aggregator for ats_hacker.

:param doc: A string representation of the input document.

:returns: A JSON document listing aggregated keyword and count pairs.

"""

import json  # https://docs.python.org/3/library/json.html
# See json.dumps() for encoding dicts to json


def aggregate(doc: str) -> json:
    """Aggregate is the primary API surface."""
    # TODO
    return '{"this": 1, "is": 1, "a": 1, "test": 1, "job": 1, "description": 1}'
