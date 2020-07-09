"""The command line interface class for ats_hacker."""

import argparse

from api.aggregator import aggregate
from api.helpers import decode_json, encode_json
from api.import_file import import_file
from api.remove_words import remove_words
from clint.textui import colored, columns
from pyfiglet import Figlet


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
        # Check if user specified word removal file
        # if args.r:
        # We need to import the remove_words() function
        # That function takes a dict, ie. self.keyword_counts
        # And returns a changed dict, so we need to assign that back to
        # self.keyword_counts
        # Then, we need to overwrite self.json_encoded_counts with
        # the json returned from encode_json
        # ie.: self.json_encoded_counts = encode_json(self.keyword_counts)
        if args.o == "json":
            self._print_json()
        else:
            self._print_pretty(args.filename[0])

        if args.r:
            self.keyword_counts = remove_words(self.keyword_counts, args.r)

    def _populate_keyword_counts(self):
        self.json_encoded_counts = aggregate(self.document)
        self.keyword_counts = decode_json(self.json_encoded_counts)

    def _print_json(self):
        print(self.json_encoded_counts)

    def _print_pretty(self, filename):
        print(colored.magenta(Figlet(font='mini').renderText('ATS_Hacker')))
        print(f"Document: {colored.magenta(filename)}\n")
        col = 20
        print(columns([(colored.red('Word')), col],
                      [(colored.blue('Occurances')), col]))
        for word, count in self.keyword_counts.items():
            print(columns([word, col], [str(count), col]))
        print()

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
    parser.add_argument('-r', metavar='filename', type=str, nargs='?',
                        help='txt filename for words to remove')
    return parser.parse_args()
