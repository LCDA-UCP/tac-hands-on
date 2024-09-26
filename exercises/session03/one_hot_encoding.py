import numpy as np


class OneHotEncoder:
    """
    One-hot encoder for categorical data.
    """

    def __init__(self):
        """
        One-hot encoder for categorical data.

        Attributes
        ----------
        categories: list
            List of unique categories in the data.
        """
        self.categories = None

    def fit(self, data: list):
        """
        Fit the encoder by determining unique categories in the data.

        Parameters
        ----------
        data: list
            List of categorical data
        """
        # Find unique categories in the data and sort them
        # add your code here
        unique = set(data)
        self.categories = sorted(unique)

    def transform(self, data: list) -> np.ndarray:
        """
        Transform the categorical data into one-hot encoded vectors.

        Parameters
        ----------
        data: list
            List of categorical data

        Returns
        -------
        np.ndarray
            Numpy array of one-hot encoded vectors
        """
        # Check if the encoder has been fitted
        # add your code here

        # Encode the data (i.e., convert each category into a one-hot encoded vector where the index of the 1 corresponds to the category)
        if self.categories is None:
            raise ValueError("One Hot Encoder nees fit before transform")

        one_hot_encoded = []
        for i in data:
            v = [0] * len(self.categories)
            for k, j in enumerate(self.categories):
                if i == j:
                    v[k] = 1
                    break
            one_hot_encoded.append(v)

        return np.array(one_hot_encoded)


    def fit_transform(self, data: list) -> np.ndarray:
        """
        Fit and transform the data in a single step.

        Parameters
        ----------
        data: list
            List of categorical data

        Returns
        -------
        np.ndarray
            Numpy array of one-hot encoded vectors
        """
        self.fit(data)
        return self.transform(data)

    def inverse_transform(self, encoded_data: np.ndarray) -> list:
        """
        Convert one-hot encoded data back into categorical values.

        Parameters
        ----------
        encoded_data: np.ndarray
            Numpy array of one-hot encoded vectors

        Returns
        -------
        list
            List of categorical data.
        """
        if self.categories is None:
            raise Exception("The encoder has not been fitted yet.")

        inverse_data = []
        # Convert one-hot encoded data back into categorical values
        # add your code here
        for i in encoded_data:
            for k, j in enumerate(i):
                if j == 1:
                    category = self.categories[k]
                    inverse_data.append(category)
                    break

        return inverse_data

if __name__ == '__main__':
    encoder = OneHotEncoder()
    data = ['cat', 'dog', 'cat', 'fish', 'dog']
    # What output do you expect here?
    encoder.fit(data)
    print(encoder.categories)
    print(encoder.transform(data))
    print(encoder.fit_transform(data))

    # What output do you expect here?
    encoded_data = np.array([[1, 0, 0], [0, 1, 0], [1, 0, 0], [0, 0, 1], [0, 1, 0]])
    print(encoder.inverse_transform(encoded_data))