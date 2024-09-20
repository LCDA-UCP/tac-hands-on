from typing import List


def suffix_s_stemmer(terms: List[str]) -> List[str]:
    """
    Removes the s-suffix from all terms in a sequence.

    Parameters
    ----------
    terms : list of str
        A list of terms.

    Returns
    -------
    list of str
        A list of terms without the s-suffix.
    """
    stemmed_terms = []
    # add code here
    for term in terms:
        if term[-1] == 's':
            term = term[:-1]
            stemmed_terms.append(term)
        else:
            stemmed_terms.append(term)
    return stemmed_terms

if __name__ == '__main__':
    terms = ["dogs", "cats", "houses", "mice"]
    print(suffix_s_stemmer(terms))
    assert suffix_s_stemmer(terms) == ["dog", "cat", "house", "mice"]