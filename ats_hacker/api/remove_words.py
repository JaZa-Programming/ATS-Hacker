"""The word removal function for ats_hacker.

:param keywords: A dict made of keywords/counts.
:param word_filename: A filename for txt file of words to remove.

:returns: Mutated dict of keywords/counts.

"""

from api.import_file import import_file


def remove_words(keywords: dict, words_to_remove: list) -> dict:
    for keyword in keywords.copy().keys():
        if keyword in words_to_remove:
            del keywords[keyword]

    return keywords
