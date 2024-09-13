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
    # add your code here
    # ...

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
    # add your code here (remember the string package)
    # ...

if __name__ == '__main__':
    text = "This is a #sample text for #tokenization. It is a simple text."

    # test the functions
