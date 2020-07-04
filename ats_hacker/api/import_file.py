"""The file importer for ats_hacker.

:param filename: A string representation of the filename to be processed.

:returns: A string representation of the file.

"""

import sys


def import_file(filename: str) -> str:
    """Opens a file, processes it, and returns a string representation."""
    try:
        with open(filename, 'r') as file:
            contents = file.read()
    except FileNotFoundError:
        sys.stderr.write(f"ats_hacker: error: No such file or directory: '{filename}'\n")
        sys.exit(1)
    return contents
