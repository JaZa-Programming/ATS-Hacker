"""The keyword aggregator for ats_hacker.

:param doc: A string representation of the input document.

:returns: A JSON document listing aggregated keyword and count pairs.

"""

import json  # https://docs.python.org/3/library/json.html
# See json.dumps() for encoding dicts to json


def aggregate(doc: str) -> json:
    """Aggregate is the primary API surface."""
    # TODO

    #Characters within a job posting that are irrelevant to keyword searches
    removal_characters = ['.', ',', '!', '_', '?', ';']

    for character in removal_characters:
        doc = doc.replace(character, '')

    keywords_dict = {}

    #Lowercase entire job posting in order to count uppercase and lowercase as same word (Example: Software == software)
    #Create list of individual words in job posting
    #If word is not in dictionary it will be added with 1. If already exists, 1 will be added to existing occurrence. 
    for word in doc.lower().split():
        if word not in keywords_dict:
            keywords_dict[word] = 1
        else:
            keywords_dict[word] += 1
    
    return json.dumps(keywords_dict)

