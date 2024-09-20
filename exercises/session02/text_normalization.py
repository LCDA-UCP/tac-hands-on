import string

import contractions


def text_to_lowercase(text: str) -> str:
    """
    Convert text to lowercase.

    Parameters
    ----------
    text

    Returns
    -------
    str
        Lowercased text.
    """
    return text.lower()

def remove_punctuation(text: str) -> str:
    """
    Remove punctuation from text.

    Parameters
    ----------
    text

    Returns
    -------
    str
        Text without punctuation.
    """
    # add code here (note you can use the string package)
    # ...
    # res = ""
    # for char in text:
    #     if char not in string.punctuation:
    #        res = res + char
    return text.translate(str.maketrans('', '', string.punctuation))

def expand_contractions(text: str) -> str:
    """
    Expand contractions in text.

    Parameters
    ----------
    text

    Returns
    -------
    str
        Text with expanded contractions.
    """
    # add code here (note you can use the contractions package)
    # ...

    return contractions.fix(text)


if __name__ == '__main__':
    text = "I don't like this movie, it's not good."
    print(text_to_lowercase(text))
    assert text_to_lowercase(text) == "i don't like this movie, it's not good."
    print(remove_punctuation(text))
    assert remove_punctuation(text) == "I dont like this movie its not good"
    print(expand_contractions(text))
    assert expand_contractions(text) == "I do not like this movie, it is not good."

    text = text_to_lowercase(text)
    text = remove_punctuation(text)
    text = expand_contractions(text)
    print(text)
    assert text == "i do not like this movie its not good"
