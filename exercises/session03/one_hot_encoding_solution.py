import numpy as np

# Solution with the missing parts + dummy variable trap
class OneHotEncoder:
    """
    One-hot encoder for categorical data.
    """

    def __init__(self, drop_first=False):
        """
        One-hot encoder for categorical data.

        Parameters
        ----------
        drop_first: bool
            Whether to drop the first category or not.
            This is useful to avoid multicollinearity in linear models (dummy variable trap).

        Attributes
        ----------
        categories: list
            List of unique categories in the data.
        """
        self.categories = None
        self.drop_first = drop_first

    def fit(self, data: list):
        """
        Fit the encoder by determining unique categories in the data.

        Parameters
        ----------
        data: list
            List of categorical data
        """
        self.categories = sorted(set(data))

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
        if self.categories is None:
            raise Exception("The encoder has not been fitted yet.")

        one_hot_encoded = []
        for item in data:
            if self.drop_first:
                vector = [1 if category == item else 0 for category in self.categories[1:]]
            else:
                vector = [1 if category == item else 0 for category in self.categories]
            one_hot_encoded.append(vector)
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
        for vector in encoded_data:
            if self.drop_first:
                # For dummy encoding, need to handle case where all values are 0
                if np.sum(vector) == 0:
                    inverse_data.append(self.categories[0])
                else:
                    index = np.argmax(vector) + 1  # Adjust index since we dropped the first category
                    inverse_data.append(self.categories[index])
            else:
                index = np.argmax(vector)
                inverse_data.append(self.categories[index])
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

    # Test drop_first
    encoder = OneHotEncoder(drop_first=True)
    # What output do you expect here?
    encoder.fit(data)
    print(encoder.categories)
    print(encoder.transform(data))
    print(encoder.fit_transform(data))

    # What output do you expect here?
    encoded_data = np.array([[0, 0], [1, 0], [0, 0], [0, 1], [1, 0]])
    print(encoder.inverse_transform(encoded_data))