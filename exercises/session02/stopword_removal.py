from typing import List, Set

from pandas.core.computation.parsing import tokenize_string
def remove_stopwords2(tokens: List[str], stopwords: Set[str]) -> List[str]:
    """
    Remove stopwords from tokens.

    Parameters
    ----------
    tokens: List[str]
        List of tokens.
    stopwords: Set[str]
        Set of stopwords.

    Returns
    -------
    List[str]
        List of tokens without stopwords.
    """
    # add code here
    return [token for token in tokens if token not in stopwords]


def remove_stopwords(tokens: List[str], stopwords: Set[str]) -> List[str]:
    """
    Remove stopwords from tokens.

    Parameters
    ----------
    tokens: List[str]
        List of tokens.
    stopwords: Set[str]
        Set of stopwords.

    Returns
    -------
    List[str]
        List of tokens without stopwords.
    """
    # add code here
    for token in tokens:
        if token in stopwords:
            tokens.remove(token)
    return tokens


if __name__ == '__main__':
    stopwords = {'a', 'is', 'it', 'this', 'for'}
    tokens = ['this', 'is', 'a', 'sample', 'text', 'for', 'token', 'removal']
    print(remove_stopwords(tokens, stopwords))
    assert remove_stopwords(tokens, stopwords) == ['sample', 'text', 'token', 'removal']
