"""The keyword aggregator for ats_hacker.

:param doc: A string representation of the input document.

:returns: A dict listing aggregated keyword and count pairs.

"""


def aggregate(document: str) -> dict:
    """Aggregate counts keywords in the given string."""
    document = remove_characters(document)

    keywords = {}
    for word in document.lower().split():
        if word not in keywords:
            keywords[word] = 1
        else:
            keywords[word] += 1

    return keywords


def remove_characters(document: str) -> str:
    removal_characters = ['.', ',', '!', '_', '?', ';', ':']
    for character in removal_characters:
        document = document.replace(character, '')
    return document
