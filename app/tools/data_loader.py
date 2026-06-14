import pandas as pd

class DatasetLoader:
    def __init__(self):
        """Initialize the loader with empty state."""
        self.filepath = None
        self.data = None

    def load(self, path):
        """Load a CSV file into the data attribute."""
        self.filepath = path
        # We will add our robust validation steps here shortly
        self.data = pd.read_csv(self.filepath)
        return self.data