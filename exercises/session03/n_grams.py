from typing import List, Tuple


class NGram:
    """
    A class used to compute n-grams from text.

    Parameters
    ----------
    n : int, optional
        The size of the n-gram (default is 2, which computes bigrams).

    Attributes
    ----------
    n : int
        The size of the n-gram.
    ngrams : list of tuple
        The list of n-grams generated after fitting.
    """

    def __init__(self, n: int = 1):
        """
        Initialize the NGram class with the specified n value.

        Parameters
        ----------
        n : int, optional
            The size of the n-gram (default is 2 for bigrams).
        """
        self.n = n
        self.ngrams = None

    def fit(self, text: str):
        """
        Fit the n-gram model on the input text.

        Parameters
        ----------
        text : str
            The input text to compute n-grams from.

        Returns
        -------
        self : NGram
            Fitted n-gram instance.
        """
        # Tokenize the text into words
        words = text.split()

        # Generate n-grams
        self.ngrams =[]

        for i in range(len(words) - self.n + 1):
            self.ngrams.append(tuple(words[i:i + self.n]))



        return self

    def transform(self) -> List[Tuple[str]]:
        """
        Transform the fitted text into n-grams.

        Returns
        -------
        list of tuple
            A list of n-grams generated from the fitted text.

        Raises
        ------
        ValueError
            If the model is not yet fitted.
        """
        if self.ngrams is None:
            raise ValueError("The model is not fitted yet. Call `fit` first.")

        return self.ngrams

    def fit_transform(self, text: str) -> List[Tuple[str]]:
        """
        Fit the n-gram model and transform the text into n-grams.

        Parameters
        ----------
        text : str
            The input text to compute n-grams from.

        Returns
        -------
        list of tuple
            A list of n-grams generated from the input text.
        """
        self.fit(text)
        return self.transform()


if __name__=='__main__':
    # Example usage
    ngram_generator = NGram(n=3)
    text = "I love my dog"

    # Fit and transform the text
    trigrams = ngram_generator.fit_transform(text)

    print(trigrams)
