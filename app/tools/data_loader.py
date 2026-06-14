import os
import pandas as pd

class DatasetLoader:
    def __init__(self):
        """Initialize the loader with empty state."""
        self.filepath = None
        self.data = None
        
    def validate_file(self, path):
        """Validate the file path and format."""
        if not os.path.isfile(path):
            raise FileNotFoundError(f"The file {path} does not exist.")
        return True

    def load(self, path):
        """Load a CSV file into the data attribute."""
        self.filepath = path
        self.validate_file(self.filepath)
        # We will add our robust validation steps here shortly
        self.data = pd.read_csv(self.filepath)
        return self.data