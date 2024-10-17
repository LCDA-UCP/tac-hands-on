from typing import List

import numpy as np


class BagOfWords:
    """
    Bag of Words encoder.
    """

    def __init__(self):
        """
        Initialize the BagOfWords encoder.

        Attributes
        ----------
        vocabulary : dict
            A dictionary that maps words to indices.
        """
        self.vocabulary = {}

    def fit(self, documents: List[str]):
        """
        Fit the vocabulary based on a list of documents.

        Arguments
        ---------
        documents : List[str]
            List of strings (documents)
        """
        # Build the vocabulary
        vocab = set()
        # tokenize each document
        # add code here
        # ...

        # Assign an index to each word in the vocabulary
        self.vocabulary = {...}

    def transform(self, documents: List[str]) -> np.ndarray:
        """
        Transform the documents into a bag-of-words representation.

        Arguments
        ---------
        documents : List[str]
            List of strings (documents)

        Returns
        -------
        bow_matrix : np.ndarray
            Numpy array of shape (n_documents, n_features)
        """
        if not self.vocabulary:
            raise Exception("The vocabulary has not been fitted yet.")

        # Initialize the matrix with zeros (what is the shape of the matrix?)
        bow_matrix = ...

        # Fill the matrix with the counts of each word in the documents
        # add code here
        # ...

        return bow_matrix

    def fit_transform(self, documents: List[str]) -> np.ndarray:
        """
        Fit the vocabulary and transform the documents in a single step.

        :param documents: List of strings (documents)
        :return: Numpy array of shape (n_documents, n_features)
        """
        self.fit(documents)
        return self.transform(documents)

    def get_feature_names(self):
        """
        Get the feature names (vocabulary words).

        Returns
        -------
        feature_names : List[str]
            List of feature names (vocabulary words)
        """
        return list(self.vocabulary.keys())


if __name__ == '__main__':
    # Example usage
    documents = [
        "the cat in the hat",
        "the dog in the house",
        "the bird in the sky"
    ]

    # Initialize and fit-transform the Bag of Words
    bow_encoder = BagOfWords()
    bow_matrix = bow_encoder.fit_transform(documents)

    print("Bag of Words Matrix:\n", bow_matrix)
    print("\nVocabulary:\n", bow_encoder.get_feature_names())
