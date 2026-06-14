import os
import pandas as pd
from app.core import logger

class DatasetLoader:
    def __init__(self):
        """Initialize the loader with empty state."""
        self.filepath = None
        self.data = None
        
    def validate_file(self, path):
        """Validate the file path and format."""
        if not os.path.isfile(path):
            logger.error(f"The file {path} does not exist.")
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
            logger.error(f"Unsupported file format: {path_ext}. Only CSV files are allowed.")
            raise ValueError(f"Unsupported file format: {path_ext}. Only CSV files are allowed.")
        return True

    def load(self, path):
        """Load a CSV file into the data attribute."""
        
        # In a production environment, we would implement more robust validation and error handling here, such as checking for file size limits, validating the content of the CSV, and handling potential exceptions during loading.
        logger.info(f"Attempting to load dataset from {path}")
        """Load a CSV file into the data attribute."""
        self.filepath = path
        
        # Validate the file before loading
        self.validate_file(self.filepath)
        self.data = pd.read_csv(self.filepath)
        
        logger.info(f"Dataset loaded {self.data.shape[0]} rows successfully from {path}")
        return self.data
    
    def get_metadata(self):
        """Return metadata about the loaded dataset."""
        
        if self.data is None:
            logger.warning("No dataset loaded. Metadata is unavailable.")
            raise ValueError("No dataset loaded. Metadata is unavailable.")
        
        
        metadata = {
            "row_count": self.data.shape[0],
            "column_count": self.data.shape[1],
            "column_names": self.data.columns.tolist(),
            "file_path": self.filepath,
            "data_types": self.data.dtypes.astype(str).to_dict()
        }
        
        logger.info(f"Metadata retrieved for dataset: {metadata}")
        
        return metadata
