import pandas as pd
from app.tools.data_loader import load_csv

def test_load_csv_returns_valid_data():
    # We use a path relative to the project root, 
    # because that is where we will run the pytest command from.
    data_path = 'data/sample/students.csv'
    
    df = load_csv(data_path)
    
    # 1. Verify it actually returns a pandas DataFrame
    assert isinstance(df, pd.DataFrame)
    
    # 2. Verify the dataframe is not empty
    assert not df.empty