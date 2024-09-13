from typing import Any

from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def one_hot_encoding_sklearn(df: pd.DataFrame, drop: Any = None):
    # Get the categorical columns
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

    # Initialize the OneHotEncoder
    encoder = OneHotEncoder(drop=drop, sparse_output=False)

    # Fit the encoder
    encoder.fit(df[categorical_columns])

    # Transform the data
    transformed_data = encoder.transform(df[categorical_columns])

    # Create a DataFrame with the transformed data
    transformed_df = pd.DataFrame(transformed_data, columns=encoder.get_feature_names_out(categorical_columns))

    # Concatenate the transformed data with the original data
    data = pd.concat([df, transformed_df], axis=1)

    # Drop the original categorical columns
    data.drop(categorical_columns, axis=1, inplace=True)

    return data


if __name__ == '__main__':
    data = {'Employee id': [10, 20, 15, 25, 30],
            'Gender': ['M', 'F', 'F', 'M', 'F'],
            'Remarks': ['Good', 'Nice', 'Good', 'Great', 'Nice'],
            }
    df1 = pd.DataFrame(data)

    print(df1)

    df1 = one_hot_encoding_sklearn(df1)

    print(df1)

    # Try with drop='first'
    df2 = pd.DataFrame(data)
    print(df2)
    df = one_hot_encoding_sklearn(df2, drop='first')

    print(df)

    # Note: you can also use encoder.inverse_transform to get back the original data