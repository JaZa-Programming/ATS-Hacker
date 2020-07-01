"""The file importer for ats_hacker.

:param filename: A string representation of the filename to be processed.

:returns: A string representation of the file.

"""


def import_file(filename: str) -> str:
    """Opens a file, processes it, and returns a string representation."""
    # TODO
    # We will need to decide how to handle newline "\n" characters. Given the
    # processing done for characters in aggregate(), it might make sense to
    # add the removal of newlines in that func instead of this one.
    #
    # Also, make sure you close the file (use the "with" keyword") before
    # this function returns so that we don't end up with any leaks. If the file
    # isn't found, you'll need to handle the IOError exception so that the
    # program doesn't crash in an ugly way.
    return
