import string
from typing import List


def tokenize(text: str, condition: str) -> List[str]:
    """
    Tokenize text based on the condition.

    Parameters
    ----------
    text : str
        The input text to tokenize.
    condition : str
        The condition to tokenize the text.

    Returns
    -------
    list of str
        A list of tokens based on the condition.
    """
    return text.split(condition)

def tokenize_punctuation(text: str) -> List[str]:
    """
    Tokenize text based on punctuation.

    Parameters
    ----------
    text : str
        The input text to tokenize.

    Returns
    -------
    list of str
        A list of tokens based on punctuation.
    """
    for p in string.punctuation:
        text = text.replace(p, f" {p} ")
    return text.split()

if __name__ == '__main__':
    text = "This is a #sample text for #tokenization. It is a simple text."
    condition = " "
    tokens = tokenize(text, condition)
    print(tokens)
    assert tokens == ['This', 'is', 'a', '#sample', 'text', 'for', '#tokenization.', 'It', 'is', 'a', 'simple', 'text.']

    condition = "#"
    tokens = tokenize(text, condition)
    print(tokens)
    assert tokens == ['This is a ', 'sample text for ', 'tokenization. It is a simple text.']

    tokens = tokenize_punctuation(text)
    print(tokens)
    assert tokens == ['This', 'is', 'a', '#', 'sample', 'text', 'for', '#', 'tokenization', '.', 'It', 'is', 'a', 'simple', 'text', '.']
