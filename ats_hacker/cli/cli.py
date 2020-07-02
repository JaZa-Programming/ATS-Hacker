"""The command line interface class for ats_hacker."""

import json
from ats_hacker.api.aggregator import aggregate


class CLI:
    """CLI interfaces between the user and the aggregator API."""

    def __init__(self):
        self.document = ""
        self.keyword_counts = {}

    def process_document(self, document: str):
        self.document = document
        self._populate_keyword_counts()

    def _populate_keyword_counts(self):
        encoded_counts = aggregate(self.document)
        self.keyword_counts = self._decode_json(encoded_counts)

    def _decode_json(self, json_document):
        return json.loads(json_document)
