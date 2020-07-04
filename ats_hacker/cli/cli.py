"""The command line interface class for ats_hacker."""

import argparse
from api.aggregator import aggregate
from api.helpers import decode_json
from api.import_file import import_file


class CLI:
    """CLI interfaces between the user and the aggregator API."""

    def __init__(self):
        self.document = ""
        self.keyword_counts = {}
        self.json_encoded_counts = ""

    def start(self):
        """Execute command-line instance of ats_hacker."""
        args = parse_args()
        self._process_document(import_file(args.filename[0]))
        if args.o == "json":
            self._print_json()
        else:
            self._print_pretty()

    def _populate_keyword_counts(self):
        self.json_encoded_counts = aggregate(self.document)
        self.keyword_counts = decode_json(self.json_encoded_counts)

    def _print_json(self):
        print(self.json_encoded_counts)

    def _print_pretty(self):
        # TODO: Implement Pretty Print Feature
        print("Pretty: " + str(self.keyword_counts))

    def _process_document(self, document: str):
        self.document = document
        self._populate_keyword_counts()


def parse_args():
    """Parse command-line args for ats_hacker."""
    parser = argparse.ArgumentParser(
        description='Keyword aggregator for ATS optimization.')
    parser.add_argument('filename', metavar='filename', type=str, nargs=1,
                        help='txt filename for keyword aggregation')
    parser.add_argument('-o', metavar='json', type=str, nargs='?',
                        help='output in raw JSON format')
    return parser.parse_args()
