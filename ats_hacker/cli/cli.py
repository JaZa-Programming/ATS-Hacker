"""The command line interface class for ats_hacker."""

import argparse
import json
from api.aggregator import aggregate
from api.import_file import import_file


class CLI:
    """CLI interfaces between the user and the aggregator API."""

    def __init__(self):
        self.document = ""
        self.keyword_counts = {}
        self.json_encoded_counts = ""

    def process_document(self, document: str):
        self.document = document
        self._populate_keyword_counts()

    def _populate_keyword_counts(self):
        self.json_encoded_counts = aggregate(self.document)
        self.keyword_counts = self._decode_json(self.json_encoded_counts)

    def _decode_json(self, json_document):
        return json.loads(json_document)

    def start():
        interface = CLI()
        args = interface._parse_args()
        interface.process_document(import_file(args.filename[0]))
        print(interface.keyword_counts)

    def _parse_args(self):
        parser = argparse.ArgumentParser(
            description='Keyword aggregator for ATS optimization.')
        parser.add_argument('filename', metavar='filename', type=str, nargs=1,
                            help='txt filename for keyword aggregation')
        return parser.parse_args()
