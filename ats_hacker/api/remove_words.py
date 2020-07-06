"""The word removal function for ats_hacker.

:param keywords: A dict made of keywords/counts.
:param word_filename: A filename for txt file of words to remove.

:returns: Mutated dict of keywords/counts.

"""

from api.import_file import import_file


def remove_words(keywords: dict, word_filename: str) -> dict:
    file = import_file(word_filename)

    removal_lst = file.split()

    for key in keywords.copy().keys():
        if key in removal_lst:
            del keywords[key]

    return keywords
