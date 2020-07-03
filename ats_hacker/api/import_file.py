"""The file importer for ats_hacker.

:param filename: A string representation of the filename to be processed.

:returns: A string representation of the file.

"""


def import_file(filename: str) -> str:
    """Opens a file, processes it, and returns a string representation."""
    try:
        with open(filename, 'r') as file:
            contents = file.readlines()
    except FileNotFoundError as e:
        raise FileNotFoundError(f'No such file or directory: {filename}')
    return contents
