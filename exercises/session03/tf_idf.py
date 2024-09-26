import math
from collections import Counter
from typing import List


class TFIDF:
    """
    A simple implementation of the Term Frequency-Inverse Document Frequency (TF-IDF) algorithm.
    """

    def __init__(self):
        """
        Initialize the TFIDF class.

        Attributes
        ----------
        documents : list of list
            The input documents to compute TF-IDF from.
        tf : list of dict
            The term frequency (TF) for each document.
        idf : dict
            The inverse document frequency (IDF) for each unique word in the corpus.
        tfidf : list of dict
            The TF-IDF score for each document.
        """
        self.documents = None
        self.tf = None
        self.idf = None
        self.tfidf = None

    def fit(self, documents: List[str]):
        """
        Fit the TF-IDF model on the input documents.

        Parameters
        ----------
        documents : list of list
            The input documents to compute TF-IDF from.

        Returns
        -------
        self : TFIDF
            Fitted TF-IDF instance.
        """
        documents_ = [document.split() for document in documents]
        self.documents = documents_
        self.tf = self.compute_tf()
        self.idf = self.compute_idf()
        self.tfidf = self.compute_tfidf()
        return self

    def transform(self) -> List[dict]:
        """
        Transform the fitted documents into TF-IDF vectors.

        Returns
        -------
        list of dict
            A list of dictionaries containing the TF-IDF vectors for the given documents.
        """
        return self.tfidf

    def fit_transform(self, documents: List[str]) -> List[dict]:
        """
        Fit the TF-IDF model and transform the documents into TF-IDF vectors.

        Parameters
        ----------
        documents : list of str
            The input documents to compute TF-IDF from.

        Returns
        -------
        list of dict
            A list of dictionaries containing the TF-IDF vectors for the given documents.
        """
        self.fit(documents)
        return self.transform()

    def compute_tf(self):
        """
        Compute term frequency (TF) for each document.

        Returns
        -------
        list of dict
            A list of dictionaries containing the term frequency for each word in the document.
        """
        tf = []
        # Compute the term frequency for each word in each document
        # add your code here
        for document in self.documents:
            word_count = Counter(document)
            size = len(document)
            tf.append({word : wc/size for word, wc in word_count.items()})
            tfi = {}
            for word, wc in word_count.items():
                tfi[word] = wc / size
        return tf

    def compute_idf(self):
        """
        Compute inverse document frequency (IDF) for each unique word in the corpus.
        """
        idf = {}
        # Compute the inverse document frequency for each word in the corpus
        # add your code here
        return idf

    def compute_tfidf(self):
        """
        Compute the TF-IDF score for each document.
        """
        idf = {}
        # Compute the TF-IDF score for each word in each document
        # add your code here
        total_documents = len(self.documents)
        words = set()
        for document in self.documents:
            words.update(document.split())

        for word in words:
            counter = 0
            for document in self.documents:
                if word in document.split():
                    counter += 1
            idf[word] = math.log(total_documents / counter)
        return tfidf


if __name__ == '__main__':
    documents = [
        'good boy',
        'good girl',
        'good boy girl'
    ]

    # using sklearn's TfidfVectorizer (results may vary)
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(documents)
    print(X.toarray())

    # Using our implementation
    tfidf = TFIDF()
    tfidf.fit(documents)
    print(tfidf.transform())

