"""The keyword aggregator for ats_hacker.

:param doc: A string representation of the input document.

:returns: A JSON document listing aggregated keyword and count pairs.

"""

import json  # https://docs.python.org/3/library/json.html


def aggregate(doc: str) -> json:
    """Aggregate counts keywords in the given string."""
    doc = remove_characters(doc)

    keywords_dict = {}
    for word in doc.lower().split():
        if word not in keywords_dict:
            keywords_dict[word] = 1
        else:
            keywords_dict[word] += 1

    return json.dumps(keywords_dict)


def remove_characters(doc: str) -> str:
    removal_characters = ['.', ',', '!', '_', '?', ';', ':']
    for character in removal_characters:
        doc = doc.replace(character, '')
    return doc
