import pandas as pd

def load_csv(path):
    """Loads a CSV file into a pandas DataFrame."""
    return pd.read_csv(path)