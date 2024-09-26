from typing import List, Set


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
    return [token for token in tokens if token not in stopwords]

if __name__ == '__main__':
    stopwords = {'a', 'is', 'it', 'this', 'for'}
    tokens = ['this', 'is', 'a', 'sample', 'text', 'for', 'token', 'removal']
    print(remove_stopwords(tokens, stopwords))
    assert remove_stopwords(tokens, stopwords) == ['sample', 'text', 'token', 'removal']
