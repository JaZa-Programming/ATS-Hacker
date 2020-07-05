"""The word removal function for ats_hacker.

:param keywords: A dict made of keywords/counts.
:param word_filename: A filename for txt file of words to remove.

:returns: Mutated dict of keywords/counts.

"""


def remove_words(keywords: dict, word_filename: str) -> dict:
    with open(word_filename, 'r') as file:
        file = file.read()
        removal_lst = file.split()

        for key, value in keywords.copy().items():
            if key in removal_lst:
                del keywords[key]

    return keywords

        
