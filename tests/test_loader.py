import pytest
import pandas as pd
from app.tools.data_loader import DatasetLoader

def test_load_csv_returns_valid_data():
    """Test that the load_csv function returns a valid pandas DataFrame."""
    # We use a path relative to the project root, because that is where we will run the pytest command from.
    data_path = 'data/sample/students.csv'
    
    df = DatasetLoader().load(data_path)
    
    # 1. Verify it actually returns a pandas DataFrame
    assert isinstance(df, pd.DataFrame)
    
    # 2. Verify the dataframe is not empty
    assert not df.empty
    
# Test function for missing file

def test_load_raises_error_on_missing_file():
    loader = DatasetLoader()
    with pytest.raises(FileNotFoundError):
        loader.load("data/sample/does_not_exist.csv")

# Test function for unsupported file format

def test_load_raises_error_on_wrong_extension():
    loader = DatasetLoader()
    with pytest.raises(ValueError, match="Only CSV files are allowed"):
        loader.load("data/sample/document.csv.txt")