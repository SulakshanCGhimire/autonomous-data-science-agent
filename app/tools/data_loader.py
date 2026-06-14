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
        """ 
            Robust form would have been to check file signature by using this code:
            with open(path, 'rb') as f:
            file_signature = f.read(4)
            if file_signature != b'\x50\x4B\x03\x04':  # ZIP file signature
                raise ValueError("The file is not a valid ZIP archive.") 
            We used the extension check for simplicity, but in production, we should implement a more robust validation method.
        """
        path_ext = os.path.splitext(path)[1].lower()
        if path_ext != '.csv':
            raise ValueError(f"Unsupported file format: {path_ext}. Only CSV files are allowed.")
        return True

    def load(self, path):
        """Load a CSV file into the data attribute."""
        self.filepath = path
        self.validate_file(self.filepath)
        # We will add our robust validation steps here shortly
        self.data = pd.read_csv(self.filepath)
        return self.data