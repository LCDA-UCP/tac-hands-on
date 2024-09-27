from typing import Tuple, List

import numpy as np


def pos_tagger(sentence: str, pos_dict: dict) -> List[Tuple[str, str]]:
    """
    Perform part-of-speech tagging on a sentence using a dictionary.

    Parameters
    ----------
    sentence : str
        Input sentence
    pos_dict : dict
        Dictionary of words and their corresponding part-of-speech tags

    Returns
    -------
    pos_tags : Tuple[str, str]
        Tuple with the part-of-speech tags for each word in the sentence.
    """
    # Tokenize the text (basic split by spaces and punctuation removal)
    tokens = sentence.lower().replace('.', '').replace(',', '').split()

    # Function to tag each word using the dictionary
    def pos_tagger(word, pos_dict):
        return pos_dict.get(word, 'UNK')  # Return 'UNK' (Unknown) if word not found in dictionary

    # Apply POS tagging
    pos_tags = [(token, pos_tagger(token, pos_dict)) for token in tokens]
    return pos_tags


if __name__ == '__main__':
    # Sample sentence
    text = "The quick brown fox jumps over the lazy dog."

    # Basic dictionary for POS tagging
    pos_dict = {
        'the': 'DT',  # Determiner
        'quick': 'JJ',  # Adjective
        'brown': 'JJ',  # Adjective
        'fox': 'NN',  # Noun
        'jumps': 'VBZ',  # Verb (3rd person singular present)
        'over': 'IN',  # Preposition
        'lazy': 'JJ',  # Adjective
        'dog': 'NN'  # Noun
    }

    # Apply POS tagging
    pos_tags = pos_tagger(text, pos_dict)
    print(pos_tags)
    assert np.all(pos_tags == [('the', 'DT'), ('quick', 'JJ'), ('brown', 'JJ'), ('fox', 'NN'), ('jumps', 'VBZ'),
                                 ('over', 'IN'), ('the', 'DT'), ('lazy', 'JJ'), ('dog', 'NN')])
