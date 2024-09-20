from typing import List, Dict


def lemmatization(text: List[str], lemmatization_dict: Dict[str, str]) -> List[str]:
    """
    Lemmatize a list of words based on a dictionary of lemmatization rules.

    Parameters
    ----------
    text : List[str]
        The list of words to lemmatize.
    lemmatization_dict : Dict[str, str]
        A dictionary that maps words to their lemmatized form.

    Returns
    -------
    lemmatized_text : List[str]
        The list of lemmatized words.
    """
    # add code here
    words =[]
    for word in text:
        if word in lemmatization_dict:
            lemmatized_word =lemmatization_dict[word]
            words.append(lemmatized_word)
        else:
            words.append(word)
    return words

if __name__ == '__main__':
    # Sample text
    text = ["the", "running", "runners", "ran", "quickly", "over", "the", "hills"]

    # Simple dictionary for lemmatization
    lemmatization_dict = {
        'running': 'run',
        'runners': 'runner',
        'ran': 'run',
        'hills': 'hill'
    }

    # Perform lemmatization
    lemmatized_text = lemmatization(text, lemmatization_dict)
    print(lemmatized_text)
    assert lemmatized_text == ['the', 'run', 'runner', 'run', 'quickly', 'over', 'the', 'hill']
