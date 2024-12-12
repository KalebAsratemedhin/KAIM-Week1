import pandas as pd

def load_dataset(filepath):
    """
    Load the dataset from the given filepath.
    """
    return pd.read_csv(filepath)
